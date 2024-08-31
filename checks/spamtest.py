import re
from typing import List

# Function to load spam keywords from a given file. Returns a list of keywords.
def load_spam_keywords(file_path: str) -> List[str]:
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

# Function to check if an email contains spam based on known spam keywords.
def is_spam_email(content: str, spam_keywords: List[str]) -> bool:
    content = content.lower()
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', content):
            return True
    return False

# Example usage (should be removed or commented out in production):
spam_keywords_path = "keywords/spam_keywords.txt"
spam_keywords = load_spam_keywords(spam_keywords_path)
email_content = "This is an example email content to check for spam."
if is_spam_email(email_content, spam_keywords):
    print("The email is classified as spam.")
else:
    print("The email is not classified as spam.")
