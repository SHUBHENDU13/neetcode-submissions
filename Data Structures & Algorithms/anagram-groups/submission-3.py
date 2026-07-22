class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            map[tuple(count)].append(word)

        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     if sorted_word not in map:
        #         map[sorted_word] = [word]
        #     else:
        #         map[sorted_word].append(word)

        res = []
        for key in map:
            res.append(map[key])

        return res

