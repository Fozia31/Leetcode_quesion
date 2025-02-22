# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head

        while itr and itr.next:

            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next


        return head







        # pointer1 = head
        # pointer2 = head.next
        # while pointer2 and pointer1.next:
             
        #     if pointer1.val == pointer2.val:
        #         pointer2 = pointer2.next
        #         pointer1 = pointer1.next.next
        #     else:    
        #         pointer1 = pointer1.next
        #         pointer2 = pointer2.next

        # return head
            
            
                
        