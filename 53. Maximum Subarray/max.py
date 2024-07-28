# for finding the subarray with the largest sum using Kadane's Algorithm is already optimal 
# in terms of time complexity, as it runs in 𝑂(𝑛) where 𝑛 is the length of the input array. 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        # Initialize max_current and max_global with the first element of the array
        first = second = nums[0]

        # Loop through the array starting from the second element
        for i in range(1,n):
            # Update max_current to be the maximum of the current element itself
            # or the current element plus the previous maximum subarray sum
            first = max(nums[i], first + nums[i])

            # Update max_global if max_current is greater than max_global
            if first>second:
                second = first
        return second
