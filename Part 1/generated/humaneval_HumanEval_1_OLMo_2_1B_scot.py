# humaneval_HumanEval_1 | Model: OLMo_2_1B | Strategy: scot
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

def separate_paren_groups(paren_string: str) -> List[str]: # Remove all spaces from the input paren_string cleaned_string = paren_string.replace(" ", "")

    # Initialize lists and counter
    groups = []
    current_group = ""
    balance = 0

    # Iterate over the cleaned string
    for char in cleaned_string:
        # Add the current character to the current group
        current_group += char
        
        # Check if it's a parenthesis ()
        if char == '(':
            # Increment balance
            balance += 1
        
        # Check if it's a closing parenthesis ')'
        elif char == ')':
            # Decrement balance
            balance -= 1
            
        # If balance is zero, it's a complete group, append to the list
        if balance == 0:
            groups.append(current_group)
            # Reset current group for the next group
            current_group = ""
            
    # Return the list of groups
    return groups

