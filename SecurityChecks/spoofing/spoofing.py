# checks message content for spoofing via header
def check_spoofing_indicators(msg):
    results = []
    # Check if the 'Received' headers are suspicious
    received_headers = msg.get_all('Received', [])
    if len(received_headers) > 1:
        results.append("Multiple 'Received' headers detected, which can indicate forwarding or spoofing.")
    return results

#  returns true or false whether or not an email has been detected for spoofing
def check_spoofing(msg):
    spoofing_indicators = check_spoofing_indicators(msg)
    return True if spoofing_indicators else False 
