class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(nums, target, left, right):
            if left>right:
                return -1
            middle = (left+right)//2

            if nums[middle] == target:
                return middle
            
            elif nums[middle]<target:
                return helper(nums,target,middle+1, right)
            
            else:
                return helper(nums,target,left,middle-1)

        return helper(nums,target,0,len(nums)-1)
