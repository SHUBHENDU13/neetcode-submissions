class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = defaultdict(list)
        for i in range(len(order)-1):
            c1, c2 = order[i], order[i + 1]
            adj[c1].append(c2)

        def dfs(c, target):
            if c == target:
                return True

            for nei in adj[c]:
                if dfs(nei, target): return True
            return False          
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if not dfs(w1[j], w2[j]): return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        
        return True

