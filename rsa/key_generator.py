import numpy as np
from math_operations import calculate_gcd_inverse

first_primes = [2,3,5,7]

def generate_num(min_num=32768, max_num=65535, d_type=np.uint16):

    # Generate a random 16-bit unsigned integer
    par = True
    random = 0
    while par:
        random = np.random.randint(min_num, max_num, dtype=d_type)
        if random % 2 != 0:
            par = False

    return random


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

def generate_prime():
    primes_generated = False
    nums_lists = []
    
    while primes_generated == False:
        
        num_generated = generate_num()
        
        if is_prime(num_generated):
            nums_lists.append(num_generated)
        
        if len(nums_lists) == 2:
            primes_generated = True
            
    return nums_lists


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

def look_for_prime(num):
    
    square_root = np.emath.sqrt(num).astype(int)+1
    square_root_limiter = int(square_root/6)+1

    for i in range(5462, square_root_limiter): # 5461 = 32768 / 6
        possible_prime1=6*i-1
        possible_prime2=6*i+1
        
        gcd1 = calculate_gcd(possible_prime1, num)
        # gcd_m1 = math.gcd(possible_prime1, phi_n)
        # print("gcd: {} mgcd: {}".format(gcd1,gcd_m1))
        
        gcd2 = calculate_gcd(possible_prime2, num)
        # gcd_m2 = math.gcd(possible_prime2, phi_n)
        # print("gcd2: {} mgcd2: {}".format(gcd2,gcd_m2))
        
        if gcd1 == 1:
            return possible_prime1
        elif gcd2 == 1:
            return possible_prime2
        
    print("not found")
    exit(1)

def generate_public_key(phi_n):
    
    # e_generated = False
    
    # not_valid = {}
    e = look_for_prime(phi_n)
        
        # if e not in not_valid:
        #     gcd = calculate_gcd(e, phi_n)
        #     if gcd == 1:
        #         e_generated = True
        #     else:
        #         not_valid[e] = "Not valid"
    
    # print("aca")
    return e

def calculate_private_key(e, phi_n):
    
    gcd, d = calculate_gcd_inverse(e,phi_n)
    
    return d
    
def load_information(e,p,q):
    
    n,phi_n = calculate_n_phi(p,q)
    
    d = calculate_private_key(e, phi_n)
    
    return n,phi_n,d

def decouple_m(c, d, p, q):
    # print(c, d, p, q)
    temp_mp = c%p
    # print(temp_mp)
    temp_dp = d%(p-1)
    # print(temp_dp)
    mp = (temp_mp**temp_dp)%p
    # print(type(mp))
    # print(mp)
    
    q_inverse = calculate_private_key(q, p)
    
    temp_mq = c%q
    temp_dq = d%(q-1)
    mq = (temp_mq**temp_dq)%q
    # print(mq)
    
    p_inverse = calculate_private_key(p, q)
    
    n = p*q
    # print(n)
    m = ((mp * q * q_inverse) + (mq * p * p_inverse))%n
    
    return m

def ascii_to_num(message):
    
    ascii_values = [ord(char) for char in message]
    return ascii_values

def num_to_ascii(ascii_values):
    message = ''.join([chr(value) for value in ascii_values])
    return message

def num_to_hex(num_values):
    hex_list = [hex(i) for i in num_values]
    return hex_list

def str_to_hexadecimal(text):
    # Use list comprehension to get the hexadecimal representation of each character
    hex = [format(ord(char), '02x') for char in text]
    
    # Join the list of hexadecimal values into a single string
    return ''.join(hex)


def initialize():
    
    primes = generate_prime()
    print("p: {}, q: {}".format(primes[0], primes[1]))

    n, phi_n = calculate_n_phi(np.int64(primes[0]),np.int64(primes[1]))
    print("n: {}, phi_n: {}".format(n, phi_n))

    e = generate_public_key(phi_n)
    print("e: ",e)

    d = calculate_private_key(e, phi_n)
    print("d: ",d)

    n, phi_n, d = load_information(5,19,29)
    print("n: {}, phi_n: {}, d: {} ".format(n, phi_n, d))
    
    message = "Hello, World!"
    
    encrypted_message = encrypt(e, n , message)
    print(encrypted_message)


def chunk_text(message):
    segments = [message[i:i+3] for i in range(0, len(message), 3)]
    return segments

