import os
from email import message_from_bytes
from email.utils import parseaddr

def load_email(file_path):
    """Load the email content from a file."""
    with open(file_path, 'rb') as f:
        email_content = f.read()
    return message_from_bytes(email_content)

def extract_domain(email_address):
    """Extract the domain from an email address."""
    return email_address.split('@')[-1]

def spoofing_check(email_path):
    """Check if the email is spoofed by comparing the 'From' and 'Return-Path' domains."""
    try:
        email_message = load_email(email_path)

        # Extract 'From' and 'Return-Path' headers
        from_address = parseaddr(email_message.get('From'))[1]
        return_path = parseaddr(email_message.get('Return-Path'))[1]

        from_domain = extract_domain(from_address)
        return_domain = extract_domain(return_path)

        # Compare the domains
        if from_domain != return_domain:
            return False, f"Spoofing detected: 'From' domain ({from_domain}) does not match 'Return-Path' domain ({return_domain})."
        else:
            return True, "No spoofing detected."

    except Exception as e:
        return False, f"Error occurred during spoofing check: {e}"

# Example usage
if __name__ == "__main__":
    email_path = os.path.join('emails', 'Test_email.eml')
    result, message = spoofing_check(email_path)
    print(f"Spoofing check result: {result}, Message: {message}")
