# The idea is to keep track of both the maximum product and the minimum product up to the 
# current position, as the minimum product can become the maximum product when multiplied by a # negative number.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = min_prod = maximum = nums[0]

        for x in nums[1:]:
            if x<0:
                # Swap max_prod and min_prod when a negative number is encountered
                max_prod, min_prod = min_prod, max_prod
            
            # Update max_prod and min_prod
            max_prod = max(x,max_prod*x)
            min_prod = min(x,min_prod*x)

            # Update the global maximum product
            maximum = max(maximum,max_prod)

        return maximum

