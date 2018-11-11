class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划法
        j = 0
        ans = max(nums)
        temp = 0
        
        if(nums == []):
            return 0
        if(ans < 0):
            return ans
        
        while j < len(nums):
            temp = temp + nums[j]
            if(temp < 0):
                ans = max(ans,temp-nums[j])
                temp = 0
                j += 1
            else:
                ans = max(ans,temp)
                j += 1
        
        return ans
if __name__ == "__main__":
    nums = [1,-8,4,6,-8,-9,4,6,3,18,9,-5,4,-7,-4,-2,-8,62,1,3,-95,-5,-4,64,-87,0,-3,-8,6,98,4,8,5,32,1,-56]   
    solve = Solution()
    print(solve.maxSubArray(nums))
