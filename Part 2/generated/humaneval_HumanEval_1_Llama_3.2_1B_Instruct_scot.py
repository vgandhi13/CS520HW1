# humaneval_HumanEval_1 | Model: Llama_3.2_1B_Instruct | Strategy: scot
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
    """Separate multiple groups of balanced parentheses into distinct strings.
    
    Args:
        parens (str): Input string containing multiple groups of balanced parentheses.
    
    Returns:
        List[str]: A list of strings representing the separate groups of parentheses.
    """
    groups = []
    current_group = ""
    balance = 0

    for ch in parens:
        if ch == '(':
            balance += 1
            current_group += ch
        elif ch == ')':
            if balance == 0:
                groups.append(current_group)
                current_group = ""
            balance -= 1

    if balance != 0:
        raise ValueError("The input string does not contain balanced parentheses.")

    return groups