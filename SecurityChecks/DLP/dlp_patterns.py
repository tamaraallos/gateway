import re

# Define DLP patterns for detection
DLP_PATTERNS = {
    'Credit Card': r'\b(?:\d[ -]*?){13,16}\b',
    'Debit Card': r'\b(?:\d[ -]*?){13,16}\b',  # Placeholder pattern similar to credit card
    'Sensitive Keywords': r'\b(confidential|proprietary|secret)\b',
    'Bank Account Number': r'\b\d{8,17}\b',  # Example: 8 to 17 digits for various formats
    'PIN Number': r'\b\d{4,6}\b',  # Example: 4 to 6 digits, common lengths for PINs
    'Tax File Number': r'\b\d{3} \d{3} \d{3}\b',  # Example format for Australian Tax File Numbers (TFNs)
    'Phone Number': r'\b(?:\+?(\d{1,3})?[-.\s]?)?((\(\d{1,4}\))|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b',
    'Email Address': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'Street Address': r'\b\d{1,5}\s+\b[A-Za-z0-9.\s,-]+\b(?:Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Lane|Ln|Drive|Dr)\b',
    'Passport Number': r'\b[A-PR-WYa-pr-wy][1-9]\d\s?\d{4}[1-9]\b',  # Generic passport number pattern
    'IP Address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    'MAC Address': r'\b([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})\b',
    'Driver License Number': r'\b[A-Z0-9]{1,9}\b'  # Generic pattern for driver's license numbers
}

#Check content against DLP patterns
def check_dlp(content):
    findings = {}
    for name, pattern in DLP_PATTERNS.items():
        matches = re.findall(pattern, content)
        if matches:
            findings[name] = matches
    return findings
