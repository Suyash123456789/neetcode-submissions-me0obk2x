class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "+":
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            elif c == "C":
                if stack:
                    stack.pop()
            elif c == "D":
                if stack:
                    stack.append(2*stack[-1])
            else:
                stack.append(int(c))
        return sum(stack)