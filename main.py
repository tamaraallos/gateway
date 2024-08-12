from email_processor import process_all_emails
from log_search import search_log
import os
from dotenv import load_dotenv
load_dotenv(".env")

# Mine Tamara's folder info 
root_dire = os.getenv("ROOT_DIRE") # my main dire
email_file_path = os.getenv("EMAIL_FOLDER") # folder where emails are kept
log_file_path = os.getenv("LOG_PATH") # path to log folder
email_archived_log_path = os.getenv("LOG_EMAIL_ARCHIVE") # path to email archived log file
email_processed_log_path = os.getenv("LOG_EMAIL_PROCESSED") # path to email processed log file

# parses and logs emails
process_all_emails(email_file_path, email_archived_log_path, email_processed_log_path)

# searches log
search_string = 'test'
search_log(email_archived_log_path, search_string)


