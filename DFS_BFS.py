from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph: self.graph[u] = set()
        if v not in self.graph: self.graph[v] = set()
        self.graph[u].add(v)
    
    def dfs(self, node, visited = set()):
        if node not in self.graph: return
        print(node,end=" ")
        visited.add(node)
        for ne in self.graph[node]:
            if ne not in visited:
                visited.add(ne)
                self.dfs(ne, visited)

    def bfs(self, node):
        q = deque([node])
        visited = set([node])
        while q:
            curr = q.popleft()
            print(curr, end=" ")
            for node in self.graph[curr]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)

graph = Graph()
graph.add_edge('a','b')
graph.add_edge('a','c')
graph.add_edge('b','d')

graph.dfs('a')
print()
graph.bfs('a')
print()
