import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.sample(characters, 10))

print("Password:", password)