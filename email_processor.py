from email import policy
from email.parser import BytesParser
import json
import os
from SecurityChecks.PhishingFilter.phishingtest import (is_phishing_email, load_phishing_domains, load_phishing_links)
from SecurityChecks.SpamFilter.spamtest import (load_spam_keywords, is_spam)
from SecurityChecks.DLP.dlp_patterns import check_dlp

# note to all
# apply integeration of other code checks.
# if something returns false it needs to modify
# type to be equal to type = spam, spoof, phishing, etc
# action status needs to be blocked.
# is true do nothing
## SEE HOW I DID IT LINE 44 - 58

# function parses email and returns extracted content
def parse_email(file_path):
    try: # using try and catch block

        # phishing - reading phishing files
        phishing_domains = load_phishing_domains('SecurityChecks/PhishingFilter/phishing_domains.txt')
        phishing_links = load_phishing_links('SecurityChecks/PhishingFilter/phishing_links.txt')

        # spam - reading spam files
        spam_keywords = load_spam_keywords('SecurityChecks/SpamFilter/spam_keywords.txt')

        # open then parse email
        with open(file_path, 'rb') as file: #open file in read binary 
            # using default policy for parsing the email msgs - policies define how aspects of email msgs are handled
            message = BytesParser(policy=policy.default).parse(file)

        # retrieve data from the parsed email
        email_data = { 
            'to': message['to'],
            'subject': message['subject'],
            'from': message['from'],
            'date': message['date'],
            'action status': message['X-Action-Status'],
            'type': message['X-Type'],
            'body': message.get_body(preferencelist=('plain', 'html')).get_content()
        }

        # Phishing check
        if is_phishing_email(message, phishing_domains, phishing_links):
            print("Phishing detected. Updating email status.") # for testing purposes
            email_data['action status'] = 'blocked'
            email_data['type'] = 'phishing'
        else:
            print("No phishing detected.") # delete later for testing

        # Spam Check
        if is_spam(email_data['body'], spam_keywords): 
            print("spam detected. Updating email stat") # for testing purposes
            email_data['action status'] = 'blocked'
            email_data['type'] = 'spam'
        else:
            print("no spam detected") # delete later for testing

        #   READ LINE 8 to 14 FOR INTEGRATION
        # integrate yours here...
        
        #DLP Check
        dlp_results = check_dlp(email_data['body'])
        if dlp_results :
            print("DLP Violation Detected. Updating email status") # this is for testing purposes
            email_data['action_status'] = 'blocked'
            email_data['type'] = 'DLP Violation'
        else:
            print("No DLP Voilations detected.") # delete later for testing


        #print(f'{file_path} has been successfully parsed!') # testing purposes
        return email_data
    # error handling - throw error if code in try doesn't work
    except Exception as e:
        #print(f"failed to parse email from the {file_path}: {e}")
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
        #print(f"file name successfully written to process email log file: {email_file_name}") # for testing

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
        #else:
            #print(f"already processed email thats being skipped: {email_file}")
