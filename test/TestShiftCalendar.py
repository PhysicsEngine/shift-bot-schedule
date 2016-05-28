import unittest

from test_helper import ShiftCalendar
from test_requests import team1_requests

from datetime import date

class TestShiftCalendar(unittest.TestCase):

    def test_assert(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_iterweekdays(self):
        shift_calendar = ShiftCalendar(7)
        day = shift_calendar.shift_start_day(today=date(2016, 5, 28))
        self.assertEqual(date(2016, 5, 30), day)

        day = shift_calendar.shift_start_day(today=date(2016, 10, 1))
        self.assertEqual(date(2016, 10, 3), day)

    def test_iter_shift_table(self):
        shift_calendar = ShiftCalendar(7)
        shifts = shift_calendar.iter_shift_tables(3, team1_requests(), today=date(2016, 1, 1))
        self.assertEqual(1, len(shifts))
        self.assertEqual(date(2016, 1, 4), shifts[0][0][0])

    def test_shift_including_date(self):
        shift_calendar = ShiftCalendar(7)
        shifts = shift_calendar.iter_shift_tables(3, team1_requests(), today=date(2016, 1, 1))
        shift = ShiftCalendar.shift_including_date(date(2016, 1, 10), shifts)
        self.assertEqual(date(2016, 1, 4), shift[0][0])


if __name__ == "__main__":
    unittest.main()
