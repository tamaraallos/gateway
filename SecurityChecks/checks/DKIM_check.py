import dkim
import email
from email import policy

# DomainKey Identified Mail
# Email authetnication method - uses digital signature

def dkim_check(file_path):
    # open and read email file
    with open(file_path, 'rb') as file:
        email_content = file.read()
    
    try:
        # parse email and extract headers
        # msg = email.message_from_bytes(email_content, policy=policy.default)
        # print(f"The message is: {msg}") # for my testing

        # verify DKIM signature
        result = dkim.verify(email_content) # verifies dkim signature of email
        # print(f"the result is: {result}") # for my testing
        return result
    except Exception as e:
        print(f"Error occured: {e}")
        return False
    
# testing - This will always fail bc I dont have access to emails with DKIM signature
file_path_email = '../emails/Test.eml'
dkim_result = dkim_check(file_path_email)
print(f"DKIM check result: {dkim_result}")