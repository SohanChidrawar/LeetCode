class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def helper(index,curr,summ):
            if summ > target:
                return
            if summ == target:
                result.append(curr[:])

            for j in range(index,n):
                curr.append(candidates[j])
                helper(j,curr,summ+candidates[j])
                curr.pop()
        
        helper(0,[],0)
        return result
        
