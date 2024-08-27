# email_security.py

import re
import email
from email import policy
from email.parser import BytesParser
from typing import List


def load_spam_keywords(file_path: str) -> List[str]:
    """
    Load spam keywords from a given file.

    Args:
        file_path (str): Path to the file containing spam keywords.

    Returns:
        List[str]: A list of spam keywords.
    """
    try:
        with open(file_path, 'r') as file:
            keywords = file.read().splitlines()
        return [keyword.lower() for keyword in keywords]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file {file_path}: {e}")
        return []


def is_spam(email_text: str, spam_keywords: List[str]) -> bool:
    """
    Detect if an email is spam based on the presence of spam keywords.

    Args:
        email_text (str): The text of the email.
        spam_keywords (List[str]): A list of spam keywords.

    Returns:
        bool: True if the email contains spam keywords, False otherwise.
    """
    email_text = email_text.lower()

    # Check for presence of any spam keyword in the email text
    for keyword in spam_keywords:
        if keyword in email_text:
            return True
    return False