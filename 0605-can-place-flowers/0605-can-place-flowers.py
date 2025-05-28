class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        Zero_count = 1
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                Zero_count +=1
            else:
                n -= ((Zero_count - 1)//2)
                Zero_count = 0


        if Zero_count >= 2:
            n -= Zero_count //2
        return n <=0
        