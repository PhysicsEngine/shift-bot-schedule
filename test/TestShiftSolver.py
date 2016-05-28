import unittest

from test_helper import ShiftSolver
from test_helper import ShiftCalendar
from test_requests import team1_requests

from datetime import date

class TestShiftSolver(unittest.TestCase):

    def setUp(self):
        self.shift_calendar = ShiftCalendar(7)
        self.shifts = self.shift_calendar.iter_shift_tables(3, team1_requests(), today=date(2016, 1, 1))

    def test_solving_problem(self):
        solver = ShiftSolver(team=1, member_list=[0,1,2,3])
        for shift in self.shifts:
            (status, opt_shift) = solver.solve(shift)
            self.assertEqual("Optimal", status)
            self.assertEqual(opt_shift.shape, (4, 7, 24))


if __name__ == "__main__":
    unittest.main()
