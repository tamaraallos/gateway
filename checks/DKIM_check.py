import dkim
import os
from email import policy

# DKIM Check Function
# This function verifies the DKIM signature of an email file.

def dkim_check(file_path):
    # Open and read the email file in binary mode
    with open(file_path, 'rb') as file:
        email_content = file.read()

    try:
        # Verify the DKIM signature of the email
        result = dkim.verify(email_content)  # Verifies DKIM signature of the email
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

if __name__ == "__main__":
    # Path to the email file passed as an argument
    email_path = os.path.join('emails', 'Test.eml')
    dkim_result = dkim_check(email_path)
    print(f"DKIM check result: {dkim_result}")
