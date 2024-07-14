class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        for i in range(n):
            res[i] = nums[i]**2
        res.sort()

        return res
