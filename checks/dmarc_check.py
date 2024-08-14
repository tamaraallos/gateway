import dns.resolver

# security protocol - verifies email senders by checking the DNS
# note: I probably need to make changes later

def dmarc_check(domain):
    try:
        # query the dns for dmarc record
        dmarc_domain = f"_dmarc.{domain}" # creates dmarc domain name. e.g _dmarc.gmail.com
        result = dns.resolver.resolve(dmarc_domain, 'TXT') # this queries txt records for the dmarc domaiin

        # iterates through the records returned from result 
        for record in result:
            text_record = record.to_text() # converts record to text
            if text_record.startswith('"v=DMARC1'): 
                return text_record.strip('"')
            return None
    except Exception as e:
        print(f"Error occured: {e}")
        return None


# My example for testing 
domain = 'sdfdsds.com'
dmarc_record = dmarc_check(domain)

if dmarc_record:
    print(f"dmarc record for {domain}: {dmarc_record}")
else:
    print(f"No dmarc record found for {domain}")

## resource: https://www.thierolf.org/posts/small-python-script-to-quick-test-dmarc-dkim-and-spf-records/