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

        BFS
        """
        if node is None:
            return None
        queue = []
        start_cloned_node = UndirectedGraphNode(node.label)
        visited = set()
        # A dictionary that maps labels to cloned nodes
        d = {node: start_cloned_node}
        queue.append(node)
        while queue:
            node = queue.pop(0)
            visited.add(node)
            cloned_node = d[node]
            cloned_neighbors = []
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                if neighbor not in d:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = cloned_neighbor
                else:
                    cloned_neighbor = d[neighbor]
                cloned_neighbors.append(cloned_neighbor)
            cloned_node.neighbors = cloned_neighbors
        return start_cloned_node
