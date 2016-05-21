#!/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
from shift import shift_job

scheduler = BlockingScheduler()

# Creating shift table scheduled job
@scheduler.scheduled_job('interval', minutes=10)
def shift():
    shift_job()

scheduler.start()
