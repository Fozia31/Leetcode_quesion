# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        prev, curr = None, head
        count = 0
        temp = head
        
        for _ in range(k):
            if not temp:
                return head
            temp = temp.next
        
        while count < k and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        
        if curr:
            head.next = self.reverseKGroup(curr, k)
        
        return prev
