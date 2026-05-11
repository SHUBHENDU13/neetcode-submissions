class Solution:
    def isValid(self, s: str) -> bool:
        # myStack = []
        # opening_parentheses = '[{('
        # for i in s:
        #     if i in opening_parentheses:
        #         myStack.append(i)
        #         continue
        #     if len(myStack) != 0:
        #         curr = myStack.pop()
        #     else:
        #         return False
        #     if (i == ']' and curr == '[') or (i == ')' and curr == '(') or (i == '}' and curr == '{'):
        #         continue
        #     else:
        #         return False
        # if len(myStack) == 0:
        #     return True
        # return False

        stack = []
        closeToOpen = {'}':'{', ')':'(', ']':'['}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        