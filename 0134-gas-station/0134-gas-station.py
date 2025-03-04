class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start_index = sum_tank = cur_sum = 0

        for i in range(len(gas)):
            
            sum_tank += gas[i] - cost[i]
            cur_sum += gas[i] - cost[i]

            if cur_sum < 0:
                start_index = i + 1
                cur_sum = 0


        return start_index if sum_tank >= 0 else -1


            

        