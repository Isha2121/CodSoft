# A Python Program for Designing a Password Generator...

import random
import string

def generate_password(length=6):
    # Define the character set for the password

    characters = string.ascii_letters + string.digits + string.punctuation 
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Set the desired new password length
password_length = 6

# Generate and print the new password
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)

exit()