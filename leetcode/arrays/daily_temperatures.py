class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using a stack approach
        
        stack = [] # (value, index)
        answer = len(temperatures) * [0]
        
        stack.append((temperatures[0], 0))

        for i in range(1, len(temperatures)):

            while temperatures[i] > stack[-1][0]:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop(-1)
                
                if len(stack) == 0:
                    break
            
            stack.append((temperatures[i], i))
            
        return answer


            
            
            
                    
        
        