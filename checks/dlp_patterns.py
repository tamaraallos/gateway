import re

# Improved DLP patterns for Australian context
DLP_PATTERNS = {
    'Credit Card': r'\b(?:\d[ -]*?){13,16}\b',  # Pattern for credit card numbers
    'Debit Card': r'\b(?:\d[ -]*?){13,16}\b',  # Similar to credit card pattern
    'Sensitive Keywords': r'\b(confidential|proprietary|secret|classified)\b',  # Sensitive keywords
    'Bank Account Number': r'\b\d{8,17}\b',  # Australian bank account numbers (typically 6-9 digits)
    'PIN Number': r'\b\d{4,6}\b',  # 4 to 6 digits for PINs
    'Tax File Number': r'\b\d{3} \d{3} \d{3}\b',  # Australian TFN format
    'ABN Number': r'\b\d{2} \d{3} \d{3} \d{3}\b',  # Australian Business Number (ABN)
    'Medicare Number': r'\b\d{4} \d{5} \d\b',  # Australian Medicare card number format
    'Passport Number': r'\b[a-zA-Z]\d{7}\b',  # Australian passport number format
    'Driver’s License': r'\b\d{9}\b',  # Common Australian driver’s license format (varies by state)
    'Email Addresses': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',  # Email address detection
}

def check_dlp(content, patterns):
    """
    This function checks content against the provided DLP patterns.
    :param content: The email or file content to scan.
    :param patterns: A dictionary of DLP patterns to check for.
    :return: A dictionary of findings with the pattern names and matches.
    """
    findings = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            findings[name] = matches
    return findings

# Example of usage
if __name__ == "__main__":
    # Sample content to scan (replace this with actual email content)
    sample_content = """
    This email contains confidential information. The user's credit card number is 4111 1111 1111 1111.
    Their Australian Business Number (ABN) is 12 345 678 901.
    """
    
    findings = check_dlp(sample_content, DLP_PATTERNS)
    if findings:
        print("Sensitive data found:")
        for item, data in findings.items():
            print(f"{item}: {data}")
    else:
        print("No sensitive data detected.")
