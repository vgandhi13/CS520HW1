from typing import List
import itertools

def filter_by_substring(strings: list[str], substring: str) -> list[str]:
    """
    Filter an input list of strings by removing elements that don't contain a given substring.
    
    Args:
        strings (list[str]): Input list of strings.
        substring (str): The substring to filter by.
    
    Returns:
        list[str]: A list of strings that contain the substring.
    """
    # Use list comprehension to create a new list with the input list transformed
    return [s for s in strings if substring in s]
