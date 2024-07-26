def minCut(self, s: str) -> int:
    #write code here
    n = len(s)
    
    def palindrome(start,end):
        while(start<end):
            if s[start]!= s[end]:
                return False
            start += 1 
            end -= 1 
        return True
        
    def partition(start,end):
        #base case 
        if start == end or palindrome(start,end):
            return 0
        
        #recursive case 
        maxcut = end - start
        for index in range(start,end):
            if palindrome(start,index):
                maxcut = min(maxcut,1+partition(index+1,end))
                
        return maxcut
    return partition(0,len(s)-1)
        
            
