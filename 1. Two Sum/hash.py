class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_available = {}
        for i in range(0,n):
            needed_val = target - nums[i]

            if needed_val in num_available:
                return[i,num_available[needed_val]]
            else:
                num_available[nums[i]] = i
        return []

