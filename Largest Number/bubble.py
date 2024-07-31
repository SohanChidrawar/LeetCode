def largestNumber(nums):
    # Convert each number to a string
    nums = list(map(str, nums))
    
    # Define the custom comparison function
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Perform bubble sort using the custom comparator
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if compare(nums[j], nums[j + 1]) > 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # Concatenate the sorted numbers
    result = ''.join(nums)
    
    # Handle the case where the result is all zeros
    if result[0] == '0':
        return '0'
    
    return result
