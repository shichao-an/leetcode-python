# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []
        n = len(intervals)
        if n == 1:
            return intervals
        else:
            # Sort the intervals by start value
            intervals.sort(key=lambda x: x.start)
            res = []
            res.append(intervals[0])
            cur_end = intervals[0].end
            cur_index = 0
            for interval in intervals[1:]:
                if interval.start <= cur_end:
                    if interval.end > cur_end:
                        res[cur_index].end = interval.end
                        cur_end = interval.end
                else:
                    # Added a non-overlapping interval
                    res.append(interval)
                    cur_end = interval.end
                    cur_index += 1
            return res
