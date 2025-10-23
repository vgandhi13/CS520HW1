# humaneval_HumanEval_1 | Model: OLMo_2_1B | Strategy: cot
# Entry point: separate_paren_groups

# Problem prompt:
# from typing import List
# 
# 
# def separate_paren_groups(paren_string: str) -> List[str]:
#     """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
#     separate those group into separate strings and return the list of those.
#     Separate groups are balanced (each open brace is properly closed) and not nested within each other
#     Ignore any spaces in the input string.
#     >>> separate_paren_groups('( ) (( )) (( )( ))')
#     ['()', '(())', '(()())']
#     """
# 

# Paste your generated code below
from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input: A string containing multiple groups of nested parentheses.
    Returns: A list of separate strings representing each complete group of balanced parentheses.
    """
    # Step 1: Initialize an empty list to store the groups
    groups = []
    
    # Step 2: Define a counter to keep track of open parentheses
    open_count = 0
    
    # Step 3: Iterate through the string, check for balanced parentheses
    for char in paren_string:
        # Skip whitespace characters
        if char != ' ':
            # If a closing parenthesis is found, increment the open parenthesis counter
            if char == ')':
                open_count += 1
            
        # Step 4: Check if we have a complete group
        if open_count == len(paren_string):
            # Step 5: Add the balanced group to the list of groups
            groups.append(paren_string[:open_count])  # Append up to the first open parenthesis

    return groups
