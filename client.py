import math
import random
from fractions import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Modular multiplicative inverses
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#Primality test
def prime(n):
    if n<=3:
        return n>1
    elif n%2 ==0 | n%3==0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 | n%(i + 2) == 0:
            return False
        i = i + 6
    return True

#Carmichael Function
def carmichael(n):
    coprimes = [x for x in range(1, n) if gcd(x, n) == 1]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k

def keygen():
    p = 0
    q = 0
    while not prime(p): 
        p = random.SystemRandom().randint(1, 10000)
    while not prime(q) or p==q:
        q = random.SystemRandom().randint(1, 10000)
    carmich = carmichael(p*q)
    
    public_key = random.SystemRandom().choice([x for x in range(1,carmich) if gcd(x,carmich) == 1])
    private_key = modinv(public_key,carmich)
    
    #returns [modulus,public_key_exponent],[modulus, private_key_exponent]
    return [[p*q,public_key],[p*q,private_key]]
