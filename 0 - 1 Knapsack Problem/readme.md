You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.

In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

Example 1:

Input:

N = 3

W = 4

values[] = {1,2,3}

weight[] = {4,5,1}

Output: 3

Explanation: Choose the last item that weighs 1 unit and holds a value of 3.


Example 2:

Input:

N = 3

W = 3

values[] = {1,2,3}

weight[] = {4,5,6}

Output: 0

Explanation: Every item has a weight exceeding the knapsack's capacity (3).


Your Task:

Complete the function knapSack() which takes maximum capacity W, weight array wt[], value array val[], and the number of items n as a parameter and returns the maximum possible value you can get.

Expected Time Complexity: O(N*W).

Expected Auxiliary Space: O(N*W)
