class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []
        

    def pushFront(self, val: int) -> None:
        self.arr.insert(0,val)
        

    def pushMiddle(self, val: int) -> None:
        index = len(self.arr) // 2
        self.arr.insert(index,val)
        

    def pushBack(self, val: int) -> None:
        self.arr.append(val)
        

    def popFront(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr.pop(0)
        

    def popMiddle(self) -> int:
        index = (len(self.arr) -1) // 2
        if len(self.arr) == 0:
            return -1
        return self.arr.pop(index)
        

    def popBack(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()