import subprocess

def fibonacci(n):
    if n <= 0:
        return "Entrez un entier positif pour calculer la suite de Fibonacci."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def write_code_to_file(code, filename='copy.py'):
    with open(filename, 'w') as file:
        file.write(code)

def execute_shell_script():
    subprocess.run(['sh', 'script.sh'])

if __name__ == "__main__":
    code = """def fibonacci(n):
    if n <= 0:
        return "Entrez un entier positif pour calculer la suite de Fibonacci."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence"""

    for iteration in range(6):
        write_code_to_file(code)
        print(f"Code écrit dans le fichier copy.py (itération {iteration + 1})")

        execute_shell_script()
        print("Commande 'sh script.sh' exécutée.")

    print("Toutes les itérations sont terminées.")
