import spf

# SPF - Sender Policy Framework
# Type of authetnication method
# Identifies mail servers that are allowed to send an email

# I can also use spf.check2. It would need 2 variables instead of 3.
# I will use 2 if the status code is uneeded, will revise later

def spf_check(ip, domain, sender):
    try:
        result, status_code, explanation = spf.check(ip, domain, sender)
        return result, status_code, explanation
    except Exception as e:
        return None, str(e)


# example
ip_address = '173.194.0.0'  
domain = 'gmail.com'
sender_email = 'user@gmail.com'

result, status_code, explanation = spf_check(ip_address, domain, sender_email)
print(f"SPF check result: {result}")
print(f"status code: {status_code}")
print(f"Explanation: {explanation}")


# results can equal to: pass(authorised), fail(not authorised), softfail(not authorised but not denied), 
# neutral(no indication of either), tempError, permError
# status code: 250 (request action completed successfully), 550(request action not taken)

