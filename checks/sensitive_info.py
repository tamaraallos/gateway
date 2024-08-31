import re

# Define patterns for Australian context and potential breaches
PATTERNS = {
    'Credit Card': r'\b(?:\d[ -]*?){13,16}\b',
    'Tax File Number': r'\b\d{3} \d{3} \d{3}\b',
    'Medicare Number': r'\b\d{4} \d{5} \d\b',
    'Sensitive Keywords': r'\b(confidential|proprietary|secret|classified|restricted)\b',
    'Bank Account Number': r'\b\d{6,10}[- ]?\d{6,10}\b',
    'PIN Number': r'\b\d{4,6}\b',
    'Company Exit Plans': r'\b(resignation|quit|leaving|new job|offer letter)\b',
    'Unauthorized Sharing': r'\b(disclose|share externally|forwarded to)\b',
    'Project Leakage': r'\b(project details|client information|RFP)\b'
}

# Function to flag content against defined patterns
def flag_content(content, patterns):
    flags = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            flags[name] = matches
    return flags

# Function to evaluate a single email file
def evaluate_email(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    flags = flag_content(content, PATTERNS)
    if flags:
        print(f"Potential policy breaches found in {file_path}: {flags}")
        # Report findings for manual review by the admin
    else:
        print(f"No policy breaches found in {file_path}.")
        # No issues detected, report for further actions

# Example usage:
# Replace 'emails/sample_email.eml' with the actual email file path
# evaluate_email('emails/sample_email.eml')
# Example of usage
if __name__ == "__main__":
    # Sample content to scan (replace this with actual email content)
    sample_content = """
    This email contains confidential information. The user's credit card number is 4111 1111 1111 1111.
    Their Australian Business Number (ABN) is 12 345 678 901.
    """
    
    findings = flag_content(sample_content, PATTERNS)
    if findings:
        print("Sensitive data found:")
        for item, data in findings.items():
            print(f"{item}: {data}")
    else:
        print("No sensitive data detected.")
