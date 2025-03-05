class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []
        for i in range(len(nums1)):
            next_max = 0
            x = nums2.index(nums1[i])
            for j in range(x,len(nums2),1):
                if nums1[i] < nums2[j]:
                    next_max = nums2[j]
                    break
            print(count)
            if next_max == 0:
                ans.append(-1)
            else:
                ans.append(next_max)

        return ans 
            
        