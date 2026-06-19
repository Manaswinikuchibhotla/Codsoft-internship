import random
import string

# Get password length from user
length = int(input("Enter the desired password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display password
print("Generated Password:", password)
