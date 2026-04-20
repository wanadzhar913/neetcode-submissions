"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Attempt 1
        hashset = set()
        for i in intervals:
            for j in list(range(i.start, i.end)):
                if j in hashset:
                    return False
                else:
                    hashset.add(j)
        return True




