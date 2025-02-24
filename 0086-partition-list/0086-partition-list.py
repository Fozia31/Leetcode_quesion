# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small = ListNode(0)
        pointer1 = dummy_small
        dummy_large = ListNode(0)
        pointer2 = dummy_large
        itr = head
        while itr:
            if itr.val < x:
                pointer1.next = itr
                pointer1 = pointer1.next
                
            else:
                pointer2.next = itr
                pointer2 = pointer2.next
                
            itr = itr.next

        pointer1.next = dummy_large.next
        pointer2.next = None
        return dummy_small.next


                

                



