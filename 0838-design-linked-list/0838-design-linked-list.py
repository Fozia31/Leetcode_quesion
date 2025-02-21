class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0
        
    def get(self, index: int) -> int: 
        if index >= self.size or index < 0:
            return -1

        current = self.dummy.next
        count = 0

        while current:
            if index == count:
                return current.val
            count += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        newNode = Node(val)
        count = 0
        itr = self.dummy
        while itr:
            if count == index:
                newNode.next = itr.next
                itr.next = newNode
                self.size += 1
                return
            itr = itr.next
            count += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        count = 0
        itr = self.dummy
        while itr and itr.next:
            if count == index:
                itr.next = itr.next.next
                self.size -= 1
                return
            itr = itr.next
            count += 1
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)