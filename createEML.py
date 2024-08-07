import uuid
import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# this script generates an email in .eml format (this is for testing purposes)
# uses MIME - multiplepurpose Internet Mail Extnesion - support transfer of text and text attatchments

# variables: create test email content - follow this structure please
to_address = "daniel@email.com"
from_address = "somehow@email.com"
subject = "just email"
date = "Thursday, 10 Jul 2024 18:16:34 -0000"
body = "just another email testing words, stuff, hi no yes, bye. afternoon."

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
file_name = str(uuid.uuid4()) + ".eml" # using .eml format for parser

# change working dire to the dire outlined
os.chdir(dire)


# write the EML format file
with open(file_name, 'w') as file: # w opens file for writing
    eml_generator = generator.Generator(file) # convert into flat text format
    eml_generator.flatten(email)
    print(f'email successfully saved')
