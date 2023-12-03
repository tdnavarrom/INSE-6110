import numpy as np


def calculate_gcd_inverse(lnum, mnum):
    
    #print("lnum: {}, mnum: {}".format(lnum, mnum))
    
    a = lnum
    b = mnum
    temp = a
    
    sum_before = 0
    sum_current = 1
    num1 = np.int64(b / a)
    
    while temp:
        num1 = np.int64(b / a)
        temp = np.int64(b % a)
        
        #print("a: {}, b: {}, temp: {}".format(a,b,temp))
        if temp != 0:
            b = a
            a = temp
            
            temp_sum = sum_current
            sum_current = sum_before - num1*sum_current
            sum_before = temp_sum

    gcd = a
    
    if sum_current < 0:
        sum_current = sum_current + mnum
        
    sum_current = int(sum_current)
    
    return gcd, sum_current

def is_prime(num):

    square_root = np.emath.sqrt(num).astype(int)+1
    square_root_limiter = int(square_root/6)+1

    if num in first_primes:
        return True
    
    if (num % 2 == 0 or num % 3 == 0):
        return False
    else:
        for i in range(1, square_root_limiter):
            possible_prime1=6*i-1
            possible_prime2=6*i+1
            if num % possible_prime1 == 0 or num % possible_prime2 == 0:
                return False

    return True

def prime_factor(num):
    
    square_root = np.emath.sqrt(num).astype(int)+1
    square_root_limiter = int(square_root/6)+1
    primes = []

    if (num % 2 == 0):
        primes.append(2)
        primes.append(int(num/2))
    if(num % 3 == 0):
        primes.append(3)
        primes.append(int(num/3))
    
    for i in range(1, square_root_limiter):
        possible_prime1=6*i-1
        possible_prime2=6*i+1
        if num % possible_prime1 == 0:
            primes.append(possible_prime1)
            primes.append(int(num/possible_prime1))
        if num % possible_prime2 == 0:
            primes.append(possible_prime2)
            primes.append(int(num/possible_prime2))

    return primes

def calculate_n_phi(p,q):
    
    n = p*q
    phi_n = (p-1)*(q-1)
    
    return n,phi_n

def calculate_gcd(lnum, mnum):
    
    #print("lnum: {}, mnum: {}".format(lnum, mnum))
    
    a = lnum
    b = mnum
    temp = a
    
    while temp:
        temp = np.int64(b % a)
        
        #print("a: {}, b: {}, temp: {}".format(a,b,temp))
        if temp != 0:
            b = a
            a = temp

    gcd = a
    
    return gcd

def multiply_mod_square(num, e, n):
    
    current_mod = 1
    
    for i in range(0,e):
        current_mod = (current_mod*num)%n
        # print(i, current_mod)
    
    return current_mod

def square_multiply(num, e, n):
    exp_bin = bin(e)
    # print(exp_bin, len(exp_bin))
    current_mod = 1
    current_value = num
    
    for i in range(len(exp_bin)-1, 1, -1):
        # print("i:", i)
        if(exp_bin[i]=='1'):
            current_mod = (current_mod * current_value)%n
            # print("i:", i)
            # print("current_mod: ", current_mod)
        
        current_value = (current_value**2)%n
        
    return current_mod
# a = calculate_gcd_inverse(3,7)
# print(a)