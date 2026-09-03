# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, l1:Optional[ListNode])->Optional[ListNode]:
        curr, prev = l1, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def getValue(self, prev:Optional[ListNode])->value:
        num = 0
        while prev:
            num *=10
            num += prev.val
            prev = prev.next
        return num
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = self.reverseList(l1)
        prev2 = self.reverseList(l2)
        num1 = self.getValue(prev1)
        num2 = self.getValue(prev2)
        sum = num1 + num2
        s = str(sum)
        
        dummy = ListNode(0)
        curr = dummy
        
        for i in s:
            curr.next = ListNode(int(i))
            curr = curr.next
        reversed_res = self.reverseList(dummy.next)
        return reversed_res