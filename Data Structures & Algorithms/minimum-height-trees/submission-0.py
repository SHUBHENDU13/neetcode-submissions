class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst) 
            adj[dst].append(src) 

        res = []
        heights = {}

        def dfs(root, visit):
            if root in visit:
                return 0
            
            visit.add(root)
            maxhei = 0
            for nei in adj[root]:
                maxhei = max(maxhei, 1 + dfs(nei, visit))
            visit.remove(root)
            return maxhei
            
        for root in range(n):
            heights[root] = dfs(root, set())

        minval = min(heights.values())
        for key in heights:
            if heights[key] == minval:
                res.append(key)

        return res


        

        