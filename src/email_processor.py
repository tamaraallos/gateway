import json
import os
from src.verify_checks import (parse_email_file, extract_email_data, check_phishing, dkim_check_result, dmarc_check_result, spf_check_result, check_spam, check_dlp_results, check_spoofing_results, check_type)

# function parses email and returns extracted content
def parse_email(file_path):
    try: 
        # parse email
        message = parse_email_file(file_path)
 
        # retrieve data from the parsed email
        email_data = extract_email_data(message)

        # perform security checks checks
        email_data = check_phishing(email_data, message)
        email_data = check_spam(email_data)
        email_data = check_dlp_results(email_data)
        email_data = check_spoofing_results(email_data, message)
        email_data = spf_check_result(email_data)
        email_data = dmarc_check_result(email_data)
        email_data = dkim_check_result(file_path, email_data)

        # update and cleans the type field
        email_data = check_type(email_data)

        return email_data
        
    except Exception as e:
        print(f"failed to parse email from the {file_path}: {e}")
        return None

# function stores email content in a log file
def log_email(log_file_path, email_content):
    if email_content: 
        # transform email content into JSON string
        json_email = json.dumps(email_content, indent=4) #4 idents according to python standards
        # write JSON string into log file
        with open(log_file_path, 'a') as log_file: # a = append json string
            log_file.write(json_email + '\n') # writes json email string to the file 

# function stores emails that have been processed (only file name)
def processed_email_storage(log_file_path, email_file_name):
    with open(log_file_path, 'a') as log_file:
        log_file.write(email_file_name + '\n') # write name of email into file

# functions reads log file and prints each line
def print_log_file(log_file_path):
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            print(line.strip())

# function load emails that are already processed
def load_emails_processed(log_file_path):
    emails_processedd = set() # initialise set object (using set for no dupes)
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                emails_processedd.add(line.strip()) # add email name to set and remove white space
            return emails_processedd

# function processes email and logs it into a log file
def process_and_log_email(email_file, log_archive_path, log_email_processed_path):
    email_details = parse_email(email_file) # parses email
    log_email(log_archive_path, email_details) # writes emails to archive email.log file
    processed_email_storage(log_email_processed_path, os.path.basename(email_file)) # logs email name to processed email log file

# automate processing of all emails in the email dire
def process_all_emails(email_dire, log_archive_path, log_email_processed_path):
    emails_processed = load_emails_processed(log_email_processed_path) # load emails that have been processed
    
    # list all files within the email dire
    for email_file in os.listdir(email_dire):
        if email_file.endswith(".eml") and email_file  not in emails_processed: # check if already processed
            email_file_path = os.path.join(email_dire, email_file) # joins email dire with email name to construct a path
            process_and_log_email(email_file_path, log_archive_path,log_email_processed_path) # parse, and log email