"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.
"""

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode

        DFS
        """
        if node is None:
            return None
        self.visited = set()
        cloned_node = UndirectedGraphNode(node.label)
        self.d = {node: cloned_node}
        self.visit(node)
        return self.d[node]

    def visit(self, node):
        if node not in self.visited:
            self.visited.add(node)
            cloned_node = self.d[node]
            cloned_neighbors = []
            for neighbor in node.neighbors:
                if neighbor not in self.d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    self.d[neighbor] = cloned_neighbor
                else:
                    cloned_neighbor = self.d[neighbor]
                cloned_neighbors.append(cloned_neighbor)
                self.visit(neighbor)
            cloned_node.neighbors = cloned_neighbors
