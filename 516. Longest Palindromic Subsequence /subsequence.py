class Solution: 
    def longestPalindromeSubseq(self, s: str) -> int: 
        # Define a memoization dictionary to store calculated results 
        memo = {} 
         
        # Recursive function to calculate the LPS length from index `i` to `j` 
        def longest_palindrome(i, j): 
            # If indices cross, there's no valid palindrome 
            if i > j: 
                return 0 
            # If indices are the same, it's a single-character palindrome 
            if i == j: 
                return 1 
             
            # If this subproblem has already been solved, return the cached result 
            if (i, j) in memo: 
                return memo[(i, j)] 
             
            # If the first and last characters are the same, include them in the palindrome 
            if s[i] == s[j]: 
                memo[(i, j)] = 2 + longest_palindrome(i + 1, j - 1) 
            else: 
                # Otherwise, consider both options and choose the longest 
                memo[(i, j)] = max(longest_palindrome(i + 1, j), longest_palindrome(i, j - 1)) 
             
            return memo[(i, j)] 
         
        # Start the recursion from the whole string 
        return longest_palindrome(0, len(s) - 1)
