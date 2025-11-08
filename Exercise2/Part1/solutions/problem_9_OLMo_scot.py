from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    
    result = []
    current_max = numbers[0]
    
    for n in numbers:
        if n > current_max:
            current_max = n
        else:
            result.append(current_max)
    
    return result
