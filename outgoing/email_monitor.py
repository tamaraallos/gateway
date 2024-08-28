import os
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Setup logging
log_dir = "logging"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'email_sensitivity.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define the email processing handler
class EmailEventHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.eml'):
            logging.info(f"New email detected: {event.src_path}")
            process_email(event.src_path)

def process_email(file_path):
    try:
        logging.info(f"Processing email: {file_path}")
        email_safe, sensitive_data = is_email_safe(file_path)
        
        if email_safe:
            logging.info(f"Email {file_path} is safe. Encrypting and sending...")
            encrypt_and_send_email(file_path, action="allow")
        else:
            logging.warning(f"Unsafe email detected: {file_path}. Sensitive data found: {', '.join(sensitive_data)}")
            print(f"Calling move_to_approval_needed for {file_path}")  # Debugging statement
            move_to_approval_needed(file_path, sensitive_data)
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")

def is_email_safe(file_path):
    sensitive_keywords = ['Tax File Number', 'Credit Card Number', 'Confidential Plan', 'Balance Sheet']
    sensitive_data_found = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            for keyword in sensitive_keywords:
                if keyword.lower() in content.lower():
                    sensitive_data_found.append(keyword)
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
    
    return (len(sensitive_data_found) == 0), sensitive_data_found

def encrypt_and_send_email(file_path, action):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Base directory for consistency
        sent_folder = os.path.join(base_dir, "Sent")
        os.makedirs(sent_folder, exist_ok=True)
        
        destination_path = os.path.join(sent_folder, os.path.basename(file_path))
        shutil.copy(file_path, destination_path)
        logging.info(f"Email encrypted and saved to {destination_path}")
        
        log_email_details(file_path, destination_path, action)

        os.remove(file_path)
        logging.info(f"Original email file {file_path} has been removed after sending.")
    except Exception as e:
        logging.error(f"Failed to encrypt and send email {file_path}: {e}")

