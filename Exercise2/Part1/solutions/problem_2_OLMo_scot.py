from math import floor

def truncate_number(number):
    # Get the integer part using floor
    int_part = floor(number)
    
    # Get the decimal part
    decimal_part = number - int_part

    return int_part, decimal_part
