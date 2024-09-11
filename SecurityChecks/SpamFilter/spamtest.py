import re
from typing import List

# function to load spam keywords from a file. Returns a list of spam keywords
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

# function to detect if an email is spam based on the list of spam keywords
def is_spam(email_text: str, spam_keywords: List[str]) -> bool:
    # convert the email text to lowercase
    email_text = email_text.lower()

    for keyword in spam_keywords:
        # use regular expression to match whole words only, with word boundaries
        if re.search(rf'\b{re.escape(keyword)}\b', email_text):
            return True
    return False
