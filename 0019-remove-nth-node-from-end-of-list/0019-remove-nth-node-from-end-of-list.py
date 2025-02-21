# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        itr = head
        while itr and itr.next:
            itr = itr.next
            count += 1

        deposite = count - n
        dummy = ListNode()
        counter = 0
        dummy.next = head
        itr = dummy

        while itr and counter < deposite:
            print(1)
            itr = itr.next
            counter += 1

        if itr and counter == deposite:
            if itr.next:
                itr.next = itr.next.next

        return dummy.next

        