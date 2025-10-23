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
from typing import List, Str

def separate_paren_groups(paren_string: Str) -> List[str]:
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the groups
    groups = []
    
    # Initialize variables for tracking current group and balance
    current_group = ""
    balance = 0
    
    # Iterate through each character in the cleaned string
    for ch in paren_string:
        # Add the character to the current group
        current_group += ch
        
        # Step 2: Check if the current group is balanced (no unmatched open parenthesis)
        if ch == '(':
            balance += 1
        
        elif ch == ')':
            balance -= 1
        
        # Step 3: If the balance is zero, it means a complete group is found
        if balance == 0:
            groups.append(current_group)
            # Reset current group
            current_group = ""
    
    return groups