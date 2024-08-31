import os
import shutil
from cryptography.fernet import Fernet
from email.parser import BytesParser
from email.policy import default

# Example encryption key (should be securely managed in a real application)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def encrypt_email_content(content):
    """Encrypt the email content."""
    encrypted_content = cipher_suite.encrypt(content.encode('utf-8'))
    return encrypted_content

def save_encrypted_email(encrypted_content, original_file):
    """Save the encrypted email to the Sent folder."""
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Base directory for consistency
    approved_folder = os.path.join(base_dir,'..', "approved")
    
    if not os.path.exists(approved_folder):
        os.makedirs(approved_folder)
        print(f"Created 'approved' folder at {approved_folder}")

    encrypted_file_path = os.path.join(approved_folder, os.path.basename(original_file))
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)
    
    # Import log_email_details and logging locally to avoid circular import
    #from email_monitor import log_email_details, logging
    
    #logging.info(f"Email encrypted and saved to {encrypted_file_path}")
  
    #destination_path = os.path.join(approved_folder, os.path.basename(file_path))
        
    #log_email_details(file_path, destination_path, action="allow")
    #logging.info(f"Original email file {file_path} has been removed after sending.")
    

def encrypt_email(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=default).parse(f)
        email_content = msg.as_string()

        # Encrypt the email content
        encrypted_content = encrypt_email_content(email_content)

        # Save the encrypted email
        save_encrypted_email(encrypted_content, file_path)

        # Optionally, remove the original unencrypted file
        os.remove(file_path)
        print(f"Original file {file_path} deleted after encryption.")

    

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python encryption.py <path_to_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    encrypt_email(file_path)
