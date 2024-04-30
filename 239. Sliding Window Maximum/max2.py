from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        # Deque to store indices of array elements, ensuring maximum at front
        dq = deque()
        # Remove elements that are out of this window (front of deque)
        for i in range(len(nums)):
            if dq and dq[0] < i-k+1:
                dq.popleft()
            # Remove indices from the back whose values are less than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

             # Add current element index to the deque
            dq.append(i)

            # If the window has enough elements, add the maximum to the result
            if i >=k-1:
                result.append(nums[dq[0]])
        
        return result
