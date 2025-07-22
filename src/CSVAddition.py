# --//[LIBRARY IMPORTS]\\--
import Libraries.TerminalService as tservice
import Libraries.FileService as fservice
import Libraries.SheetService as sservice

# --//[CODE STARTS HERE]\\--
def main():
    # --//[SETUP TERMINAL]\\--
    tservice.clearTerminal()
    tservice.header("CSV ADDITION TERMINAL SERVICE")
    tservice.emptyLine()

    # --//[CHOOSING THE CSV FILES]\\--
    print("Please select the template CSV file:")
    first_csv_file = fservice.askOpenFile()                        # This .csv file is the template
    print(f"Selected template file: {first_csv_file}")
    tservice.emptyLine()

    print("Please select the target CSV file:")
    second_csv_file = fservice.askOpenFile()
    print(f"Selected target file: {second_csv_file}")
    tservice.emptyLine()

    # --//[CONVERTING CSV TO CONTACTS]\\--
    contacts = sservice.convertCSVPathToContacts(second_csv_file)  # This .csv file contains the contacts to be added
    print(f"Found {len(contacts)} contacts in the target file.")  # Fixed: was saying "template file"
    tservice.emptyLine()

    # Debug: Show first and last contact to verify
    if contacts:
        print(f"First contact: {contacts[0].FirstName} {contacts[0].LastName}")
        print(f"Last contact: {contacts[-1].FirstName} {contacts[-1].LastName}")
        tservice.emptyLine()

    # --//[APPENDING CONTACTS TO CSV FILE]\\--
    sservice.appendContactsToCSV(first_csv_file, contacts)
    print(f"Appended {len(contacts)} contacts to the template file: {first_csv_file}")
    tservice.emptyLine()

if __name__ == "__main__":
    main()