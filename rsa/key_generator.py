import numpy as np
from math_operations import *
from bin_operations import *

def generate_num(min_num=32768, max_num=65535, d_type=np.uint16):

    """
        Generate a random 16-bit unsigned integer
    """
    
    par = True
    random = 0
    while par:
        random = np.random.randint(min_num, max_num, dtype=d_type)
        if random % 2 != 0:
            par = False

    return random


def generate_prime():
    """
    Generate two prime numbers and return them as a list.
    """
    primes_generated = False
    nums_lists = []
    
    while primes_generated == False:
        
        num_generated = generate_num()
        
        if is_prime(num_generated):
            nums_lists.append(num_generated)
        
        if len(nums_lists) == 2:
            primes_generated = True
            
    return nums_lists


def look_for_prime(num):
    """
    Look for a prime number around the given number.
    """
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
    """
    Generate a public key using a prime number function.
    """
    e = look_for_prime(phi_n)
    return e

def calculate_private_key(e, phi_n):
    """
    Calculate the private key using the modular multiplicative inverse.
    """
    gcd, d = calculate_gcd_inverse(e,phi_n)
    
    return d
    
def load_information(e,p,q):
    """
    Load information including n, phi_n, and private key d.
    """
    n,phi_n = calculate_n_phi(p,q)
    
    d = calculate_private_key(e, phi_n)
    
    return n,phi_n,d

def decouple_m(c, d, p, q):
    """
    Decouple the encrypted message using the Chinese Remainder Theorem.
    """
    temp_mp = c%p
    temp_dp = d%(p-1)
    mp = (temp_mp**temp_dp)%p
    
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

def encrypt(e, n, message):
    """
    Encrypt a message using a public key and return the encrypted values.
    """
    message_segments = chunk_text(message)
    # print(message_segments)
    
    message_values = [int(str_to_hexadecimal(message_segments[i]),16) for i in range(len(message_segments))]
    print("Message Values-----------------")
    print(message_values)
    
    encrypted_values = []
    for i in range(len(message_values)):
        c = multiply_mod_square(message_values[i],e,n)
        # print(c)
        encrypted_values.append(c)
    
    #encrypted_message = num_to_ascii(encrypted_values)
    return encrypted_values   
    #return encrypted_message

def decipher(d, n, p,q, encrypted_values):
    
    """
    Decipher an encrypted message using the private key and prime factors.
    """
    
    # p_prime, q_prime = prime_factor(n)
    # print("p: {}, q: {}".format(p_prime, q_prime))

    # n, phi_n = calculate_n_phi(p, q)
    # print("n: {}, phi_n: {}".format(n, phi_n))

    # d = calculate_private_key(e, phi_n)
    # print("d: ",d)
    
    message_values = []
    for i in encrypted_values:
        m = decouple_m(i, d, p, q)
        message_values.append(m)
    
    hex_values = num_to_hex(message_values)
    print(hex_values)
        
    message = ''.join([bytes.fromhex(chunk[2:]).decode('utf-8') for chunk in hex_values])
    
    
    return message

def sign(d, n, message):
    """
    Sign a message using the private key and return the signed values.
    """
    
    message_segments = chunk_text(message)
    
    message_values = [int(str_to_hexadecimal(message_segments[i]),16) for i in range(len(message_segments))]
    print(message_values)
    
    signed_values = []
    for i in range(len(message_values)):
        c = square_multiply(message_values[i],d,n)
        # print(c)
        signed_values.append(c)
    
    return signed_values   

def verify(e, n, signed_values):
    """
    Verify a message's signature using the public key and return the message.
    """
    
    message_values = []
    for i in range(len(signed_values)):
        c = square_multiply(signed_values[i],e,n)
        # print(c)
        message_values.append(c)    
    
    
    hex_values = num_to_hex(message_values)
    print(hex_values)
        
    message = ''.join([bytes.fromhex(chunk[2:]).decode('utf-8') for chunk in hex_values])
    
    
    return message

def initialize():
    """
    Initialize the encryption system and print key information.
    """
    
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
    
    message = "Encryption by Tomas Navarro"
    
    encrypted_message = encrypt(e, n , message)
    print(encrypted_message)


def test():
    """
    Test encryption, decryption, and signing of a message.
    """
    e = 32771
    p = 49123
    q = 57301
    n = 2814797023
    d =  1256909531
    message = "Encryption by Tomas Navarro"
    
    # chunk = str_to_hexadecimal(hex_chunk[0])
    # decimal = int(chunk, 16)
    # print(decimal)
    
    encrypted_values = encrypt(e,n,message)
    print("Encrypted Values-----------------")
    print(encrypted_values)
    
    
    print("Partner Message-----------------")
    encrypted_values = 	[1131917940, 1103261126, 1555222728, 1190175489, 1954013392, 226677880, 2530775063]
    message_partner = decipher(d,n,p,q ,encrypted_values)
    print(message_partner)
    
    print("Signature Message-----------------")
    message_sign =  "Tomas Navarro"
    
    # print(chunk_text(message_sign))
    # hex_chunk = chunk_text(message_sign)
    
    signed_values = sign(d, n, message_sign)
    print(signed_values)


def test_signature():
    """
    Test signature verification using predefined parameters.
    """
    
    e = 672961497
    n = 3497594377

    signed_values = [2722866973, 594348302, 3308561343, 1549806427, 3172487038, 518921097]
    
    print("Partner Signature Message---------------")
    message = verify(e,n,signed_values)
    print(message)
    

if __name__=="__main__":
    """
    Entry point for the script, initializing and testing the encryption system.
    """
    
    initialize()
    test()
    test_signature()