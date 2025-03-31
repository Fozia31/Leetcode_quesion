class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        count=0
        for i in range(n):
            if citations[i]>=n-i:
                count=n-i
                break
        return count