from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0  # Initialize balance at 0
    for op in operations:
        if op < 0:
            balance -= op  # Perform the withdrawal
        else:
            balance += op  # Perform the deposit
    return balance <= 0  # Return True if the balance ever drops below zero
