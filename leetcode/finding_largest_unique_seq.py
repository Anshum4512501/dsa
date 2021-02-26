# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Input: s = ""
# Output: 0

def solution(string):
    if string:

        list_of_string = string.split()
        new_string_array = []
        newstring = ""
        for char in list_of_string:
            if char not in newstring:
                newstring = newstring+char
            else:
                new_string_array.append(newstring)
                newstring = char
        print(max([len(item)] for item in new_string_array)[0])  
    return 0       

solution("")        

        

