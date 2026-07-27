class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strings:
            key = []
            for i in range(len(word)-1):
                diff = (ord(word[i+1]) - ord(word[i]))%26
                key.append(diff)

            key = tuple(key)
            hash_map[key].append(word)

        res = []
        for key in hash_map:
            res.append(hash_map[key])
        return res
