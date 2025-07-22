
# --//[ESSENTIAL IMPORTS]\\--
pass

# --//[LIBRARY IMPORTS]\\--
import Libraries.TerminalService as tservice
import Libraries.FileService as fservice
import Libraries.SheetService as sservice

# --//[CODE STARTS HERE]\\--
def main():
    # --//[SETUP TERMINAL]\\--
    tservice.clearTerminal()
    tservice.header("MAILBOT TERMINAL SERVICE")
    tservice.emptyLine()

    # --//[CHOOSING PROGRAM OPTIONS]\\--
    program_options = [
        "Send 1. Mail",
        "Send 2. Mail ",
        "Send 3. Mail",
        "Review Answers"
    ]

    program_option_selected = tservice.chooseOption(
        "Please select a program option:",
        program_options
    )

    # --//[CHOOSING A CSV FILE]\\--
    csv_file_path = fservice.askOpenFile()

    # --//[CONVERTING CSV TO CONTACTS]\\--
    contacts = sservice.convertCSVPathToContacts(csv_file_path)
    tservice.emptyLine()
    print(f"Found {len(contacts)} contacts in the CSV file: {csv_file_path}")
    tservice.emptyLine()
    print("First 5 contacts:")
    for contact in contacts[:5]:
        print(f" - {contact}")

if __name__ == "__main__":
    main()