# humaneval_HumanEval_10 | Model: OLMo_2_1B | Strategy: scot
# Entry point: make_palindrome

# Problem prompt:
# 
# 
# def is_palindrome(string: str) -> bool:
#     """ Test if given string is a palindrome """
#     return string == string[::-1]
# 
# 
# def make_palindrome(string: str) -> str:
#     """ Find the shortest palindrome that begins with a supplied string.
#     Algorithm idea is simple:
#     - Find the longest postfix of supplied string that is a palindrome.
#     - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
#     >>> make_palindrome('')
#     ''
#     >>> make_palindrome('cat')
#     'catac'
#     >>> make_palindrome('cata')
#     'catac'
#     """
# 

# Paste your generated code below

from typing import List