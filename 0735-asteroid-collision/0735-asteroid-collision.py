class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            while len(stack)!=0 and asteroids[i]<0 and stack[-1]>0:
                if stack[-1]< -asteroids[i]:
                    stack.pop()
                elif stack[-1]== -asteroids[i]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroids[i])
        return stack
        