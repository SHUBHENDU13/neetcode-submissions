class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                res = self.operate(a, b, c)
                stack.append(res)
        return stack[-1]

    def operate(self, a, b, opr):
        if opr == '+':
            return a + b
        elif opr == '-':
            return a - b
        elif opr == '*':
            return a * b
        elif opr == '/':
            return int(a / b)
        