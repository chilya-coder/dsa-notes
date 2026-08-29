# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Iterative approach
        # # Time Complexity: O(n)
        # # Space Complexity: O(1)
        # # Remove connection between 1 -> 2; save 2 to nxt
        # # 1 (current) should be pointint on previous (null)
        # curr, prev = head, None
        # nxt = None

        # while(curr):
        #     nxt = curr.next
        #     curr.next = prev # 1 -> null

        #     prev = curr 
        #     curr = nxt # 2

        #return prev

        # Recursive approach
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newHead
        