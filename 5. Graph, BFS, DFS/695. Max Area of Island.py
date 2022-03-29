from collections import defaultdict
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = dict()

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                index = n * i + j
                if value == "0" or value == 0:
                    continue
                else:
                    graph[index] = []
                if (i - 1) >= 0:
                    # up
                    value = grid[i - 1][j]
                    cindex = n * (i - 1) + j
                    if value == 1 or value == "1":
                        graph[index].append(cindex)
                if (i + 1) < m:
                    # down
                    value = grid[i + 1][j]
                    cindex = n * (i + 1) + j
                    if value == 1 or value == "1":
                        graph[index].append(cindex)
                if (j - 1) >= 0:
                    # left
                    value = grid[i][j - 1]
                    cindex = n * i + (j - 1)
                    if value == 1 or value == "1":
                        graph[index].append(cindex)
                if (j + 1) < n:
                    # right
                    value = grid[i][j + 1]
                    cindex = n * i + (j + 1)
                    if value == 1 or value == "1":
                        graph[index].append(cindex)

        count = self.DFS(graph=graph)
        return count

    def DFS(self, graph):
        visited = set()
        size = 0
        max_size = 0
        for key in graph.keys():
            if key not in visited:
                self.doDFS(graph, key, visited)
                current = len(visited) - size
                if current > max_size:
                    max_size = current
                size = len(visited)
        return max_size

    def doDFS(self, graph, key, visited: set):
        if key not in visited:
            visited.add(key)
            for key in graph[key]:
                if key in graph.keys():
                    self.doDFS(graph, key, visited)


if __name__ == "__main__":
    s = Solution()
    count = s.numIslands(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    print(f"Max area of island: {count}")
