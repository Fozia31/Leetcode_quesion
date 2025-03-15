class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list_num=[]
        c=0
        for i in range(1,n+1):
            list_num.append(i)
        while len(list_num)>1:
            c=c+ (k-1)
            if c>=len(list_num):
                c=c%len(list_num)
                list_num.remove(list_num[c])
            else:
                list_num.remove(list_num[c])
        return list_num[0]






        