import spf
import socket

# SPF - Sender Policy Framework
# Type of authetnication method
# Identifies mail servers that are allowed to send an email

# function gets ip from domain
def get_ip_from_domain(domain):
    ip_address = socket.gethostbyname(domain)
    return ip_address

def spf_check(sender):
    domain = sender.split('@', 1)[1]
    ip_address = get_ip_from_domain(domain)
    _, status_code, _ = spf.check(ip_address, domain, sender)
    return status_code

# if spf status code is not 250 or 451, it fails
def check_spf_status_code(sender):
    status_code = spf_check(sender)
    if status_code == 250 or status_code == 451:
        return True
    else:
        return False 
