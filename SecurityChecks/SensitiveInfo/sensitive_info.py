import re

# Extended sensitive data patterns
SENSITIVE_PATTERNS = {
    'Tax File Number': r'\b\d{3}\s*\d{3}\s*\d{3}\b',
    'Credit Card Number': r'\b(?:\d[ -]*?){13,16}\b',
    'Medicare Number': r'\b\d{4}\s*\d{5}\s*\d{1}\b',
    'Driver\'s License Number': r'\b[A-Z]{1,2}\d{5,9}\b',
    'Passport Number': r'\b[A-Z]{1,2}\d{7,9}\b',
    'Bank Account Number': r'\b\d{2,6}\s*\d{2,6}\s*\d{1,6}\b',
    'BSB Number': r'\b\d{3}\s*\d{3}\b',
    'Health Information': r'\b(health|medical|diagnosis|prescription)\b',
    'Balance Sheet': r'\b(balance\s*sheet)\b',
    'Confidential Plan': r'\b(confidential|plan)\b',
    'Superannuation Details': r'\b(superannuation|super\s*fund|super\s*account)\b',
    'IP Address': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    'Email Address': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'Phone Number': r'\b(\+?\d{1,3}[-.\s]?)?(\(?\d{1,4}\)?[-.\s]?)?[\d\s]{5,14}\b',
    'Security Information': r'\b(password|passcode|PIN|encryption\s*key|auth\s*code)\b',
}

def extract_content(msg):
    content = []
    if msg.is_multipart():
        for part in msg.iter_parts():
            content_type = part.get_content_type()
            disposition = part.get_content_disposition()
            if disposition is None:  # Not an attachment
                try:
                    if content_type in ['text/plain', 'text/html']:
                        charset = part.get_content_charset() or 'utf-8'
                        payload = part.get_payload(decode=True).decode(charset)
                        content.append(payload)
                except Exception as e:
                    print(f"Failed to decode part of type {content_type}: {e}")
    else:
        try:
            charset = msg.get_content_charset() or 'utf-8'
            payload = msg.get_payload(decode=True).decode(charset)
            content.append(payload)
        except Exception as e:
            print(f"Failed to decode email content: {e}")
    
    return "\n".join(content) if content else ""

def check_sensitive_data(content, patterns):
    detected = []
    for data_type, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            print(f"Detected {data_type} in the content!")
            detected.append(data_type)
    return detected

def check_email_sensitivity(msg):

    content = extract_content(msg)
    detected_sensitive_data = check_sensitive_data(content, SENSITIVE_PATTERNS)

    if detected_sensitive_data:
        print(f"Unsafe: Sensitive data detected - {', '.join(detected_sensitive_data)}")
    
    print(f"Result for {msg}: {'Safe' if not detected_sensitive_data else 'Unsafe'}")
    return
