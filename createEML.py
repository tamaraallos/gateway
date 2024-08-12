import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# this script generates an email in .eml format (this is for testing purposes)
# uses MIME - multiplepurpose Internet Mail Extnesion - support transfer of text and text attatchments

# variables: create test email content - follow this structure please
to_address = "John.Doe@gmail.com" 
from_address = "Jane.Doe@gmail.com"
subject = "Admin Meeting"
date = "Thursday, 10 Jul 2024 12:39:34 -0000"
body = "Hey John, how is it going? I just wanted to send you a message to see if you got a message from admin? They asked me for a meeting. I was wondering if this was to do with the software we were working on? Thanks Jane."

# pass in email content into parameters to create an email
def generate_email(to_address, from_address, subject, date, body):
    # constructs email message
    msg = MIMEMultipart() # create new message object
    # sets email headers
    msg["To"] = to_address
    msg["From"] = from_address
    msg["Subject"] = subject
    msg["Date"] = date
    msg.attach(MIMEText(body, 'plain')) # MIME represents textual data (attatched plain text body to email)
    return msg

# generate the email
email = generate_email(to_address, from_address, subject, date, body)

# save email to my file
dire = "C:\\Users\\Tamara\\Desktop\\BSI\\gateway\\emails"


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
