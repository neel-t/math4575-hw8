import math

def fast_power(base, power):

    result = 1
    while power > 0:
        
        if power % 2 == 0:
            power = math.floor(power / 2)
            base *= base
        else:
            power -= 1
            result *= base
            power = math.floor(power / 2)
            base *= base

    return result