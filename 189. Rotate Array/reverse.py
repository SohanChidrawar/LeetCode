class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 0:
            return []
        
        k = k % n
        temp = nums[-k:]

        for i in reversed(range(0,n-k)):
            nums[i+k] = nums[i]
        
        for i in range(len(temp)):
            nums[i] = temp[i]

        return nums


        
