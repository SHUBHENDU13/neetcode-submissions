# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        """
        we want to return this as answer:
        ∑ val * (max_depth - depth + 1)
        this can be rewritten as:
        ∑ val * (max_depth + 1 - depth)
        ∑ val * (max_depth + 1) - ∑(val * depth)
        (max_depth + 1)∑(val) - ∑(val * depth)
        so the answer would be:
        (max_depth + 1) * sum_of_elements - sum_of_products
        """

        q = deque(nestedList)

        max_depth = 0
        depth = 1
        sum_of_elements = 0
        sum_of_products = 0

        while q:
            size = len(q)
            max_depth = max(max_depth, depth)
            for _ in range(size):
                nested = q.popleft()
                if nested.isInteger():
                    sum_of_elements += nested.getInteger()
                    sum_of_products += nested.getInteger() * depth
                else:
                    q.extend(nested.getList())
            depth += 1

        return (max_depth + 1) * sum_of_elements - sum_of_products


        