from log_search import search_log
import os
from dotenv import load_dotenv
from visual import cliVisual
from getpass import getpass
import time
from email_handler import create_event_handler
from watchdog.observers import Observer
from email_processor import process_all_emails
import threading 

load_dotenv(".env")

# my folder info 
root_dire = os.getenv("ROOT_DIRE") # my main dire
email_file_path = os.getenv("EMAIL_FOLDER") # folder where emails are kept
log_file_path = os.getenv("LOG_PATH") # path to log folder
email_archived_log_path = os.getenv("LOG_EMAIL_ARCHIVE") # path to email archived log file
email_processed_log_path = os.getenv("LOG_EMAIL_PROCESSED") # path to email processed log file
user_password = os.getenv("PASSWORD")


def authenticate_user():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return username, password

def display_options():
    print("Options: \n 1. Search Logs \n 2. Maybe Add Additional Feature Later \n 3. Exit")
    while True:
        try:
            options = int(input("Please enter the option you want: "))
            if options in [1, 2, 3]:
                return options
            else:
                print('Enter a valid number from the set of options')
        except ValueError:
            print("Please enter a number ")


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
                        search_string = input('Enter the string you want to search within the email log file: ')
                        search_log(email_archived_log_path, search_string)
                        time.sleep(5) # wait 5s before showing the options again
                elif (options == 2):
                    # print("test")
                    pass
                elif (options == 3):
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


# note to self: threading helps allow 2 things work at the same time
# issues: I need to remove the print statements in email_processing/handling
# this is so it does not intefer with the main