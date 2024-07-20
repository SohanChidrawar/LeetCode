class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        one = 1
        two = 1
        if n<=1:
            return n
        if n==2 :
            return 1
        
        for i in range(3,n+1):
            next = zero + one + two
            zero = one
            one = two
            two = next
        return next
