class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        count = 0
        count = len(points)
        pre = points[0]
        for i in range(1 , len(points)):
            if points[i][0]  <= pre[1] :
                count -=  1
                pre = [points[i][0] , min(pre[1] ,points[i][1] )]
            else:
                pre =  points[i]
        return count

        