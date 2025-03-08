class DataStream:

    def __init__(self, value: int, k: int):
        self.que = []
        self.k = k
        self.value = value
    def consec(self, num: int) -> bool:

        if num == self.value:
            if len(self.que) < self.k:
                self.que.append(num)
        else:
            self.que = []
            
        return len(self.que) == self.k
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)