class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict1 = {}
        my_dict2 = {}
        for c in s:
            if c not in my_dict1:
                my_dict1[c] = 1
            else:
                my_dict1[c] += 1
        
        for c in t:
            if c not in my_dict2:
                my_dict2[c] = 1
            else:
                my_dict2[c] += 1
        
        if (my_dict1 == my_dict2):
            return True
        return False