import csv
import spacy
import random
from prettytable import PrettyTable

nlp = spacy.load("en_core_web_sm")

# List of emojis for random selection
emojis = ["😀", "😎", "🥳", "📞", "📧", "📌", "👍", "❤️", "🌟", "🌈"]

class PhoneBook:
    def __init__(self):
        self.contacts = {}
        self.logged_in = False

    def login(self):
        """Log in to the phone book application."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Basic username and password check (you can improve this)
        if username == "admin" and password == "password":
            print("Login successful.")
            self.logged_in = True
        else:
            print("Login failed. Please try again.")

    def add_contact(self, name, phone_number, email, notes=""):
        """Add a contact to the phone book."""
        if not self.logged_in:
            print("You need to log in to add contacts.")
            return

        # Convert the contact name to uppercase
        name = name.upper()

        if name not in self.contacts:
            # Automatically add "+91" as the default country code
            if not phone_number.startswith("+"):
                phone_number = "+91" + phone_number

            # Generate a random emoji
            random_emoji = random.choice(emojis)
            
            self.contacts[name] = {
                'phone_number': phone_number,
                'email': email,
                'notes': notes,
                'emoji': random_emoji
            }
        else:
            print(f"Contact '{name}' already exists in the phone book.")

    # Other methods (remove_contact, search_contact, advanced_search) as before

    def display_contacts(self):
        """Display all contacts in the phone book using PrettyTable."""
        if not self.contacts:
            print("Phone book is empty.")
        else:
            table = PrettyTable()
            table.field_names = ["Name", "Phone Number", "Email", "Notes"]
            table.align["Name"] = "l"  # Left-align the Name column
            table.align["Phone Number"] = "l"  # Left-align the Phone Number column
            table.align["Email"] = "l"  # Left-align the Email column
            table.align["Notes"] = "l"  # Left-align the Notes column
            for name, contact in self.contacts.items():
                formatted_name = f"{contact['emoji']} {name}"
                table.add_row([formatted_name, contact['phone_number'], contact['email'], contact['notes']])
            print(table)

    def generate_report(self, report_type):
        """Generate a report and export it to CSV or text file."""
        if not self.contacts:
            print("Phone book is empty. Nothing to export.")
            return

        if report_type == "1":
            # Export to CSV
            filename = input("Enter the CSV file name: ")
            with open(filename, mode='w', newline='') as csv_file:
                fieldnames = ['Name', 'Phone Number', 'Email', 'Notes']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for name, contact in self.contacts.items():
                    writer.writerow({
                        'Name': name,
                        'Phone Number': contact['phone_number'],
                        'Email': contact['email'],
                        'Notes': contact['notes']
                    })
            print(f"Contacts exported to '{filename}'.")
        elif report_type == "2":
            # Export to Text File
            filename = input("Enter the text file name: ")
            with open(filename, 'w') as text_file:
                text_file.write("Contacts in Phone Book:\n")
                for name, contact in self.contacts.items():
                    formatted_name = f"{contact['emoji']} {name}"
                    text_file.write(f"Name: {formatted_name}\n")
                    text_file.write(f"Phone Number: {contact['phone_number']}\n")
                    text_file.write(f"Email: {contact['email']}\n")
                    text_file.write(f"Notes: {contact['notes']}\n")
                    text_file.write("-" * 20 + "\n")
            print(f"Contacts exported to '{filename}'.")
        else:
            print("Invalid report type. Please select 1 (CSV) or 2 (Text).")

def display_menu():
    """Display the admin menu."""
    print("\nAdmin Menu:")
    print("1. Display Contacts 📋")
    print("2. Add/Edit Contacts ✏️")
    print("3. Generate Report 📄")
    print("4. Exit 🚪")

# Create a phone book
phone_book = PhoneBook()

# Log in to the phone book application
phone_book.login()

while phone_book.logged_in:
    display_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        # Display Contacts
        phone_book.display_contacts()
    elif choice == "2":
        # Add/Edit Contacts
        print("\nLogged in. You can now add/edit contacts.")
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number (without country code, e.g., 9876543210): ")
        email = input("Enter email: ")
        notes = input("Enter notes (optional): ")

        phone_book.add_contact(name, phone_number, email, notes)
    elif choice == "3":
        # Generate Report
        report_type = input("Select report type (1: CSV, 2: Text): ")
        phone_book.generate_report(report_type)
    elif choice == "4":
        # Exit
        print("Exiting admin mode. 🚀")
        phone_book.logged_in = False
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
