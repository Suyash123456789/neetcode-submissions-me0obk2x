class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0 and a:
                    if stack[-1] > abs(a):
                        a = 0
                    elif stack[-1] < abs(a):
                        stack.pop()
                    else:
                        stack.pop()
                        a = 0
                if a:
                    stack.append(a)
            elif a > 0:
                stack.append(a)
            else:
                continue
        return stack


        