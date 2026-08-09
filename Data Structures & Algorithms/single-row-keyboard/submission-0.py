class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        for i in range(len(keyboard)):
            hashmap[keyboard[i]] = i
        res = 0
        prev = 0
        for c in word:
            res += abs(hashmap[c] - prev)
            prev = hashmap[c]
        return res