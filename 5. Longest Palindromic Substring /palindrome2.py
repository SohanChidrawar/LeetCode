class Solution: 
    def longestPalindrome(self, s: str) -> str: 
        def is_palindrome(sub: str) -> bool: 
            return sub == sub[::-1] 
 
        n = len(s)  # Get the length of the input string 
        if n == 0: 
            return ""  # If the string is empty, return an empty string 
 
        # Initialize variables to track the longest palindrome 
        longest_palindrome = s[0] 
 
        # Loop through all possible substrings 
        for i in range(n): 
            for j in range(i + 1, n + 1): 
                substring = s[i:j]  # Get the substring from index i to j-1 
                # If it's a palindrome and longer than the current longest, update the longest palindrome 
                if is_palindrome(substring) and len(substring) > len(longest_palindrome): 
                    longest_palindrome = substring 
 
        return longest_palindrome 
