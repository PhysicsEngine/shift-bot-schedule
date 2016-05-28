#!/usr/bin/env python

import os
from urlparse import urlparse
from datetime import datetime
import json
import psycopg2

from model.Request import Request
from ShiftCalendar import ShiftCalendar
from ShiftSolver import ShiftSolver

DATABASE_URL = os.environ['DATABASE_URL']
pg_credential = urlparse(DATABASE_URL)

def shift_job():
    print("Creating shift tables... {}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
    create_shift_table_by_team()

# private
# Team 1 is mainly for debug
def create_shift_table_by_team(team=1):
    conn = psycopg2.connect(host=pg_credential.hostname,
                            port=pg_credential.port,
                            user=pg_credential.username,
                            password=pg_credential.password,
                            database=pg_credential.path[1:]) # To remove slash
    cursor = conn.cursor()
    members = []
    cursor.execute("SELECT * FROM members WHERE team = {} ORDER BY id".format(team))
    for m in cursor:
        members.append(m[0])
    cursor.execute("SELECT days_in_shift, max_shift_count_in_routine FROM teams WHERE id={}".format(team))
    (days_in_shift, max_shift_count_in_routine) = cursor.fetchone()
    print("days_in_shift: {}, max_shift_count_in_routine: {}".format(days_in_shift, max_shift_count_in_routine))
    cursor.execute("SELECT * FROM requests WHERE team={} AND start_time >= current_date".format(team))
    requests = [Request(r) for r in cursor]
    optimized_shifts = optimize_shifts(team, members, requests)

    # Now optimal
    for s in optimized_shifts:
        ((status, time_table), start_date) = s
        json_time_table = json.dumps({
            'time_table': time_table.tolist()
        })
        ret = cursor.execute("INSERT INTO shifts (team, start_date, time_table) VALUES(%s, %s, %s)", (team, start_date, json_time_table))

    cursor.close()
    conn.close()

def optimize_shifts(team, members, requests):
    shift_calendar = ShiftCalendar(days_in_shift=7)
    shift_solver = ShiftSolver(team, members, days_in_shift=7)

    shifts = shift_calendar.iter_shift_tables(3, requests)
    optimized_shifts = [(shift_solver.solve(s), s[2]) for s in shifts]
    return optimized_shifts


if __name__ == "__main__":
    create_shift_table_by_team(team=1)
