
# --//[ESSENTIAL IMPORTS]\\--
import os

# --//[TERMINAL FUNCTIONS]\\--
def clearTerminal() -> None:
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def header(title: str = "Terminal Service") -> None:
    """
    Prints a header for the terminal service.
    """
    print("========================================")
    print(f"          {title}              ")
    print("========================================")

def emptyLine() -> None:
    """
    Prints an empty line in the terminal.
    """
    print()

def chooseOption(prompt: str, options: list) -> str:
    """
    Prompts the user to choose an option from a list.
    
    :param prompt: The prompt message to display to the user.
    :param options: A list of options for the user to choose from.
    :return: The selected option.
    """
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Please select an option (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")