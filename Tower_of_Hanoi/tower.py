class Solution:
    def toh(self, n, fromm, to, aux):
        # Your code here
        count = 0
        def helper(n, fromm, to, aux):
            nonlocal count
            if n==1:
                count+=1
                print("move disk "+ str(n)+" from rod "+str(fromm)+" to rod "+str(to))
                
                return
            
            helper(n-1,fromm,aux,to)
            print("move disk "+ str(n)+" from rod "+str(fromm)+" to rod "+str(to))
            count+=1
            helper(n-1,aux,to,fromm)
        helper(n, fromm, to, aux)
        return count
