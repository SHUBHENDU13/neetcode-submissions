class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        q = deque([src])
        visited = {src}
        while q:
            node = q.popleft()
            if node == dst:
                return True
            if node in self.adj:
                for child in self.adj[node]:
                    if child not in visited:
                        visited.add(child)
                        q.append(child)
        return False
