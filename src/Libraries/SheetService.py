# --//[ESSENTIAL IMPORTS]\\--
import csv
import os

# --//[CONTACT CLASS]\\--
class Contact:
    def __init__(self, _Company, _FirstName, _LastName, _Email, _Title, _LinkedIn, _Status):
        self.Company = _Company
        self.FirstName = _FirstName
        self.LastName = _LastName
        self.Email = _Email
        self.Title = _Title
        self.LinkedIn = _LinkedIn
        self.Status = _Status

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
    
    def __str__(self):
        return f"{self.FirstName} {self.LastName} ({self.Email}) - {self.Company} - {self.Title} - {self.LinkedIn} - {self.Status}"

def createContact(_Company, _FirstName, _LastName, _Email, _Title, _LinkedIn, _Status) -> Contact:
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
    return Contact(_Company, _FirstName, _LastName, _Email, _Title, _LinkedIn, _Status)

def convertCSVPathToContacts(filePath: str) -> list:
    """
    Converts a CSV file path to a list of Contact objects.
    
    :param filePath: The path to the CSV file.
    :return: A list of Contact objects.
    """
    contacts = []
    
    try:
        with open(filePath, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')        
            for i, row in enumerate(reader):
                try:                        
                    contact = createContact(
                        _Company=row.get('Company', '').strip(),
                        _FirstName=row.get('First Name', '').strip(),
                        _LastName=row.get('Last Name', '').strip(),
                        _Email=row.get('Email', '').strip(),
                        _Title=row.get('Title', '').strip(),
                        _LinkedIn=row.get('LinkedIn', '').strip(),
                        _Status=row.get('Status', '-').strip()
                    )
                    contacts.append(contact)
                except Exception as e:
                    print(f"Error processing row {i+1}: {e}")
                    continue
    except FileNotFoundError:
        print(f"File not found: {filePath}")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []
    
    return contacts

def appendContactsToCSV(filePath: str, contacts: list) -> None:
    """
    Appends a list of Contact objects to a CSV file.
    
    :param filePath: The path to the CSV file.
    :param contacts: A list of Contact objects to append.
    """
    
    # Check if file exists and has content
    file_exists = os.path.exists(filePath) and os.path.getsize(filePath) > 0
    
    with open(filePath, mode='a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Company', 'First Name', 'Last Name', 'Email', 'Title', 'LinkedIn', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        
        if not file_exists:
            writer.writeheader()

        for contact in contacts:
            writer.writerow({
                'Company': contact.Company,
                'First Name': contact.FirstName,
                'Last Name': contact.LastName,
                'Email': contact.Email,
                'Title': contact.Title,
                'LinkedIn': contact.LinkedIn,
                'Status': contact.Status
            })
    
    return None