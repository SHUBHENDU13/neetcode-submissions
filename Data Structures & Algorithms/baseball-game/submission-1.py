class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i in range(len(operations)):
            if operations[i] == '+':
                score.append(score[-1] + score[-2])
            elif operations[i] == 'C':
                score.pop()
            elif operations[i] == 'D':
                score.append(2 * score[-1])
            else:
                score.append(int(operations[i]))
        
        return sum(score)