class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c=="+" and len(stack)>=2:
                stack.append(stack.pop()+stack.pop())
            elif c=="*" and len(stack)>=2:
                stack.append(stack.pop()*stack.pop())
            elif c=="-" and len(stack)>=2:
                a, b=stack.pop(),stack.pop()
                stack.append(b-a)

            elif c=="/" and len(stack)>=2:
                a, b=stack.pop(),stack.pop()
                stack.append(int(b/a))

            else:
                stack.append(int(c))

        return stack[0] if stack else 0

            