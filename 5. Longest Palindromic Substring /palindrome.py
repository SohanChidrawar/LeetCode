class Solution: 
    def longestPalindrome(self, s: str) -> str: 
        # Helper function to expand around a given center and find the longest palindrome 
        def expand_around_center(left: int, right: int) -> (int, int): 
            while(left >= 0 and right < len(s) and s[left] == s[right]): 
                left -= 1 
                right += 1 
            # Return the start and length of the palindrome found 
            return (left + 1, right - left - 1) 
 
        n = len(s)  # Get the length of the input string 
        if n == 0: 
            return ""  # If the string is empty, there's no palindrome 
 
        # Initialize variables to track the longest palindrome 
        start, max_length = 0, 1 
 
        # Loop through each character to consider it as a center for odd-length palindromes 
        for i in range(n): 
            # Expand around a single-character center (odd-length palindrome) 
            left, length = expand_around_center(i, i) 
            if length > max_length: 
                start = left 
                max_length = length 
 
            # Expand around a two-character center (even-length palindrome) 
            if i < n - 1: 
                left, length = expand_around_center(i, i + 1) 
                if length > max_length: 
                    start = left 
                    max_length = length 
 
        # Return the longest palindromic substring based on the start index and length 
        return s[start:start + max_length] 
