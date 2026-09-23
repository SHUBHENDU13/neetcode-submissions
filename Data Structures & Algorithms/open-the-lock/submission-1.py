class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if target in dead:
            return -1
        if "0000" in dead:
            return -1

        visit = set()
        q = deque()
        q.append([[0,0,0,0], 0])
        while q:
            cur, moves = q.popleft()
            if tuple(cur) in visit:
                continue
            visit.add(tuple(cur))
            comb = ''.join(str(n) for n in cur)
            if comb in dead:
                continue
            if comb == target:
                return moves
            for i in range(4):
                inc = list(cur)
                dec = list(cur)
                inc[i] = (inc[i] + 1) % 10
                dec[i] = ((dec[i] - 1) + 10) % 10
                q.append([inc, moves + 1])
                q.append([dec, moves + 1])
        return -1
