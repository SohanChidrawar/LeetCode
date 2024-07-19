class Solution:
    def fib(self, n: int) -> int:
        ht = {0:0,1:1}
        def helper(n):
            if n in ht:
                return ht[n] 
            else:
                ht[n] = helper(n-1) + helper(n-2)
                return ht[n]
        return helper(n)
