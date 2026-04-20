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
        # hashset = set()
        # for i in intervals:
        #     for j in list(range(i.start, i.end)):
        #         if j in hashset:
        #             return False
        #         else:
        #             hashset.add(j)
        # return True

        # Attempt 2 (Buggy!)
        # if len(intervals) < 2:
        #     return True

        # intervals.sort(key=lambda x: x.start)

        # for i in range(len(intervals)-1):
        #     if intervals[i+1].start < intervals[i].end:
        #         return False
        #     else:
        #         return True

        # Attempt #3
        if len(intervals) < 2:
            return True

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
            




