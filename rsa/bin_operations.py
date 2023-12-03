def ascii_to_num(message):
    """
    Convert each character in the message to its ASCII value.
    """
    ascii_values = [ord(char) for char in message]
    return ascii_values

def num_to_ascii(ascii_values):
    """
    Convert a list of ASCII values back to a string message.
    """
    message = ''.join([chr(value) for value in ascii_values])
    return message

def num_to_hex(num_values):
    """
    Convert a list of numerical values to their hexadecimal representation.
    """
    hex_list = [hex(i) for i in num_values]
    return hex_list

def str_to_hexadecimal(text):
    """
    Convert a string to its hexadecimal representation.
    """
    hex = [format(ord(char), '02x') for char in text]
    return ''.join(hex)

def chunk_text(message):
    """
    Split a message into segments of three characters each.
    """
    segments = [message[i:i+3] for i in range(0, len(message), 3)]
    return segments