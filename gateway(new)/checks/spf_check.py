import spf

# SPF - Sender Policy Framework
# Type of authentication method
# Identifies mail servers that are allowed to send an email

# I can also use spf.check2. It would need 2 variables instead of 3.
# I will use 2 if the status code is unnecessary; will revise later.

def spf_check(ip, domain, sender):
    try:
        result, status_code, explanation = spf.check(ip, domain, sender)
        return result, status_code, explanation
    except Exception as e:
        return None, str(e)


# Example usage for testing
if __name__ == "__main__":
    ip_address = '173.194.0.0'  
    domain = 'gmail.com'
    sender_email = 'user@gmail.com'

    result, status_code, explanation = spf_check(ip_address, domain, sender_email)
    print(f"SPF check result: {result}")
    print(f"Status code: {status_code}")
    print(f"Explanation: {explanation}")


# Results can equal: pass (authorized), fail (not authorized), softfail (not authorized but not denied), 
# neutral (no indication of either), tempError, permError
# Status code: 250 (request action completed successfully), 550 (request action not taken)
