import dns.resolver

# security protocol - verifies email senders by checking the DNS

def dmarc_check(sender):
    try:
        domain = sender.split('@', 1)[1] # gets domain
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
        return None

def is_dmarc_record(sender):
    dmarc_record = dmarc_check(sender)
    return dmarc_record is not None 


# examples to use for testing tempmail.net,... <-- these don't have a dmarc record