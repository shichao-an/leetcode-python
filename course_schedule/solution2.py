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
import sys

sys.setrecursionlimit(5000)

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Detect if course prerequisites graph has a cycle.
        """

        self.unvisited = set(range(numCourses))
        self.visiting = set()
        self.visited = set()
        self.graph = {x: set() for x in range(numCourses)}
        for c, p in prerequisites:
            self.graph[p].add(c)

        for u in range(numCourses):
            if u in self.unvisited:
                if self.visit(u) is False:
                    return False
        return True

    def visit(self, u):
        if u in self.visiting:
            return False
        elif u in self.unvisited:
            self.unvisited.remove(u)
            self.visiting.add(u)
            for v in self.graph[u]:
                if self.visit(v) is False:
                    return False
            self.visiting.remove(u)
            self.visited.add(u)

s = Solution()
print(s.canFinish(1, []))
print(s.canFinish(3, [[1, 0], [0, 1]]))
with open('test.txt') as f:
    args = f.read().split()
    arg0 = int(args[0][:-1])
    arg1 = eval(args[1])
    print(s.canFinish(arg0, arg1))
