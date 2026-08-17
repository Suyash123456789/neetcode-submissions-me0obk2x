class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                if len(stack) >= 2:
                    a, b = stack.pop(), stack.pop()
                    stack.append(a + b)
            elif t == "-":
                if len(stack) >= 2:
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
            elif t == "*":
                if len(stack) >= 2:
                    a, b = stack.pop(), stack.pop()
                    stack.append(a * b)
            elif t == "/":
                if len(stack) >= 2:
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[0] if stack else 0

