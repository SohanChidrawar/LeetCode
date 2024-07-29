def canJump(nums):
    #write code here
    n = len(nums)
    
    max_len = 0
    
    for i in range(n):
        if i > max_len:
            return False
        max_len = max(max_len, i + nums[i])
        
        if max_len >= n-1:
            return True
    return False
