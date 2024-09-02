import spf
import socket

# SPF - Sender Policy Framework
# Type of authetnication method
# Identifies mail servers that are allowed to send an email

# function gets ip from domain
def get_ip_from_domain(domain):
    ip_address = socket.gethostbyname(domain)
    return ip_address

def spf_check(domain, sender):
    ip_address = get_ip_from_domain(domain)
    _, status_code, _ = spf.check(ip_address, domain, sender)
    return status_code

# if spf status code is not 250, it fails
def check_spf_status_code(domain, sender):
    status_code = spf_check(domain, sender)
    if status_code == 250:
        return True
    else:
        return False 


# BELOW IS AN EXAMPLE FOR TESTING PURPOSES
# IT NEEDS TO BE DELETED AFTER TESTING.
domain = 'gmail.com'
sender_email = 'user@gmail.com'

status_code = check_spf_status_code(domain, sender_email)

print(f"spf status code: {status_code}")