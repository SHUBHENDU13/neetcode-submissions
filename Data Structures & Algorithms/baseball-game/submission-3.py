class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # score = []

        # for i in range(len(operations)):
        #     if operations[i] == '+':
        #         score.append(score[-1] + score[-2])
        #     elif operations[i] == 'C':
        #         score.pop()
        #     elif operations[i] == 'D':
        #         score.append(2 * score[-1])
        #     else:
        #         score.append(int(operations[i]))
        
        # return sum(score)

        stack, res = [], 0
        for op in operations:
            if op == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                res += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == "C":
                res -= stack.pop()
            else:
                res += int(op)
                stack.append(int(op))
        return res