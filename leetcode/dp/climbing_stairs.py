class Solution:
    def climbStairs(self, n: int) -> int:
        # # recursive/brute-force approach, O(2^n)
        #     return self.one_step(n) + self.two_steps(n)

        # def one_step(self, n):
        #     if n - 1 == 0 :
        #         return 1
        #     elif n - 1 < 0:
        #         return 0 
        #     n -= 1
        #     return self.one_step(n) + self.two_steps(n)   

        # def two_steps(self, n):
        #     if n - 2 == 0 :
        #         return 1
        #     elif n - 2 < 0:
        #         return 0 
        #     n -= 2
        #     return self.one_step(n) + self.two_steps(n)   

        # # backwards dp implementation, O(n), but also space complexity O(n)
        # dp = [0] * (n + 1)
        # for i in range(n, -1, -1):
        #     if i == n:
        #         dp[i] = 1
        #     elif i == n - 1:
        #         dp[i] = 1
        #     else:
        #         dp[i] = dp[i + 1] + dp[i + 2]
        
        # return dp[0]

        # fibonaccis implementation, dp, 
        p1, p2 = 1, 1
        for i in range(n - 1):
            temp = p1
            p1 += p2
            p2 = temp
        return p1



    

