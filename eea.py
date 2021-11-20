import math

def gcd_eea(a, b): 

    if a == 0:  
        return b, 0, 1

    gcd_result = gcd_eea(b % a, a)
    gcd = gcd_result[0]
    new_x = gcd_result[1]
    new_y = gcd_result[2]
    
    z = math.floor(b/a) * new_x 
    result_x = new_y - z
    result_y = new_x 
     
    return [gcd, result_x, result_y]