# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = []
        for list_ in lists:
            head = list_
            itr = head
            while itr and itr.next:
                answer.append(itr.val)
                itr = itr.next
            if itr is not None:
                answer.append(itr.val)

        answer.sort()
        dummy = ListNode(0)
        cur = dummy
        for num in answer:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next










        
        