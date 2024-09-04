import os
from cryptography.fernet import Fernet
from email.parser import BytesParser
from email.policy import default

# Example encryption key (should be securely managed in a real application)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Encrypt the email_content
def encrypt_email_content(content):
    """Encrypt the email content."""
    encrypted_content = cipher_suite.encrypt(content.encode('utf-8'))
    return encrypted_content

# Save the encrypted file in a new folder
def save_encrypted_email(encrypted_content, original_file):
    """Save the encrypted email to the Sent folder."""
    sent_folder = os.path.join(os.path.dirname(original_file), "Sent")
    if not os.path.exists(sent_folder):
        os.makedirs(sent_folder)
        print(f"Created 'Sent' folder at {sent_folder}")

    encrypted_file_path = os.path.join(sent_folder, os.path.basename(original_file))
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)
    
    print(f"Email encrypted and saved to {encrypted_file_path}")

# Encrypt the email and remove the unencrypted email from the server
def encrypt_email(file_path):
    try:
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
            return True
        
    except Exception as e:
        print(f"Failed to process email {file_path}: {e}")
        return False
