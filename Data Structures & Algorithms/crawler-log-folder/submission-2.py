class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for opr in logs:
            if opr == '../':
                if stack:
                    stack.pop()
            elif opr == './':
                continue
            else:
                stack.append(opr)
        return len(stack)