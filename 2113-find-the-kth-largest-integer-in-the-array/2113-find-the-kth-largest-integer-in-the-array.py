class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ans = []
        for num in nums:
            ans.append(int(num))
            
        ans.sort(reverse = True)
        return str(ans[k-1])