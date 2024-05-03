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

def append_code_to_file(code, filename='lune.cpp'):
    with open(filename, 'a') as file:
        file.write(code + '\n\n')  # Ajouter une ligne vide entre chaque ajout de code

def execute_git_commands():
    commands = [
        'git add .',
        'git commit -m "Le commit cool"',
        'git push --set-upstream origin main'
    ]
    for command in commands:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)

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

    for iteration in range(5):
        append_code_to_file(code)
        print(f"Code ajoute dans le fichier copy.py (iteration {iteration + 1})")

        execute_git_commands()
        print("Commandes Git exécutées.")

    print("Toutes les iterations sont terminees.")
