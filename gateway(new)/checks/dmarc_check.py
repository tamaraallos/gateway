import dns.resolver

def dmarc_check(domain):
    try:
        dmarc_domain = f"_dmarc.{domain}"
        result = dns.resolver.resolve(dmarc_domain, 'TXT')

        for record in result:
            text_record = record.to_text()
            if text_record.startswith('"v=DMARC1'):
                return text_record.strip('"')
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
