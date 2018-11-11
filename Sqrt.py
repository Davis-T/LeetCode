class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1 = x/2
        x2 = (x1 + x/x1)/2
        while abs(x2-x1)>1e-8:
            x1 = x2
            x2 = (x1 + x/x1)/2
            
        return x2
if __name__ == '__main__':
    # main()
    sol = Solution()
    print(sol.mySqrt(int(input("x = "))))