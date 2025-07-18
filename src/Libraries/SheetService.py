
# --//[ESSENTIAL IMPORTS]\\--
import csv

# --//[CONTACT CLASS]\\--
class Contact:
    def __init__(self, _Company, _FirstName, _LastName, _Email, _Title, _Status, _LinkedIn):
        self.Company = _Company
        self.FirstName = _FirstName
        self.LastName = _LastName
        self.Email = _Email
        self.Title = _Title
        self.Status = _Status
        self.LinkedIn = _LinkedIn

    def getStatus(self) -> tuple:
        # --//[EVALUATE STATUS]\\--
        if self.Status == "-":
            return (True, 0)
        elif self.Status == "1.":
            return (True, 1)
        elif self.Status == "2.":
            return (True, 2)
        
        # --//[CONTACT HAS ALREADY DECIDED ON OFFER]\\--
        elif self.Status == "Ja":
            return (False, None)
        elif self.Status == "Nein":
            return (False, None)
        
        raise ValueError("Invalid status value")
        return (False, None)
    

def createContact(_Company, _FirstName, _LastName, _Email, _Title, _Status) -> Contact:
    """
    Creates a new contact with the provided details.
    
    :param _Company: The company of the contact.
    :param _FirstName: The first name of the contact.
    :param _LastName: The last name of the contact.
    :param _Email: The email address of the contact.
    :param _Title: The title of the contact.
    :param _Status: The status of the contact.
    :return: A Contact object with the provided details.
    """
    return Contact(_Company, _FirstName, _LastName, _Email, _Title, _Status)

def convertCSVPathToContacts(filePath: str) -> list:
    """
    Converts a CSV file path to a list of Contact objects.
    
    :param filePath: The path to the CSV file.
    :return: A list of Contact objects.
    """
    
    contacts = []
    
    with open(filePath, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contact = createContact(
                _Company=row['Company'],
                _FirstName=row['First Name'],
                _LastName=row['Last Name'],
                _Email=row['Email'],
                _Title=row['Title'],
                _Status='-',
                _LinkedIn=row['Person Linkedin Url']
            )
            contacts.append(contact)
    
    return contacts

def appendContactsToCSV(filePath: str, contacts: list) -> None:
    """
    Appends a list of Contact objects to a CSV file.
    
    :param filePath: The path to the CSV file.
    :param contacts: A list of Contact objects to append.
    """
    
    with open(filePath, mode='a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Company', 'First Name', 'Last Name', 'Email', 'Title', 'Status', 'LinkedIn']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for contact in contacts:
            writer.writerow({
                'Company': contact.Company,
                'First Name': contact.FirstName,
                'Last Name': contact.LastName,
                'Email': contact.Email,
                'Title': contact.Title,
                'Status': contact.Status,
                'LinkedIn': contact.LinkedIn
            })
    
    return None