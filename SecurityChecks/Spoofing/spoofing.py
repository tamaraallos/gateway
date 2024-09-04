from email.parser import BytesParser
from email.policy import default


def check_spoofing_indicators(msg):
    """Check for common signs of email spoofing."""
    results = []

    # Check if the 'Received' headers are suspicious
    received_headers = msg.get_all('Received', [])
    if len(received_headers) > 1:
        results.append("Multiple 'Received' headers detected, which can indicate forwarding or spoofing.")

    # Add more checks as needed...

    return results

def spoofing(msg):

    spoofing_indicators = check_spoofing_indicators(msg)
    if spoofing_indicators:
        print(f"Spoofing indicators found in {msg}:")
        for indicator in spoofing_indicators:
            print(f"  - {indicator}")
    else:
        print(f"No spoofing indicators found in {msg}.")
