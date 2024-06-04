def longest_palindrome(self, s: str) -> int:
    ss = set()  # Initialize an empty set to keep track of characters
    for letter in s:  # Iterate through each character in the string
        if letter not in ss:  # If the character is not in the set
            ss.add(letter)  # Add the character to the set
        else:  # If the character is already in the set
            ss.remove(letter)  # Remove the character from the set
    
    if len(ss) != 0:  # If the set is not empty
        return len(s) - len(ss) + 1  # Return the length of the string minus the size of the set plus one
    else:  # If the set is empty
        return len(s)  # Return the length of the string
