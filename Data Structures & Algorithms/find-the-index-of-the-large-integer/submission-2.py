# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        length = reader.length()
        l, r = 0, length - 1

        # remember this compareSub is custom defined function, 
        # not usual range(len) which ignores the last index of range passed
        while length > 1:
            mid = (l + r)//2
            if length % 2 == 0:
                # for even length array
                ret_val = reader.compareSub(l, mid, mid+1, r)
                if ret_val > 0:
                    r = mid
                elif ret_val < 0:
                    l = mid + 1
            else:
                # for odd length array
                ret_val = reader.compareSub(l, mid-1, mid+1, r)
                if ret_val == 0:
                    return mid
                elif ret_val > 0:
                    r = mid
                else:
                    l = mid + 1
            length = r - l + 1
        # if not returned result from odd length array, 
        # then l will be at target index which is the answer
        return l
