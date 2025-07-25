
# --//[ESSENTIAL IMPORTS]\\--
pass

# --//[LIBRARY IMPORTS]\\--
import Libraries.TerminalService as tservice
import Libraries.FileService as fservice
import Libraries.SheetService as sservice
import Libraries.MailService as mservice
import Libraries.AIService as aiservice

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

    # --//[CHOOSING A PROGRAM OPTION]\\--
    program_option_selected = tservice.chooseOption(
        "Please select a program option:",
        program_options
    )
    # --//[CONVERTING PROGRAM OPTION TO INDEX]\\--
    program_option_selected = program_options.index(program_option_selected)

    # --//[CHOOSING A CSV FILE]\\--
    tservice.emptyLine()
    print("Please select a CSV file containing contacts.")
    csv_file_path = fservice.askOpenFile()

    # --//[CONVERTING CSV TO CONTACTS]\\--
    contacts = sservice.convertCSVPathToContacts(csv_file_path)
    
    tservice.emptyLine()
    tservice.header("CONTACTS LOADED")
    tservice.emptyLine()

    print(f"Found {len(contacts)} contacts in the CSV file: {csv_file_path}")
    print(f"First contact: {contacts[0].name()}")
    tservice.emptyLine()

    # --//[PROCESSING CONTACTS BASED ON SELECTED OPTION]\\--
    if program_option_selected <= 2:
        # --//[SETUP AI AGENT]\\--
        ai_agent = aiservice.AIAgent(
            _model="TODO", #TODO: Replace with actual model name
            _temperature=1.2,
            _max_tokens=80
        )
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that generates personalized email content."
            },
            {
                "role": "user",
                "content": "Generate a personalized email for the contact based on their profile."
            }
        ] #TODO: Replace with actual messages

        # --//[SETUP MAIL SERVICE]\\--
        mail_service = mservice.MailService()

        changed_contacts = mail_service.send_email_to_contacts(contacts, program_option_selected, ai_agent, messages) # Sends emails based on the selected option

    # --//[OVERWRITE CSV FILE WITH CHANGED CONTACTS]\\--
    if changed_contacts:
        for contact in changed_contacts:
            print(f"Contact: {contact.name()} - Status: {contact.getStatus()[1]}")
        sservice.overwriteCSV(csv_file_path, changed_contacts)
        tservice.emptyLine()
        tservice.header("CHANGED CONTACTS SAVED")
        tservice.emptyLine()

if __name__ == "__main__":
    main()