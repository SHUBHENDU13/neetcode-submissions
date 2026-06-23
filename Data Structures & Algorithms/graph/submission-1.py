class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        if dst not in self.adjList[src]:
            self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList:
            return False
        for i in range(len(self.adjList[src])):
            if self.adjList[src][i] == dst:
                self.adjList[src].remove(dst)
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True
        visit = set()
        queue = deque()
        visit.add(src)
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True
                
                for neighbour in self.adjList[curr]:
                    if neighbour not in visit:
                        visit.add(neighbour)
                        queue.append(neighbour)
        return False
