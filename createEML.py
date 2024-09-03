import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv(".env")


# this script generates an email in .eml format (this is for testing purposes)
# uses MIME - multiplepurpose Internet Mail Extnesion - support transfer of text and text attatchments
# variables: create test email content - follow this structure please
to_address = "tester@gmail.com" 
from_address = "adminBSI@gmail.com"
subject = "Personal Info - For payslips"
date = "Tuesday, 03 Sep 2024 12:39:34 -0000"
#body = "test"
action_status = "pending" 
email_type = "normal"

# for phishing test
# body = """
# Dear User at BSI,

# Your account has been temporarily suspended due to suspicious activity. To reactivate your account, please verify your identity by clicking the link below:

# https://2020logs.duckdns.org/verify

# Failure to do so within 24 hours will result in permanent account deactivation.

# Thank you,
# Support Team from BSI
# """

body = """
 Hey,
 Hope you are well. I was just sending you the details you requested so you guys can verify my account information:
 Credit Card Number: 4111 1111 1111 1111
 Bank Account Number: 98765432101234567
 PIN Number: 654321
 Tax File Number: 123 456 789

 Thanks,
 Teddy
"""

body = body.replace("\n", " ").strip()

# encrypt_body = cipher_suite.encrypt(body.encode())

# pass in email content into parameters to create an email
def generate_email(to_address, from_address, subject, date, body, action_status, email_type):
    # constructs email message
    msg = MIMEMultipart() # create new message object
    # sets email headers
    msg["To"] = to_address
    msg["From"] = from_address
    msg["Subject"] = subject
    msg["Date"] = date
    msg['X-Action-Status'] = action_status # custom header for the action status
    msg['X-Type'] = email_type # custom header for the emial type
    
    msg.attach(MIMEText(body, 'plain')) # MIME represents textual data (attatched plain text body to email)
    return msg

# generate the email
email = generate_email(to_address, from_address, subject, date, body, action_status, email_type)

# save email to my 'email' folder
dire = os.getenv("EMAIL_FOLDER")

# format email file name to be 'emailN' n being number of email generated
existing_file = []

# loop through all the files in the dire
for email_file in os.listdir(dire):
    if email_file.startswith('email') and email_file.endswith('.eml'): # check if file name starts with email and ends with .eml
        existing_file.append(email_file) # add to the list

# number for file name
next_num = len(existing_file) + 1

# file name format 
file_name = 'email' + str(next_num) + '.eml'

# change working dire to the dire outlined
os.chdir(dire)

# write the EML format file
with open(file_name, 'w') as file: # w opens file for writing
    eml_generator = generator.Generator(file) # convert into flat text format
    eml_generator.flatten(email)
    print(f'Email successfuly created!')
