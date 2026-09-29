class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number) * string)
            else:
                stack.append(c)
        return "".join(stack)