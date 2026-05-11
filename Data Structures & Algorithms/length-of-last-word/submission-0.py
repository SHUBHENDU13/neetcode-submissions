class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tempList = s.split()
        lastWord = tempList[-1]
        return len(lastWord)