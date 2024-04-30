You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

max1.py code uses slicing approach but is time complexity is O(n*k) where k: slicing window, so due to high complexity some test cases get fail

max2.py using dequeue approach and its time complexity is O(n). All test cases are pass
