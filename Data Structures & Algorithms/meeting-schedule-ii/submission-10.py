"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([n.start for n in intervals])
        end = sorted([n.end for n in intervals])

        i = j = 0
        res, count = 0, 0

        while i < len(start):
            if start[i] < end[j]:
                count += 1
                res = max(res, count)
                i += 1
            else:
                count -= 1
                j += 1
        return res
