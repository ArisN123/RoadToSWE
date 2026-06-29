# 9. Palindrome Number
# Easy
# Topics
# premium lock iconCompanies
# Hint

# Given an integer x, return true if x is a , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
input = str(1000021)

input_as_list = list(input_as_str)
start_index = 0 
end_index = len(input_as_list)-1
while start_index <= end_index:
    print(f'start index is {start_index}, end_index is {end_index}')
    if input_as_list[start_index] != input_as_list[end_index]:
        flag = False
        break
    else:
        start_index = start_index + 1 
        end_index = end_index - 1 
    flag = True


print(flag)