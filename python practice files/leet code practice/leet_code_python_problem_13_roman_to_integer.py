# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 
roman_value_to_int_dict = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}

s = 'MCMXCIV'
input_as_list = list(s)
sum_of_nums = 0 
flag = False


for letter_index in range(0,len(input_as_list)):
        if flag == True:
              flag = False
              continue
        if letter_index == len(input_as_list)-1:
            sum_of_nums = sum_of_nums + roman_value_to_int_dict[input_as_list[letter_index]]
        elif (input_as_list[letter_index] == 'I' and input_as_list[letter_index+1]  in ['V','X']) or (input_as_list[letter_index] == 'X' and input_as_list[letter_index+1]  in ['L','C']) or (input_as_list[letter_index] == 'C' and input_as_list[letter_index+1]  in ['D','M']):
                sum_of_nums = sum_of_nums + roman_value_to_int_dict[input_as_list[letter_index+1]] - roman_value_to_int_dict[input_as_list[letter_index]]
                flag = True
                print(f'current letter is {input_as_list[letter_index]}, next letter is {input_as_list[letter_index+1]}, new sum is {sum_of_nums}')
        else:
            sum_of_nums = sum_of_nums + roman_value_to_int_dict[input_as_list[letter_index]]
            print(f'current letter is {input_as_list[letter_index]}, new sum is {sum_of_nums}')

print(sum_of_nums)
