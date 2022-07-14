class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = collections.deque()
        result = []
        
        # [5, 5, 5, -5]
        # s: [5, 10] 
        for i in range(len(asteroids)): 
                if len(stack) > 0 and asteroids[i] < 0 and stack[-1] > 0: 
                    while len(stack) > 0 and (stack[-1] > 0 and stack[-1] < abs(asteroids[i])): 
                        stack.pop()

                    if len(stack) > 0 and stack[-1] == abs(asteroids[i]): 
                        stack.pop()
                    
                    elif (len(stack) > 0 and stack[-1] < 0) or len(stack) == 0:
                        stack.append(asteroids[i])
                else: 
                    stack.append(asteroids[i])
        
        while len(stack) > 0: 
            result.append(stack.pop())
        
        return result[::-1]
    
    
     