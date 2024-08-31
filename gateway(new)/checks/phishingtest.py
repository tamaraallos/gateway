import re
from urllib.parse import urlparse
from email.utils import parseaddr

def load_phishing_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            return [domain.lower() for domain in file.read().splitlines()]
    except Exception as e:
        print(f"Error loading phishing domains: {e}")
        return []

def load_phishing_links(file_path):
    try:
        with open(file_path, 'r') as file:
            return [link.lower() for link in file.read().splitlines()]
    except Exception as e:
        print(f"Error loading phishing links: {e}")
        return []

def is_phishing_email(email_message, phishing_domains, phishing_links):
    sender_domain = parseaddr(email_message.get('From'))[1].split('@')[-1]
    if sender_domain in phishing_domains:
        return True

    links = extract_links_from_email(email_message)
    for link in links:
        parsed_link = urlparse(link).netloc
        if parsed_link in phishing_links or parsed_link in phishing_domains:
            return True

    return False
