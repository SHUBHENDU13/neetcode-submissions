class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = ['a', 'e', 'i', 'o', 'u']
        vowels = set(vowel_set)
        hashmap = {}
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                hashmap[word] = True
            else:
                hashmap[word] = False

        res = []
        for i,j in queries:
            count = 0
            while i <= j:
                if hashmap[words[i]] == True:
                    count += 1
                i += 1
            res.append(count)

        return res
            