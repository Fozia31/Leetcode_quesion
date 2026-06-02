class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        
        def calc(start1, dur1, start2, dur2):
            first_finish = min(s + d for s, d in zip(start1, dur1))
            
            ans = float('inf')
            for s, d in zip(start2, dur2):
                ans = min(ans, max(first_finish, s) + d)
            
            return ans
        
        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )