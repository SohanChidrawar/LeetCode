# Given n = 10
n = 10
# Limit m for the multiplication table (in this case, it's 10)
m = 10

# Initialize sum value
sum_value = 0

# Loop to get the sum of all multiples of n from 1 to m
for i in range(1, m + 1):
    sum_value += n * i

print("Output:", sum_value)
