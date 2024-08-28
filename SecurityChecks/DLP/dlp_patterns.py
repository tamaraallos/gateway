import re

# Define DLP patterns for detection
DLP_PATTERNS = {
    'Credit Card': r'\b(?:\d[ -]*?){13,16}\b',
    'Debit Card': r'\b(?:\d[ -]*?){13,16}\b',  # Placeholder pattern similar to credit card
    'Sensitive Keywords': r'\b(confidential|proprietary|secret)\b',
    'Bank Account Number': r'\b\d{8,17}\b',  # Example: 8 to 17 digits for various formats
    'PIN Number': r'\b\d{4,6}\b',  # Example: 4 to 6 digits, common lengths for PINs
    'Tax File Number': r'\b\d{3} \d{3} \d{3}\b',  # Example format for Australian Tax File Numbers (TFNs)
}

#Check content against DLP patterns
def check_dlp(content, patterns):
    findings = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            findings[name] = matches
    return findings
