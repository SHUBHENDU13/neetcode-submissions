class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

    def _add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        self._add(x)
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x,y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        uf = UnionFind(len(synonyms))
        for x, y in synonyms:
            uf.union(x,y)

        groups = {}
        for word in list(uf.parent.keys()):
            root = uf.find(word)
            groups.setdefault(root, []).append(word)
        for root in groups:
            groups[root].sort()

        res = []
        words = text.split(" ")
        def backtrack(i):
            if i == len(words):
                res.append(' '.join(words))
                return
            if words[i] in uf.parent:
                root = uf.find(words[i])
                original = words[i]
                for syn in groups[root]:
                    words[i] = syn
                    backtrack(i + 1)
                words[i] = original
            else:
                backtrack(i + 1)
        
        backtrack(0)
        res.sort()
        return res

"""
PROBLEM:
Given synonym pairs and a sentence, generate all possible sentences
by substituting words with their synonyms (synonyms are transitive:
happy<->joy, joy<->glad means happy<->glad too).

WHY UNION-FIND:
- Synonymy is transitive -> need connected components of words
- Union-Find groups words efficiently (near O(1) per op with path
  compression + union by rank) as we merge pairs and later look up
  which group a word belongs to

WHY BACKTRACKING:
- "return ALL possible sentences" -> enumerate, not optimize
- Each word position = independent discrete choice (its synonym group,
  or itself if no synonyms exist) -> no complex pruning needed, just
  try every option and undo before trying the next

ALGORITHM:
1. Union-Find: merge all synonym pairs -> canonical root per word
2. Build `groups`: root -> sorted list of all words sharing that root
3. Backtrack over each word index i in the split sentence:
   - if words[i] has synonyms -> try each synonym in groups[root],
     recurse, then undo (restore original word) [classic apply/undo]
   - else -> just move to i+1, no branching
   - base case: i == len(words) -> join words, save sentence
4. Sort final result for lexicographic order

COMPLEXITY:
- Union-Find build: ~O(E * alpha(N)) for E synonym pairs
- Backtracking: O(product of group sizes across substitutable words)
  in the worst case (exponential, but bounded by actual synonym counts)
"""


        