import math
from fast_power import fast_power
 
def is_prime(num):
    
    for n in range(2, int((num**1) / 2) + 1):
        if num % n == 0:
            return False

    return True

def get_prime_factors(n):

    prime_factors = set()
 
    while (n % 2 == 0):
        prime_factors.add(2)
        n = math.floor(n / 2)
 
    for i in range(3, int(math.sqrt(n)), 2):
        while (n % i == 0) :
            prime_factors.add(i)
            n = math.floor(n / i)
    
    if (n > 2) :
        prime_factors.add(n)

    return prime_factors

def get_primitive_roots(n):
 
    if not is_prime(n):
        return None

    primitive_roots = set()
 
    phi = n - 1 
    prime_factors = get_prime_factors(phi)
 
    for possible_root in range(2, phi + 1):
 
        is_primitive_root = False
        
        for prime_factor in prime_factors:
            if fast_power(possible_root, math.floor(phi / prime_factor)) % n == 1:
                is_primitive_root = True
                break
             
        if not is_primitive_root:
            primitive_roots.add(possible_root)
 
    return sorted(primitive_roots) 