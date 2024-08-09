class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            middle = (left+right)//2

            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]:
                #left part is sorted
                if target >= nums[left] and target<=nums[right]:
                    #explore left part
                    right = middle-1
                else:
                    left = middle+1

            else:
                #right part is sorted
                if  target <= nums[right] and target > nums[middle] :
                    #explore right part
                    left = middle+1
                else:
                    right = middle-1

        return -1
