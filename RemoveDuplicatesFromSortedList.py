# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 设置头节点，指向给定的链表头节点
        first = ListNode(-1)
        first.next = head
        # 上一节点
        last = first
        # 当前节点
        curr = head
        while curr and curr.next:
            if(curr.val != curr.next.val):
                curr = curr.next
                last = last.next
            else:
                last = last.next
                val = curr.val
                # 过滤重复节点
                while curr and curr.val == val:
                    curr = curr.next
                last.next = curr
        return first.next

# 列表转链表：
class ListToLinkedlist:
    def __init__(self,sortedlist):
        curr = ListNode(sortedlist[0])
        self.first = ListNode(-1)
        self.first.next = curr

        for i in range(1,len(sortedlist)):
            curr.next = ListNode(sortedlist[i])
            curr = curr.next

# 执行
if(__name__ == "__main__"):
    sortedlist = [1,2,3,3,4,5,6,6,6,7,8,9,10,10,11,12,13,13,14,15,16,16,16,17,18,18,19,20,23,25,26,28,29,30,32,36,38,31]
    head = ListToLinkedlist(sortedlist).first.next

    s = Solution()
    res = s.deleteDuplicates(head)

    while res:
        print(res.val)
        res = res.next