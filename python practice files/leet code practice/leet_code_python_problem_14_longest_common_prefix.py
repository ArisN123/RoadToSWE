# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


words = ["flower","flow","flight"]
max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

output = ''


def test_function(words):

    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    output = ''
    for letter in range(0,max_len):
            letter_to_find = words[0][letter]
            for word in words:
                if word[letter]!=letter_to_find:
                    return(output)
            output = output + letter_to_find
    return(output)


print(test_function(words))
# if word[0][0] = word[1][0] = word[2][0]