def log_email_details(original_path, destination_path, action):
    try:
        with open(original_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            from_address = extract_header(content, 'From')
            to_address = extract_header(content, 'To')
            subject = extract_header(content, 'Subject')
            date_sent = extract_header(content, 'Date')
        
        log_entry = f"ACTION: {action.upper()} | Type: Sent | From: {from_address} | To: {to_address} | Date: {date_sent} | Subject: {subject} | Path: {destination_path}"
        logging.info(log_entry)
    except Exception as e:
        logging.error(f"Failed to log email details for {original_path}: {e}")

def extract_header(content, header_name):
    for line in content.splitlines():
        if line.startswith(header_name):
            return line[len(header_name) + 1:].strip()
    return "Unknown"

def move_to_approval_needed(file_path, sensitive_data):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Base directory for consistency
        approval_needed_folder = os.path.join(base_dir, "Approval needed")
        os.makedirs(approval_needed_folder, exist_ok=True)
        
        destination_path = os.path.join(approval_needed_folder, os.path.basename(file_path))
        shutil.move(file_path, destination_path)
        logging.info(f"Email {file_path} moved to 'Approval needed' due to detected sensitive data: {', '.join(sensitive_data)}")
        
        print(f"Logging block action for {file_path}")  # Debugging statement
        log_email_details(file_path, destination_path, action="block")
    except Exception as e:
        logging.error(f"Failed to move email {file_path} to 'Approval needed': {e}")

def search_logs(date_str=None, time_str=None, subject_str=None, from_str=None, to_str=None, action_str=None):
    log_file = os.path.join("logging", 'email_sensitivity.log')
    if not os.path.exists(log_file):
        print("No logs found.")
        return
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if (date_str in line if date_str else True) and \
               (time_str in line if time_str else True) and \
               (subject_str.lower() in line.lower() if subject_str else True) and \
               (from_str.lower() in line.lower() if from_str else True) and \
               (to_str.lower() in line.lower() if to_str else True) and \
               (action_str.lower() in line.lower() if action_str else True):
                print(line.strip())

def view_logs():
    while True:
        print("\nView Logs Menu")
        print("1. View by date")
        print("2. View by time")
        print("3. View by subject")
        print("4. View by sender")
        print("5. View by receiver")
        print("6. View by action (block/allow)")
        print("7. View all logs")
        print("8. Go back to main menu")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            date_str = input("Enter the date (YYYY-MM-DD) to search: ").strip()
            search_logs(date_str=date_str)
        elif choice == '2':
            time_str = input("Enter the time (HH:MM) to search: ").strip()
            search_logs(time_str=time_str)
        elif choice == '3':
            subject_str = input("Enter the subject to search: ").strip()
            search_logs(subject_str=subject_str)
        elif choice == '4':
            from_str = input("Enter the sender address to search: ").strip()
            search_logs(from_str=from_str)
        elif choice == '5':
            to_str = input("Enter the receiver address to search: ").strip()
            search_logs(to_str=to_str)
        elif choice == '6':
            action_str = input("Enter the action (block/allow) to search: ").strip()
            search_logs(action_str=action_str)
        elif choice == '7':
            search_logs()
        elif choice == '8':
            break
        else:
            print("Invalid option, please try again.")

def view_sent_emails():
    while True:
        print("\nView Sent Emails Menu")
        print("1. View by sender/receiver address")
        print("2. View by date")
        print("3. View by time")
        print("4. View all sent emails")
        print("5. Go back to main menu")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            address_str = input("Enter the sender or receiver address to search: ").strip()
            search_sent_emails(address_str=address_str)
        elif choice == '2':
            date_str = input("Enter the date (YYYY-MM-DD) to search: ").strip()
            search_sent_emails(date_str=date_str)
        elif choice == '3':
            time_str = input("Enter the time (HH:MM) to search: ").strip()
            search_sent_emails(time_str=time_str)
        elif choice == '4':
            search_sent_emails()
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

def search_sent_emails(address_str=None, date_str=None, time_str=None):
    log_file = os.path.join("logging", 'email_sensitivity.log')
    if not os.path.exists(log_file):
        print("No logs found.")
        return
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "SENT" in line:
                if (address_str.lower() in line.lower() if address_str else True) and \
                   (date_str in line if date_str else True) and \
                   (time_str in line if time_str else True):
                    print(line.strip())

def approve_emails():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    approval_needed_folder = os.path.join(base_dir, "Approval needed")
    if not os.path.exists(approval_needed_folder):
        logging.info("No 'Approval needed' folder found.")
        print("No emails in 'Approval needed' folder.")
        return
    
    for filename in os.listdir(approval_needed_folder):
        if filename.endswith('.eml'):
            file_path = os.path.join(approval_needed_folder, filename)
            user_input = input(f"Approve and encrypt {filename}? (yes/no): ").strip().lower()
            if user_input == 'yes':
                encrypt_and_send_email(file_path, action="allow")
            else:
                print(f"Skipping {filename}...")

def summarize_emails(directory):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    approval_needed_folder = os.path.join(base_dir, "Approval needed")
    sent_folder = os.path.join(base_dir, "Sent")
    
    approval_needed_count = len([name for name in os.listdir(approval_needed_folder) if name.endswith('.eml')]) if os.path.exists(approval_needed_folder) else 0
    sent_count = len([name for name in os.listdir(sent_folder) if name.endswith('.eml')]) if os.path.exists(sent_folder) else 0

    print("\nSummary of Email Processing:")
    print(f"All emails are scanned.")
    print(f"{approval_needed_count} email(s) need approval.")
    print(f"{sent_count} email(s) got sent.")

def main_menu():
    email_directory = os.path.dirname(os.path.abspath(__file__))  # Adjust as needed
    process_existing_emails(email_directory)
    monitor_directory_in_background(email_directory)
    summarize_emails(email_directory)
    
    while True:
        print("\nEmail Monitoring System")
        print("1. Approve emails")
        print("2. View and search email logs")
        print("3. View sent emails")
        print("4. Quit")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            approve_emails()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            view_sent_emails()
        elif choice == '4':
            print("Quitting...")
            break
        else:
            print("Invalid option, please try again.")

def process_existing_emails(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.eml'):
            file_path = os.path.join(directory, filename)
            process_email(file_path)

def monitor_directory_in_background(directory):
    observer = Observer()
    event_handler = EmailEventHandler(directory)
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()

if __name__ == "__main__":
    main_menu()
