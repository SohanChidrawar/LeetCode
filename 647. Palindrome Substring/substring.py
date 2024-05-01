class Solution: 
    def countSubstrings(self, s: str) -> int: 
        # This helper function counts the number of palindromic substrings  
        # starting from a given center and expanding outward. 
        def count_palindrome(left: int, right: int) ->int: 
            count = 0 
            # Expand outward as long as the characters at the left and right pointers are the same 
            while(left >=0 and right < len(s) and s[left] == s[right]): 
                count+=1 
                left-=1 
                right+=1 
            return count 
 
        n = len(s) 
        total_substring = 0 
 
        # Loop through the string, considering each character as a center for odd length palindromes 
        for i in range(n): 
            # Count palindromic substrings with a single-character center (odd length) 
            total_substring += count_palindrome(i,i) 
 
        # Loop through the string, considering each character as a center for  even-length palindromes 
        for i in range(n-1): 
            # Count palindromic substrings with a single-character center (even length) 
            total_substring += count_palindrome(i,i+1) 
 
        return total_substring 
