# humaneval_HumanEval_6 | Model: Llama_3.2_1B_Instruct | Strategy: scot
# Entry point: parse_nested_parens

# Problem prompt:
# from typing import List
# 
# 
# def parse_nested_parens(paren_string: str) -> List[int]:
#     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
#     For each of the group, output the deepest level of nesting of parentheses.
#     E.g. (()()) has maximum two levels of nesting while ((())) has three.
# 
#     >>> parse_nested_parens('(()()) ((())) () ((())()())')
#     [2, 3, 1, 3]
#     """
# 

# Paste your generated code below

from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): Input string containing groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    # Split the input string by spaces to extract each group of parentheses
    groups = paren_string.split()

    # Initialize an empty list depths to store the result for each group
    depths = []

    # Iterate over each group
    for group in groups:
        # Initialize current_depth = 0 and max_depth = 0
        current_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If '(', increment current_depth
            if char == '(':
                current_depth += 1
            # Update max_depth = max(max_depth, current_depth)
            max_depth = max(max_depth, current_depth)
            # If ')', decrement current_depth
            if char == ')':
                current_depth -= 1

        # Append max_depth to depths
        depths.append(max_depth)

    # After processing all groups, return depths
    return depths