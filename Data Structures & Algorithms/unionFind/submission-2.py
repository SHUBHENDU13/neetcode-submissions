class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.num_components = n  # count of number of components

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        # p1, p2 = self.find(x), self.find(y)
        # if p1 == p2:
        #     return True
        # return False
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        # totalComponents = set(self.par.values())
        # return len(totalComponents)
        return self.num_components
