#!/usr/bin/env python

import os
from urlparse import urlparse
from datetime import datetime
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
pg_credential = urlparse(DATABASE_URL)

def shift_job():
    print("Creating shift tables... {}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
    create_shift_table_by_team()

# private
def create_shift_table_by_team(team=1):
    conn = psycopg2.connect(host=pg_credential.hostname,
                            port=pg_credential.post,
                            user=pg_credential.username,
                            password=pg_credential.password,
                            database=pg_credential.path[1:]) # To remove slash

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM requests WHERE team={}".format(team))
    for request in cursor:
        print(request)

    cursor.close()
    conn.close()
