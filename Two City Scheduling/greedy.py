def twoCitySchedCost(costs):
    #write code here
    n = len(costs)
    costs.sort(key = lambda x:x[0]-x[1])
    
    cost = 0
    
    for i in range(n//2):
        cost = cost + costs[i][0]
    
    for i in range(n//2,n):
        cost = cost + costs[i][1]
        
    return cost
