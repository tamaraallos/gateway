import re
from urllib.parse import urlparse
from email.utils import parseaddr
from typing import List


# Function to load phishing domains from a given file. Returns a set of phishing domains.
def load_phishing_domains(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file:
            domains = file.read().splitlines()
        return [domain.lower() for domain in domains]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file {file_path}: {e}")
        return []

# Function to load phishing links from a given file. Returns a set of phishing links.
def load_phishing_links(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file:
            links = file.read().splitlines()
        return [link.lower() for link in links]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file {file_path}: {e}")
        return []

# Function to extract the domain name from an email address.
def extract_domain(email_address: str) -> str:
    if '@' in email_address:
        domain = email_address.split('@')[-1]
    else:
        domain = ''
    return domain

# Function to extract all the links from an email message. Returns a list of links present.
def extract_links_from_email(email_message) -> List[str]:
    links = []
    for part in email_message.walk():
        if part.get_content_type() in ["text/plain", "text/html"]:
            body = part.get_payload(decode=True).decode(part.get_content_charset(), errors='replace')
            links.extend(re.findall(r'https?://\S+', body))
    return links

# Function to determine if an email is a phishing email based on known phishing domains and links.
def is_phishing_email(email_message, phishing_domains: List[str], phishing_links: List[str]) -> bool:
    sender_domain = extract_domain(parseaddr(email_message.get('From'))[1])

    # Check if the sender's domain is a known phishing domain
    if sender_domain in phishing_domains:
        return True

    # Extract all links from the email
    links_in_email = extract_links_from_email(email_message)

    # Check if any link in the email matches a known phishing link or domain
    for link in links_in_email:
        parsed_link = urlparse(link).netloc
        if parsed_link in phishing_links or parsed_link in phishing_domains:
            return True

    return False
