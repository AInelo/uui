import random
import string

def generate_random_code():
    code_length = random.randint(50, 100)
    code = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=code_length))
    return code

def write_code_to_file(code, filename='copy.py'):
    with open(filename, 'w') as file:
        file.write(code)

if __name__ == "__main__":
    random_code = generate_random_code()
    write_code_to_file(random_code)
    print(f"Code généré et écrit dans le fichier copy.py")
