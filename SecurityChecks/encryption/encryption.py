from cryptography.fernet import Fernet

# Example encryption key (should be securely managed in a real application)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Encrypt email body
def encrypt_body(content):
    encrypted_content = cipher_suite.encrypt(content.encode('utf-8'))
    return encrypted_content.decode('utf-8')


