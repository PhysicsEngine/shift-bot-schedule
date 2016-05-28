import os
import sys
from calendar import Calendar
from datetime import date
from datetime import timedelta

#
# One shift usually represents one week or one month
# A shift should include the days which can be devided by 7
# In short, one shift must be composed of some weeks
#

class ShiftCalendar(Calendar):
    def __init__(self, days_in_shift=7, first_day_in_week=0):
        '''
        shift table is created each one week as default which
        is specified by days_in_shift
        first_day specifies the start date of shift calendar
        default 0 specifies monday
        '''
        assert days_in_shift % 7 == 0
        assert first_day_in_week < 7
        super(ShiftCalendar, self).__init__(first_day_in_week)
        self.days_in_shift = days_in_shift

    @classmethod
    def shift_including_date(cls, day, shifts):
        '''
        Return the shift which includes give date
        '''
        for i, shift in enumerate(shifts):
            if day in shift[0]:
                return shifts[i]
        return None

    def shift_start_day(self, today=date.today()):
        '''
        Return the start date of next shift tables from today
        '''
        weeks = self.monthdatescalendar(today.year, today.month)
        shift_start_day = None
        for week in weeks:
            for i, day in enumerate(week):
                if today <= day:
                    shift_start_day = day + timedelta(days=7 - i)
                    break
            if not shift_start_day is None:
                break

        return shift_start_day

    def iter_shift_tables(self, max_shift, requests, today=date.today()):
        '''
        Return the shift table. A shift table includes several shift at most
        `max_shift` count in list format.
        shifts[max_shift] = (days, requests)
        '''
        shift_start_day = self.shift_start_day(today)
        shifts = []
        for i in xrange(max_shift):
            start_day = shift_start_day + timedelta(days=self.days_in_shift * i)
            end_day = start_day + timedelta(days=self.days_in_shift)
            shift = [start_day + timedelta(days=interval)
                     for interval in xrange(0, self.days_in_shift)]
            requests_in_shift = []
            for request in requests:
                if start_day <= request.start_time.date() and request.end_time.date() <= end_day:
                    requests_in_shift.append(request)
            if len(requests_in_shift) != 0:
                shifts.append((shift, requests_in_shift, start_day))

        return shifts
