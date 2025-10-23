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
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # Initialize balance to 0 and current_group to an empty string
    balance = 0
    current_group = ''

    # Initialize the list to store completed groups of parentheses
    completed_groups = []

    # Iterate over each character in the input string
    for char in paren_string.strip():
        # Add the character to the current group if it is a opening parenthesis
        if char == '(':
            balance += 1
            current_group += char
        # Add the character to the current group only if it is a closing parenthesis
        elif char == ')':
            balance -= 1
            if balance == 0:  # The group is complete
                completed_groups.append(current_group)
            current_group = ''

    # Return the list of completed groups
    return completed_groups