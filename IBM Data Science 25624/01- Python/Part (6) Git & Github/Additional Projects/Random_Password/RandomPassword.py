
import random

def create_password():
    upper_len = num_len = symbol_len = 2
    lower_len = 16 - upper_len - num_len - symbol_len
    
    password = []
    for i in range(upper_len):
        password += chr(random.randint(65, 90))

    for i in range(num_len):
        password += chr(random.randint(48, 57))

    for i in range(symbol_len):
        password += random.choice(['@', '#', '$', '^', '&', '*'])

    for i in range(lower_len-1):
        password += chr(random.randint(97, 122))
    
    random.shuffle(password)  # Shuffle the characters
    first_chr = chr(random.randint(97, 122))

    return first_chr +''.join(password)

if __name__ == '__main__':
    print(create_password())

