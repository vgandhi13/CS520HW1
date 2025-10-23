# humaneval_HumanEval_6 | Model: OLMo_2_1B | Strategy: scot
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
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    # Use regular expressions to split the string by parentheses
    paren_groups = re.findall(r'\((.*?)\)', paren_string)
    
    # Initialize the list to store the depths
    depths = []
    
    # Process each group of parentheses
    for group in paren_groups:
        # Initialize the current depth and maximum depth
        current_depth = 0
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If it's an opening parenthesis, increase current_depth
            if char == '(':
                current_depth += 1
            
            # Update max_depth if necessary
            # Remember to check after each ')' to avoid exceeding maximum depth
            else:
                max_depth = max(max_depth, current_depth)
        
        # Add the current depth to the list
        depths.append(max_depth)
    
    return depths