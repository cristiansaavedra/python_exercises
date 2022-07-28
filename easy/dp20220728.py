# ---------------------------------------
# [Easy]
# This problem was asked by Palantir.
# Write a program that checks whether an integer is a palindrome. 
# For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
# Do not convert the integer into a string.
# ---------------------------------------

def is_palindrome(n):
    """

    n = integer number

    Function to know if a number is a palindrome
    palindrome = a word, phrase, or sequence that reads the same backward as forward

    Solution
    --------

    Using Slice notation [start:stop:step]. We use step = -1, which do a reverse

    """

    t1 = str(n)
    t2 = t1[::-1]
    return t1 == t2

print("Are the following numbers palindromes?")
print("121 ", is_palindrome(121))
print("888 ", is_palindrome(888))
print("678 ", is_palindrome(678))