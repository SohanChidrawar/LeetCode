class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        zero, one, two = 0, 1, 1

        for i in range(3, n + 1):
            next_val = zero + one + two
            zero, one, two = one, two, next_val

        return two
