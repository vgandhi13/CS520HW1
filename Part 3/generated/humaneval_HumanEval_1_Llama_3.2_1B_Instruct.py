# humaneval_HumanEval_1 | Model: Llama_3.2_1B_Instruct | Strategy: cot
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
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate balanced groups of parentheses into separate strings.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a balanced group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize the counter and output list
    count = 0
    output = []

    # Initialize a flag to track whether we're inside a group
    inside_group = False

    # Iterate over each character in the input string
    for char in paren_string:
        # If we're inside a group and encounter an open parenthesis, increment the counter
        if inside_group and char == '(':
            count += 1
        # If we're inside a group and encounter a close parenthesis, decrement the counter
        elif inside_group and char == ')':
            count -= 1
            # If the counter becomes zero, it means we've reached the end of a group
            if count == 0:
                # Reset the counter and append a pair of parentheses to the output list
                count = 1
                output.append('()')
                # Set the flag to False to indicate we're no longer inside a group
                inside_group = False
        # If we encounter an open parenthesis, set the flag to True
        elif char == '(':
            inside_group = True
        # If we encounter a close parenthesis, set the flag to False
        elif char == ')':
            inside_group = False

    return output