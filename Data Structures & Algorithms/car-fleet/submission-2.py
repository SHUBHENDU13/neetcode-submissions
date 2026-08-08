class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort() # sort based on 1st element, i.e, position
        pair.reverse() # reverse so we start with the car closest to target position
        stack = []
        for p, s in pair:
            # add the speed of car on stack
            stack.append((target - p) / s)
            # if stack has atleast 2 speeds and 
            # time taken by behind car is less than the car in front, 
            # remove the behind car which is at top of stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)