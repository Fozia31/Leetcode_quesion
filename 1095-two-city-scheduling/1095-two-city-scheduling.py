class Solution:
    def twoCitySchedCost(self, costs):

        for cost in costs:
            cost.append(cost[1] - cost[0])  

        for i in range(len(costs)):
            for j in range(0, len(costs)-i-1):
                print(costs[j][2])
                if costs[j][2] > costs[j+1][2]:
                    costs[j], costs[j+1] = costs[j+1], costs[j]  

        for cost in costs:
            cost.pop()  

        N = len(costs) // 2 
        total_cost = 0
        
        for i in range(N):
            total_cost += costs[i][1] 
        for i in range(N, 2 * N):
            total_cost += costs[i][0] 
        
        return total_cost
