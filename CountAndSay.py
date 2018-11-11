class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n == 1):
            return "1"
        # 递归
        s = self.countAndSay(n - 1)

        i = 0
        j = 1
        count = 1
        new_s = ""
        while j < len(s):
            if(s[i] == s[j]):
                count += 1
                j += 1
            else:
                new_s = new_s + str(count) + str(s[i])
                i = j
                j += 1
                count = 1

        if(i != j):
            new_s = new_s + str(count) + str(s[i])

        return new_s


if __name__ == '__main__':

    while 1:
        n = int(input("Give the val of n, if input -1 then quit:\n"))
        if(n < 1 or n > 30):
            break
        CountAndSay = Solution()
        print(CountAndSay.countAndSay(n))
