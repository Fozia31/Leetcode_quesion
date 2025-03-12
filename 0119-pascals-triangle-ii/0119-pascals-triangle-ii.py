class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1 ,1]
        # if rowIndex == 2:
        #     return [1,2,1]

        p_row = self.getRow( rowIndex - 1)
        ans = [1]

        for i in range(rowIndex - 1):
            ans.append( p_row[i] + p_row[i + 1])

        ans.append(1)

        return ans
        