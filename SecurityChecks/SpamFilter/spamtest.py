from typing import List

# Function to load spam keywords from a file. Returns a list of spam keywords.
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

# Function to detect if an email is spam based on the list of spam keywords. Returns bool.
def is_spam(email_text: str, spam_keywords: List[str]) -> bool:
    # converts text to lowercase.
    email_text = email_text.lower()
    for keyword in spam_keywords:
        if keyword in email_text:
            return True
    return False