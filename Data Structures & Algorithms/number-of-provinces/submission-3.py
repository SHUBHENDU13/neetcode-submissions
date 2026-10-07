class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        visit = [False] * n

        def dfs(node):
            visit[node] = True
            for nei in range(n):
                if isConnected[node][nei] == 1 and not visit[nei]:
                    dfs(nei)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        
        return res