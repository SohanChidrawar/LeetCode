class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        perm = []

        def helper(i):
            if i==n-1:
                perm.append(nums[:])
                return

            hash = {}
            for j in range(i,n):
                if nums[j] not in hash:
                    hash[nums[j]]=True

                    nums[i], nums[j] =  nums[j], nums[i]
                    helper(i+1)
                    nums[i], nums[j] =  nums[j], nums[i]
        helper(0)
        return perm


        
