from functools import cmp_to_key

def largestNumber(nums):
    #write code here 
    nums_str = list(map(str, nums))
    
    def compare(X,Y):
      # Compare two concatenated results
        if X+Y > Y+X:
            return -1
        else:
            return 1

    # Sort the array with the custom comparator
    nums_str.sort(key = cmp_to_key(compare))

    # Concatenate the sorted array
    result = ''.join(nums_str)

    # Handle the case where all numbers are zero
    if result[0] == '0':
        return '0'
    return result
