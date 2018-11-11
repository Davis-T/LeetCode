class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        先将nums排序,设定三个指针遍历nums,分别为left,mid,right
        left = 0 -> len(nums)-3
        right = len(nums)-1 -> left+2
        mid = left <- (left+right)/2 -> right
        sum < 0 , mid ->
        sum > 0 , mid <-
        sum = 0 , collect.append(sum)
        如果 sum前后变号，则 right -= 1
        """
        nums.sort()
        n = len(nums)
        collect = []
        for left in range(0, n - 2):
            if(nums[left] > 0):
                break
            for right in range(n - 1, left, -1):
                if(nums[right] < 0):
                    break
                mid = (left + right) // 2
                last_sum = 0
                this_sum = nums[left] + nums[mid] + nums[right]
                omid = (mid > left and mid < right)
                goon = True
                while (this_sum * last_sum) >= 0 and omid and goon:
                    if(this_sum < 0):
                        mid += 1
                    elif(this_sum > 0):
                        mid -= 1
                    else:
                        if([nums[left], nums[mid], nums[right]] not in collect):
                            collect.append(
                                [nums[left], nums[mid], nums[right]])
                        goon = False
                    omid = (mid > left and mid < right)
                    last_sum = this_sum
                    this_sum = nums[left] + nums[mid] + nums[right]
        return collect


if(__name__ == "__main__"):
    import time
    t1 = time.process_time()
    nums = [-12, 4, 12, -4, 3, 2, -3, 14, -14, 3, -12, -7, 2, 14, -11, 3, -6, 6,
            4, -2, -7, 8, 8, 10, 1, 3, 10, -9, 8, 5, 11, 3, -6, 0, 6, 12, -13,
            -11, 12, 10, -1, -15, -12, -14, 6, -15, -3, -14, 6, 8, -9, 6, 1, 7,
            1, 10, -5, -4, -14, -12, -14, 4, -2, -5, -11, -10, -7, 14, -6, 12, 1,
            8, 4, 5, 1, -13, -3, 5, 10, 10, -1, -13, 1, -15, 9, -13, 2, 11, -2,
            3, 6, -9, 14, -11, 1, 11, -6, 1, 10, 3, -10, -4, -12, 9, 8, -3, 12,
            12, -13, 7, 7, 1, 1, -7, -6, -13, -13, 11, 13, -8]
    sol = Solution()
    collect = sol.threeSum(nums)
    t2 = time.process_time()
    t = t2 - t1
    print(collect, "\n time = {} s".format(t))
    