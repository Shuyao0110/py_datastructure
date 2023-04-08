# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 递归解法
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.Next is None:
            return head
        first = head
        second = head.next
        pass_val = self.swapPairs(second.next)
        first.next = pass_val
        second.next = first
        return second
    # 迭代解法

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 翻转操作需要和前一次second链接，用prev记录
        # 但是首节点没有前一个节点，还需要单独讨论
        # 加入dummy节点可减少讨论：
        # 1.空节点
        # 2.只有一个节点
        # 3.有一有二：（1）如果是首节点，不用连接操作；（2）非首节点，需和prev连接
        dummy = ListNode()
        dummy.next = head
        prev, first = dummy, head
        # and前一为否，不执行其后，所以复国first为空，first.next也不会报错
        while first is not None and first.next is not None:
            second = first.next
            prev.next, first.next = second, second.next
            second.next = first
            prev = first
            first = prev.next
        return dummy.next
