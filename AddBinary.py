class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # int(x,base = 2) 二进制转十进制
        # bin(x) 十进制转二进制，形式"0bxxxxxx"
        try:
            return bin(int(a, 2) + int(b, 2))[2:]
        except Exception as e:
            print(e,"非法二进制格式")
        finally:
            pass


if __name__ == '__main__':
    a = input("\ta = ")
    b = input("\tb = ")
    sol = Solution()
    print("\ta + b =", sol.addBinary(a, b))
