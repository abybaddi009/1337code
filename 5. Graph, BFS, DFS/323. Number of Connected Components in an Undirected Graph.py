from typing import List

class Solution():
    def countComponents(self, edges: List[List[str]]) -> int:
        graph = {}
        for edge in edges:
            start, end = sorted(edge)
            if start not in graph.keys():
                graph[start] = []
            graph[start].append(end)
        
        count = 0
        visited = set()
        for key in graph.keys():
            if key not in visited:
                count += 1
                self.DFS(graph=graph, node=key, visited=visited)
        return count

    def DFS(self, graph: dict, node, visited):
        if node not in visited:
            visited.add(node)
            for key in graph.get(node, []):
                self.DFS(graph=graph, node=key, visited=visited)



if __name__ == '__main__':
    s = Solution()
    count = s.countComponents(
        edges=[[0, 1], [1, 2], [3, 4]]
    )
    assert count == 2
    count = s.countComponents(
        edges=[[0, 1], [1, 2], [2, 3], [3, 4]]
    )
    assert count == 1
