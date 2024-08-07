import email
from email import policy
from email.parser import BytesParser
import json

# function parses email and returns extracted content
def parse_email(file_path):
    try: # using try and catch block
        # open then parse email
        with open(file_path, 'rb') as file: #open file in read binary 
            # using default policy for parsing the email msgs - policies define how aspects of email msgs are handled
            message = BytesParser(policy=policy.default).parse(file)

        # retrieve data from the parsed email
        email_data = {
            'to': message['to'],
            'subject': message['subject'],
            'from': message['from'],
            'date': message['date'], # formats the date
            'body': message.get_body(preferencelist=('plain', 'html')).get_content()
            # is there anything else im missing
        }

        print('success')
        return email_data
    # error handling - throw error if code in try doesn't work
    except Exception as e:
        print(f"failed to parse email from the {file_path}: {e}")
        return None

# function stores emails in a log file
def log_email(log_file_path, email_content):
    # transform email content into JSON string
    json_email = json.dumps(email_content, indent=4) #4 idents according to python standards

    # write JSONs tring into log file
    with open(log_file_path, 'a') as log_file: # a = append json string
        log_file.write(json_email + '\n') # writes json email string to the file 

# function processes email and logs it into a log file
def process_and_log_email(path_file, log_file_path):
    # parse email
    email_details = parse_email(path_file)

    # write to log file
    log_email_details = log_email(log_file_path, email_details)


# example
root_dire = "C:/Users/Tamara/Desktop/BSI/gateway"
email_path_file = './emails/82224dd6-9780-4e79-9cd1-507cd368fd4e.eml'
log_file_path = './log/test.log'

process_and_log_email(email_path_file, log_file_path)

# search for specific string from log files and return line number 
def search_log(log_file_path, search_string):
    try:
        line_count = 1 # initalise the line count
        with open(log_file_path, 'r') as log_file: # file opened in read mode
            for line in log_file:
                if search_string in line:
                    print(f"Found '{search_string}' on line {line_count}: {line.strip()}")
                line_count += 1 # increment line count
    except Exception as e: # throw error 
        print(f"An error has occured: {e}")

search_string = 'admin'
search_log(log_file_path, search_string)
