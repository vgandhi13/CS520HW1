# humaneval_HumanEval_6 | Model: OLMo_2_1B | Strategy: cot
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

    E.g. '(()())' has maximum two levels of nesting while '(())' has three.
    """

    # Initialize a list to store the maximum nesting depth for each group
    max_depths = []

    # Split the input string by spaces to get individual groups
    groups = paren_string.split()

    # Process each group
    for group in groups:
        # Remove any leading/trailing whitespace if necessary
        group = group.strip()

        # Count the number of opening parentheses
        opening_count = group.count('(')
        
        # Count the number of closing parentheses
        closing_count = group.count(')')

        # The nesting depth is the smaller of the two counts, as we're tracking the maximum level
        max_depth = min(opening_count, closing_count)

        # Append the maximum depth to the list
        max_depths.append(max_depth)

    return max_depths
