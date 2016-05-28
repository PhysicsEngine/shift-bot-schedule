import pulp
import numpy as np

#
# ShiftSolver solves the linear problem of give team shift table
# The number of shifts solved by ShiftSolver is at maximum `max_shift`
#
# Each request is a model.Request which has
# (id, member, team, start_time, end_time, availability)
#

class ShiftSolver:
    HOURS_IN_DAY = 24
    MINIMUM_MEMBERS = 3
    def __init__(self, team, member_list, days_in_shift=7):
        self.team = team
        self.member_list = member_list
        self.num_members = len(self.member_list)
        self.days_in_shift = days_in_shift
        self.problem = pulp.LpProblem('shift_table', pulp.LpMaximize)
        self.lp_variables = pulp.LpVariable.dicts(
            'VAR',
            (range(self.num_members), range(self.days_in_shift), range(ShiftSolver.HOURS_IN_DAY)),
            0, 1, 'Binary'
        )
        self.availability = np.zeros([
            self.num_members,
            self.days_in_shift,
            ShiftSolver.HOURS_IN_DAY
        ])

    def _init_availability(self, shift):
        '''
        @params shift: which includes (days, requests) in tuple format
        '''
        (days, requests, start_day) = shift
        start_in_shift = days[0]
        assert len(days) == self.days_in_shift
        for r in requests:
            if r.team == self.team:
                d = (r.start_time.date() - start_in_shift).days
                for t in xrange(r.start_time.hour, r.end_time.hour):
                    self.availability[r.member][d][t] = r.availability



    def solve(self, shift):
        self._init_availability(shift)
        # Create the objective function
        obj = None
        for m in xrange(self.num_members):
            for d in xrange(self.days_in_shift):
                for t in xrange(ShiftSolver.HOURS_IN_DAY):
                    obj += self.availability[m][d][t] * self.lp_variables[m][d][t]

        # Set objective function of this linear problem
        self.problem += obj

        # Set the contraint of variables of this problem
        for d in xrange(self.days_in_shift):
            for t in xrange(ShiftSolver.HOURS_IN_DAY):
                c = None
                for m in xrange(self.num_members):
                    c += self.lp_variables[m][d][t]
                self.problem += c >= ShiftSolver.MINIMUM_MEMBERS

        status = self.problem.solve()

        result = np.zeros([self.num_members, self.days_in_shift, ShiftSolver.HOURS_IN_DAY])
        for m in xrange(self.num_members):
            for d in xrange(self.days_in_shift):
                for t in xrange(ShiftSolver.HOURS_IN_DAY):
                    result[m][d][t] = self.lp_variables[m][d][t].value()

        return (pulp.LpStatus[status], result)
