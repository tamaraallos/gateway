import dkim
# DomainKey Identified Mail
# Email authetnication method - uses digital signature

def dkim_check(file_path):
    try:
        # open and read email file
        with open(file_path, 'rb') as file:
            email_content = file.read()
        # verify DKIM signature
        result = dkim.verify(email_content)
        return result
    except Exception as e:
        print(f"Error occured: {e}")
        return False
