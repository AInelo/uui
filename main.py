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

def append_code_to_file(code, filename='main.cpp'):
    with open(filename, 'a') as file:
        file.write(code + '\n\n')  # Ajouter une ligne vide entre chaque ajout de code

def execute_shell_script():
    subprocess.run(['sh', 'script.sh'])

if __name__ == "__main__":
    code = """int main()
{
    std::string input;

    std::cout << "Enter a string: ";
    std::cin >> input;

    if (isPalindrome(input))
    {
        std::cout << input << " is a palindrome.";
    }
    else
    {
        std::cout << input << " is not a palindrome.";
    }

    return 0;
}"""

    for iteration in range(20):
        append_code_to_file(code)
        print(f"Code ajouté dans le fichier copy.py (itération {iteration + 1})")

        execute_shell_script()
        print("Commande 'sh script.sh' exécutée.")

    print("Toutes les itérations sont terminées.")
