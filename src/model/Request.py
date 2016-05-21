import sys
import os

class Request:
    def __init__(self, request):
        '''
        @param request: represents a request in tuple format
                        which includes (id, team, member, start_time, end_time, availability)
        '''
        assert len(request) == 6
        self.id = request[0]
        self.team = request[1]
        self.member = request[2]
        self.start_time = request[3]
        self.end_time = request[4]
        self.availability = request[5]
