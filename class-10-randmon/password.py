import random
import string

# Define characters to use in password
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = string.punctuation

# Combine all characters
all_chars = uppercase + lowercase + digits + special

# Password length
length = 10

# Generate random password
password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Generated Password:", password)