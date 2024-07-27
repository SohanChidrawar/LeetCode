class Solution:
    def matrixMultiplication(self, N, arr):
        # code here        
        def findcost(i,j):
            if i==j:
                return 0
             
            min_cost = float('inf')
            for k in range(i,j):
                curr_cost = findcost(i,k)+findcost(k+1,j)+arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost,curr_cost)
                
            return min_cost         
        return findcost(1,N-1)
