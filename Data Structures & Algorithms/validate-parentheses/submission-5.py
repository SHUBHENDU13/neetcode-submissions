class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        opening_parentheses = '[{('
        for i in s:
            if i in opening_parentheses:
                myStack.append(i)
                continue
            if len(myStack) != 0:
                curr = myStack.pop()
            else:
                return False
            if (i == ']' and curr == '[') or (i == ')' and curr == '(') or (i == '}' and curr == '{'):
                continue
            else:
                return False
        if len(myStack) == 0:
            return True
        return False
        