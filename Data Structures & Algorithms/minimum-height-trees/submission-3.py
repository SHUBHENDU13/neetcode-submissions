class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(root, visit):
            if root in visit:
                return 0
            
            visit.add(root)
            maxhei = 0
            for nei in adj[root]:
                maxhei = max(maxhei, 1 + dfs(nei, visit))
            visit.remove(root)
            return maxhei

        mht = {}
        res = []
        for i in range(n):
            mht[i] = dfs(i, set())
        
        minval = min(mht.values())
        for root in mht:
            if mht[root] == minval:
                res.append(root)

        return res
        