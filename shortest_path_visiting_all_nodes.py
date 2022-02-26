"""
847. Shortest Path Visiting All Nodes
You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node.
You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Constraints:
n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
"""

from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodeCount = len(graph)
        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = deque([(i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] iff
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            count = len(queue)

            while count:
                currentNode, visited = queue.popleft()
                if visited == allVisited:
                    return steps

                # start bfs from each neighbor
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_visited == allVisited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        # no path which explores every node
        return inf
