import os
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
    sent_folder = os.path.join(os.path.dirname(original_file), "Sent")
    if not os.path.exists(sent_folder):
        os.makedirs(sent_folder)
        print(f"Created 'Sent' folder at {sent_folder}")

    encrypted_file_path = os.path.join(sent_folder, os.path.basename(original_file))
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)
    
    print(f"Email encrypted and saved to {encrypted_file_path}")

def process_email(eml_file):
    try:
        with open(eml_file, 'rb') as f:
            msg = BytesParser(policy=default).parse(f)
            email_content = msg.as_string()

            # Encrypt the email content
            encrypted_content = encrypt_email_content(email_content)

            # Save the encrypted email
            save_encrypted_email(encrypted_content, eml_file)

            # Optionally, remove the original unencrypted file
            os.remove(eml_file)
            print(f"Original file {eml_file} deleted after encryption.")

    except Exception as e:
        print(f"Failed to process email {eml_file}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python encryption.py <path_to_eml_file>")
        sys.exit(1)

    eml_file = sys.argv[1]
    process_email(eml_file)