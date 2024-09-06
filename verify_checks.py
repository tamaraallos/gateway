from email import policy
from email.parser import BytesParser
from SecurityChecks.PhishingFilter.phishingtest import (is_phishing_email, load_phishing_domains, load_phishing_links)
from SecurityChecks.SpamFilter.spamtest import (load_spam_keywords, is_spam)
from SecurityChecks.DLP.dlp_patterns import (check_dlp)
from SecurityChecks.spoofing.spoofing import (check_spoofing)
from SecurityChecks.encryption.encryption import (encrypt_body)

# parse email file
def parse_email_file(file_path):
    # open then parse email
    with open(file_path, 'rb') as file: # open file in read binary 
        # using default policy for parsing the email msgs - policies define how aspects of email msgs are handled
        return BytesParser(policy=policy.default).parse(file)

# extract email data
def extract_email_data(message):
    return { 
        'to': message['to'],
        'subject': message['subject'],
        'from': message['from'],
        'date': message['date'],
        'action status': "allowed",
        'type': '',
        'body': message.get_body(preferencelist=('plain', 'html')).get_content()
    }

# below all modify the email_data action_status and type.
# it checks if the content of the emails contain security threats

# phishing
def check_phishing(email_data, message):
    phishing_domains = load_phishing_domains('SecurityChecks/PhishingFilter/phishing_domains.txt')
    phishing_links = load_phishing_links('SecurityChecks/PhishingFilter/phishing_links.txt')
    
    if is_phishing_email(message, phishing_domains, phishing_links):
        email_data['action status'] = 'blocked'
        email_data['type'] += 'Phishing, '
    return email_data

# spam
def check_spam(email_data):
    spam_keywords = load_spam_keywords('SecurityChecks/SpamFilter/spam_keywords.txt')
    if is_spam(email_data['body'], spam_keywords):
        email_data['action status'] = 'blocked'
        email_data['type'] += 'Spam, '
    return email_data

# dlp check
def check_dlp_results(email_data):
    dlp_results = check_dlp(email_data['body'])
    if dlp_results:
        email_data['action status'] = 'blocked' # changed to pending
        email_data['type'] += 'DLP Violation, '
        encrypted_body = encrypt_body(email_data['body'])
        email_data['body'] = encrypted_body # encrypts body of email
    return email_data

# spoofing
def check_spoofing_results(email_data, message):
    spoofing_results = check_spoofing(message)
    if spoofing_results:
        email_data['action status'] = 'blocked'
        email_data['type'] += 'Spoofing, '
    return email_data

# check email type
def check_type(email_data):
    if email_data['type']:
        email_data['type'] = email_data['type'].rstrip(', ')
    else:
        email_data['type'] = 'normal'
    return email_data