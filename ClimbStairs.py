class Solution:
    def climbStairs1(self, n):
        """
        方法一:迭代
        :type n: int
        :rtype: int
        """
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        if(n >= 3):
            s1 = self.climbStairs1(n-1)
            s2 = self.climbStairs1(n-2)
            return s1 + s2
            
    def climbStairs2(self, n):
        """
        方法2:斐波那契数列
        :type n: int
        :rtype: int
        """
        fib = [0] * (n+1)
        fib[0] = 1
        fib[1] = 2
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n-1]
        
if (__name__ == "__main__"):
    import time
    n = int(input("please input n:"))
    sol = Solution()
    start1 = time.clock()
    sol1 = sol.climbStairs1(n)
    end1 = time.clock()
    t1 = end1 - start1
    start2 = time.clock()
    sol2 = sol.climbStairs2(n)
    end2 = time.clock()
    t2 = end2 - start2
    print("\tsol1 = {0}\tt1 = {1} s\n\tsol2 = {2}\tt2 = {3} s".format(sol1,t1,sol2,t2))