# humaneval_HumanEval_7 | Model: Llama_3.2_1B_Instruct | Strategy: scot
# Entry point: filter_by_substring

# Problem prompt:
# from typing import List
# 
# 
# def filter_by_substring(strings: List[str], substring: str) -> List[str]:
#     """ Filter an input list of strings only for ones that contain given substring
#     >>> filter_by_substring([], 'a')
#     []
#     >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
#     ['abc', 'bacd', 'array']
#     """
# 

# Paste your generated code below
from typing import List
import itertools

def filter_by_substring(strings: list[str], substring: str) -> list[str]:
    """
    Filter an input list of strings by removing elements that don't contain a given substring.
    
    Args:
        strings (list[str]): Input list of strings.
        substring (str): The substring to filter by.
    
    Returns:
        list[str]: A list of strings that contain the substring.
    """
    # Use list comprehension to create a new list with the input list transformed
    return [s for s in strings if substring in s]
