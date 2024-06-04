Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindromethat can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Detailed Explaination
------------------------------------------------------------------------------------------------------------------

1. ss = set()
An empty set ss is initialized to keep track of characters that appear an odd number of times in the string.

2. for letter in s:
    if letter not in ss:
        ss.add(letter)
    else:
        ss.remove(letter)
   
The code iterates through each character (letter) in the string s.

If the character is not in the set ss, it means it is appearing for the first time (or another odd occurrence), so the character is added to the set.

If the character is already in the set ss, it means it is appearing for the second time (or another even occurrence), so the character is removed from the set.

By the end of this loop, the set ss will contain all characters that have appeared an odd number of times in the string.

3. if len(ss) != 0:
    return len(s) - len(ss) + 1
  else:
    return len(s)

If the set ss is not empty (len(ss) != 0), it means there are characters with odd frequencies.

  The length of the longest palindrome that can be formed is given by len(s) - len(ss) + 1.
  
  This formula works because len(s) - len(ss) gives the length of characters that can pair up to form a palindrome, and +1 allows for one odd character to be placed in the center of the palindrome.
  
If the set ss is empty (len(ss) == 0), it means all characters have even frequencies.

  The length of the longest palindrome in this case is simply the length of the string len(s) because all characters can be used to form a perfect palindrome.  


Example visualisation:

Consider the string "abccccdd":

After iterating through the string:
a is added to ss: ss = {'a'}

b is added to ss: ss = {'a', 'b'}

c is added to ss: ss = {'a', 'b', 'c'}

c is removed from ss: ss = {'a', 'b'}

c is added to ss: ss = {'a', 'b', 'c'}

c is removed from ss: ss = {'a', 'b'}

d is added to ss: ss = {'a', 'b', 'd'}

d is removed from ss: ss = {'a', 'b'}

After processing, ss contains {'a', 'b'} which means characters a and b have odd frequencies.

Since len(ss) != 0, the length of the longest palindrome is calculated as len(s) - len(ss) + 1, which is 8 - 2 + 1 = 7.
