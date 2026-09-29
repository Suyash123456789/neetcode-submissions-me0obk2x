class Solution:
    def simplifyPath(self, path: str) -> str:
        c = ""
        stack = []

        for p in path + "/":
            if p == "/":
                if c == "..":
                    if stack:
                        stack.pop()
                elif c != "." and c:
                    stack.append(c)
                c = ""
            else:
                c += p
        return "/" + "/".join(stack)