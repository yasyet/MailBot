import csv

def get_csv_delimiter(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        # Read a sample of the file to guess the delimiter
        sniffer = csv.Sniffer()
        try:
            dialect = sniffer.sniff(csvfile.read(1024))
            csvfile.seek(0) # Reset file pointer
            return dialect.delimiter
        except csv.Error:
            # Could not determine delimiter
            return None

# Replace with the path to your CSV file
csv_file = 'NexLead DecisionMakers - Test.csv'
delimiter = get_csv_delimiter(csv_file)

if delimiter:
    print(f"The detected delimiter is: '{delimiter}'")
else:
    print("Could not determine the delimiter.")