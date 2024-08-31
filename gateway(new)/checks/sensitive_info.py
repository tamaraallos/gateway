import re

# Updated sensitive information patterns for DLP check
DLP_PATTERNS = {
    'Credit Card': r'\b(?:\d[ -]*?){13,16}\b',
    'Tax File Number': r'\b\d{3} \d{3} \d{3}\b',
    'Confidential Keywords': r'\b(confidential|proprietary|secret|classified|private)\b',
    'Bank Account Number': r'\b\d{8,17}\b',
    'PIN Number': r'\b\d{4,6}\b',
    'Company Sensitive Data': r'\b(balance sheet|project plan|strategy document)\b'
}

def check_sensitive_info(content):
    findings = {}
    for label, pattern in DLP_PATTERNS.items():
        matches = re.findall(pattern, content)
        if matches:
            findings[label] = matches
    return findings
