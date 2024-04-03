import random
import string

def generate_password(lenght):

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(all_chars) for i in range(lenght))

    return password

password = generate_password(15)
print(password)