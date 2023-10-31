import random
import string
import subprocess

def generate_random_code():
    code_length = random.randint(50, 100)
    code = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=code_length))
    return code

def write_code_to_file(code, filename='copy.py'):
    with open(filename, 'w') as file:
        file.write(code)

def execute_shell_script():
    subprocess.run(['sh', 'script.sh'])

if __name__ == "__main__":
    for iteration in range(6):
        random_code = generate_random_code()
        write_code_to_file(random_code)
        print(f"Code généré et écrit dans le fichier copy.py (itération {iteration + 1})")
        
        execute_shell_script()
        print("Commande 'sh script.sh' exécutée.")

    print("Toutes les itérations sont terminées.")
