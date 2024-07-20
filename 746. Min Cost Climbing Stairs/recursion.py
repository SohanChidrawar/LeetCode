class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def helper(index):
            #base condition
            if index > n-1:
                return 0

            #recursive condition

            onestep = cost[index] + helper(index+1)
            twostep = cost[index] + helper(index+2)

            mincost[index] = min(onestep,twostep)
            return mincost[index]

        return min(helper(0), helper(1))
