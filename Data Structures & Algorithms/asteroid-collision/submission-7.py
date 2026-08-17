class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            
            if a < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(a):
                        stack.pop()
                    elif stack[-1] == abs(a):
                        stack.pop()
                        a = 0
                        break
                    else:
                        a = 0
                        break
            if a != 0:
                stack.append(a)
        return stack
