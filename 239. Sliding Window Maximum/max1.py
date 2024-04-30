class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result= []

        for i in range(len(nums)-k+1):
            current = nums[i:i+k]

            window = max(current)

            result.append(window)
        
        return result
        
