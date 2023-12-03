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

def chunk_text(message):
    segments = [message[i:i+3] for i in range(0, len(message), 3)]
    return segments