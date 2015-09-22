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
        BFS with only a queue and dictionary (used as visited set)
        """
        if node is None:
            return None
        queue = []
        start_node = node
        start_cloned_node = UndirectedGraphNode(node.label)
        d = {node: start_cloned_node}
        queue.append(node)
        i = 0
        while i < len(queue):
            node = queue[i]
            i += 1
            for neighbor in node.neighbors:
                if neighbor not in d:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
        for node in queue:
            cloned_node = d[node]
            cloned_neighbors = []
            for neighbor in node.neighbors:
                cloned_neighbor = d[neighbor]
                cloned_neighbors.append(cloned_neighbor)
            cloned_node.neighbors = cloned_neighbors
        return d[start_node]
