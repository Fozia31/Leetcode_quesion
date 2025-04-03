class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]

        for key , value in count.items():
            bucket[value].append(key)

        result = []

        for i in range(len(bucket) - 1, -1, -1):

            for num in bucket[i]:

                result.append(num)
                if len(result) == k:
                    return result


        
        

     
     