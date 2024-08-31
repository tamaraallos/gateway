import dns.resolver

def dmarc_check(domain):
    """
    This function checks the DMARC record for a given domain.
    :param domain: The domain to check DMARC for.
    :return: The DMARC record if found, otherwise None.
    """
    try:
        # Construct the DMARC domain name
        dmarc_domain = f"_dmarc.{domain}"
        
        # Query the DNS for the DMARC TXT record
        result = dns.resolver.resolve(dmarc_domain, 'TXT')
        
        # Iterate through the TXT records returned
        for record in result:
            text_record = record.to_text()
            if text_record.startswith('"v=DMARC1'):
                return text_record.strip('"')
        return None  # No DMARC record found
    except dns.resolver.NoAnswer:
        print(f"No DMARC record found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except dns.resolver.Timeout:
        print(f"Query timed out for {domain}.")
    except Exception as e:
        print(f"Error occurred: {e}")
    return None

# Example usage for testing
if __name__ == "__main__":
    domain = 'example.com'
    dmarc_record = dmarc_check(domain)

    if dmarc_record:
        print(f"DMARC record for {domain}: {dmarc_record}")
    else:
        print(f"No DMARC record found for {domain}")
