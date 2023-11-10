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


# a = calculate_gcd_inverse(3,7)
# print(a)