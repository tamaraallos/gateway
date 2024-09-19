from src.log_search import search_log, search_by_field
import os
from dotenv import load_dotenv
from visual import cliVisual
from getpass import getpass
import time
from src.email_handler import create_event_handler
from watchdog.observers import Observer
from src.email_processor import process_all_emails, print_log_file
import threading 

load_dotenv(".env")

# my folder info 
root_dire = os.getenv("ROOT_DIRE") # my main dire
email_file_path = os.getenv("EMAIL_FOLDER") # folder where emails are kept
log_file_path = os.getenv("LOG_PATH") # path to log folder
email_archived_log_path = os.getenv("LOG_EMAIL_ARCHIVE") # path to email archived log file
email_processed_log_path = os.getenv("LOG_EMAIL_PROCESSED") # path to email processed log file
user_password = os.getenv("PASSWORD")


# checks users password
def authenticate_user():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return username, password

# displays options within CLI
def display_options():
    print("\n Options: \n 1. View Email Logs \n 2. Search Email Logs \n 3. View Processed Email's by Name \n 4. Exit")
    while True:
        try:
            options = int(input("Please enter the option you want: "))
            if options in [1, 2, 3, 4]:
                return options
            else:
                print('Enter a valid number from the set of options')
        except ValueError:
            print("Please enter a number ")

# displays search by log options 
def display_search_log_by():
    print("\n Search By: \n 1.String \n 2.Date \n 3.Subject \n 4.Sender \n 5.Reciver \n 6.Type \n 7.Action \n 8.Back to menu")
    while True:
        try:
            search_by = int(input("Please enter the option you want: "))
            if search_by in [1, 2, 3, 4, 5, 6, 7, 8]:
                return search_by
            else:
                print('Enter a valid number from the set of options')
        except ValueError:
            print("Please enter a number ")


# menu options for searching by specific type
def search_log_menu():
     while True:
        search_by = display_search_log_by()
        if (search_by == 1):
            search_string = input('Enter the string you want to search within the email log file: ')
            search_log(email_archived_log_path, search_string)
            time.sleep(5)
        elif (search_by == 2):
            value = input('Enter the date you want to search for (e.g., "Wed, 10 Jul 2024 12:39:34 -0000"): ')
            search_by_field(email_archived_log_path, 'date', value)
        elif (search_by == 3):
            value = input('Enter a keyword to search in the email subject: ')
            search_by_field(email_archived_log_path, 'subject', value)
        elif (search_by == 4):
            value = input("Enter the sender's email address to search for: ") 
            search_by_field(email_archived_log_path, 'from', value)
        elif (search_by == 5):
            value = input("Enter the reciever's email address to search for: ") 
            search_by_field(email_archived_log_path, 'to', value)
        elif (search_by == 6):
            value = input('Enter the type of email to search for (e.g., phishing, spam, DLP Violation): ') # later add more
            search_by_field(email_archived_log_path, 'type', value)
        elif (search_by == 7):
            value = input('Enter the action status you want to search for (e.g., blocked, allowed): ') 
            search_by_field(email_archived_log_path, 'action status', value)
        elif (search_by == 8):
            print('Returning to the menu...')
            time.sleep(0.2)
            break
            
# this monitors the folder initially - it runs once and only once
def initial_email_monitor():
    print("Processing the existing emails in the dire...")
    process_all_emails(email_file_path, email_archived_log_path, email_processed_log_path)

# monitors any new emaiils within the folder
def monitor_new_emails():
    print("Monitoring new emails...")
    event_handler = create_event_handler(email_file_path, email_archived_log_path, email_processed_log_path)
    observer = Observer()
    observer.schedule(event_handler, path=email_file_path, recursive=False)
    observer.start()
    print("Monitoring started. Waiting for new emails...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

# starts a thread for monitoring new emails
def start_monitoring_thread():
    monitoring_thread = threading.Thread(target=monitor_new_emails)
    monitoring_thread.daemon = True
    monitoring_thread.start()

def main_loop():
    while True:
        print(cliVisual.name_of_client, cliVisual.img)
        username, password = authenticate_user()

        if password == user_password:
            print('\nWelcome to Bad Security Inc Email Terminal, user:', username, '\n')
            while True:
                options = display_options()
                if (options == 1):
                    print("\n All emails stored in the log file: \n")
                    print_log_file(email_archived_log_path)
                elif (options == 2):
                    search_log_menu()
                    time.sleep(5)
                elif (options == 3):
                    print("\n Email names that have been processed: \n")
                    print_log_file(email_processed_log_path )
                elif (options == 4):
                    print('Exiting...')
                    time.sleep(0.5)
                    break
        else:
            print("Access Denied!")
            time.sleep(1.5) 
        
if __name__ == "__main__":
    initial_email_monitor()
    start_monitoring_thread()
    main_loop()
