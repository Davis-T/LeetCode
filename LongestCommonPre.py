class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        com = ""
        if(strs == []):
            return ""
        for each in list(zip(*strs)):
            # zip(*strs) strs中元素是可迭代的，返回一个zip对象，由strs各元素组成的元组
            if(len(set(each)) == 1):
                # set()转成集合
                com += each[0]
            else:
                return com
        return com


if __name__ == '__main__':
    w = ["llopssign", "llosodw", "llopeas"]
    s = Solution()
    print(s.longestCommonPrefix(w))
