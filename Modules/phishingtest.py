# phishing_detection.py

import re
from urllib.parse import urlparse
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr
from typing import List


def load_phishing_domains(file_path: str) -> List[str]:
    """
    Load phishing domains from a given file.

    Args:
        file_path (str): Path to the file containing phishing domains.

    Returns:
        List[str]: A list of phishing domains.
    """
    with open(file_path, 'r') as file:
        domains = file.read().splitlines()
    return domains


def load_phishing_links(file_path: str) -> List[str]:
    """
    Load phishing links from a given file.

    Args:
        file_path (str): Path to the file containing phishing links.

    Returns:
        List[str]: A list of phishing links.
    """
    with open(file_path, 'r') as file:
        links = file.read().splitlines()
    return links


def extract_links_from_email(email_message) -> List[str]:
    """
    Extract all links from an email message.

    Args:
        email_message (email.message.EmailMessage): The email message object.

    Returns:
        List[str]: A list of URLs found in the email.
    """
    links = []
    for part in email_message.walk():
        if part.get_content_type() in ["text/plain", "text/html"]:
            body = part.get_payload(decode=True).decode(part.get_content_charset(), errors='replace')
            links.extend(re.findall(r'https?://\S+', body))
    return links


def is_phishing_email(email_message, phishing_domains: List[str], phishing_links: List[str]) -> bool:
    """
    Determine if an email is a phishing email based on the presence of known phishing domains or links.

    Args:
        email_message (email.message.EmailMessage): The email message object.
        phishing_domains (List[str]): A list of known phishing domains.
        phishing_links (List[str]): A list of known phishing links.

    Returns:
        bool: True if the email is phishing, False otherwise.
    """
    sender_domain = extract_domain(parseaddr(email_message.get('From'))[1])

    # Check if the sender's domain is a known phishing domain
    if sender_domain in phishing_domains:
        return True

    # Extract all links from the email
    links_in_email = extract_links_from_email(email_message)

    # Check if any link in the email matches a known phishing link
    for link in links_in_email:
        parsed_link = urlparse(link).netloc
        if parsed_link in phishing_links or parsed_link in phishing_domains:
            return True

    return False
