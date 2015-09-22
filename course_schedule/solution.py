"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course
1. So it is impossible.
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Topological sort
        """
        # An implementation of
        # https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
        #
        # Graph in which each node has its prerequisite courses as a
        # adjacency list
        queue = []
        finished_courses = []
        prq_graph = {x: set() for x in range(numCourses)}
        for c, p in prerequisites:
            prq_graph[c].add(p)

        # Add nodes with no prerequisites
        for c in prq_graph:
            if not prq_graph[c]:
                queue.append(c)

        # For each of the remaining node, remove its prerequisites in queue;
        # if node has no prerequisites, add it to queue, and repeat
        while queue:
            u = queue.pop(0)
            for v, prqs in prq_graph.items():
                if u in prqs:
                    prqs.remove(u)
                    if not prqs:
                        queue.append(v)
            finished_courses.append(u)

        return len(finished_courses) == numCourses

s = Solution()
print(s.canFinish(1, []))
print(s.canFinish(3, [[1, 0], [0, 1]]))
