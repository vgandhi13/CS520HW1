# humaneval_HumanEval_7 | Model: OLMo_2_1B | Strategy: cot
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
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring.lower() in s]