def multiply_mod_square(num, e, n):
    
    current_mod = 1
    
    for i in range(0,e):
        current_mod = (current_mod*num)%n
        # print(i, current_mod)
    
    return current_mod
    

def square_multiply(num, e, n):
    exp_bin = bin(e)
    print(exp_bin, len(exp_bin))
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

def encrypt(e, n, message):
    
    # value = multiply_mod_square(7,6,11)
    # print(value)
    
    message_segments = chunk_text(message)
    # print(message_segments)
    
    message_values = [int(str_to_hexadecimal(message_segments[i]),16) for i in range(len(message_segments))]
    print(message_values)
    
    encrypted_values = []
    for i in range(len(message_values)):
        c = multiply_mod_square(message_values[i],e,n)
        print(c)
        encrypted_values.append(c)
    
    #encrypted_message = num_to_ascii(encrypted_values)
    return encrypted_values   
    #return encrypted_message

def decipher(e, n, encrypted_values):
    p_prime, q_prime = prime_factor(n)
    print("p: {}, q: {}".format(p_prime, q_prime))

    n, phi_n = calculate_n_phi(p_prime, q_prime)
    print("n: {}, phi_n: {}".format(n, phi_n))

    d = calculate_private_key(e, phi_n)
    print("d: ",d)
    
    #encrypted_values = ascii_to_num(encrypted_message)
    message_values = []
    for i in encrypted_values:
        m = decouple_m(i, d, p_prime, q_prime)
        message_values.append(m)
    
    hex_values = num_to_hex(message_values)
    # print(message_values)
    print(hex_values)
        
    message = ''.join([bytes.fromhex(chunk[2:]).decode('utf-8') for chunk in hex_values])
    
    # message = "2"
    # for chunk in hex_values:
    #     print(bytes.fromhex(chunk[2:]).decode('utf-8'))
    
    return message

def sign(d, n, message):
    
    # value = multiply_mod_square(7,6,11)
    # print(value)
    
    message_segments = chunk_text(message)
    # print(message_segments)
    
    message_values = [int(str_to_hexadecimal(message_segments[i]),16) for i in range(len(message_segments))]
    print(message_values)
    
    signed_values = []
    for i in range(len(message_values)):
        c = square_multiply(message_values[i],d,n)
        print(c)
        signed_values.append(c)
    
    #encrypted_message = num_to_ascii(encrypted_values)
    return signed_values   
    #return encrypted_message

def verify(e, n, signed_values):
    
    message_values = []
    for i in range(len(signed_values)):
        c = square_multiply(signed_values[i],e,n)
        print(c)
        message_values.append(c)    
    
    
    hex_values = num_to_hex(message_values)
    # print(message_values)
    print(hex_values)
        
    message = ''.join([bytes.fromhex(chunk[2:]).decode('utf-8') for chunk in hex_values])
    
    # message = "2"
    # for chunk in hex_values:
    #     print(bytes.fromhex(chunk[2:]).decode('utf-8'))
    
    return message

    
if __name__=="__main__":
    
    # e = 672961497
    # n = 3497594377
    e = 32771
    n = 2814797023
    d =  1256909531
    # message = "Encryption by Tomas Navarro"
    message = "Tomas Navarro"
    print(chunk_text(message))
    
    hex_chunk = chunk_text(message)
    chunk = str_to_hexadecimal(hex_chunk[0])
    
    decimal = int(chunk, 16)
    print(decimal)
    
    # c = (decimal**e)%n
    # print(c) 
    
    # encrypted_values = encrypt(e,n,message)
    # print(encrypted_values)
    
    # encrypted_values = 	[1131917940, 1103261126, 1555222728, 1190175489, 1954013392, 226677880, 2530775063]
    
    # message = decipher(e,n,encrypted_values)
    # print(message)
    
    signed_values = sign(d, n, message)
    print(signed_values)
    
    message = verify(e,n,signed_values)
    print(message)
    
    # m = 72
    # c = (m**e)%n
    # print(c)
    # m = decipher(e,n,[c])
    # print(m)
    
    # d = 1256909531
    # p = 49123
    # q = 57301
    # m = decouple_m(c, d, p, q)
    # print(m)
    
    # d = 5
    # m = 11
    # n = 551
    
    # c = square_multiply(m,d,n)
    # print(c)