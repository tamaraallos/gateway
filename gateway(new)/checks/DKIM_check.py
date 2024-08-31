
import os
from email import policy
import dkim

def dkim_check(file_path):
    with open(file_path, 'rb') as file:
        email_content = file.read()

    try:
        result = dkim.verify(email_content)
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
