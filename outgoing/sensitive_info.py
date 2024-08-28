import os
import re
import logging
from email.parser import BytesParser
from email.policy import default
import shutil
import subprocess
import PyPDF2
import docx

# Setup logging
log_dir = "logging"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'email_sensitivity.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SENSITIVE_PATTERNS = {
    'Tax File Number': r'\b\d{3}-\d{3}-\d{3}\b',
    'Credit Card Number': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
    'Balance Sheet': r'\b(balance\s*sheet)\b',
    'Confidential Plan': r'\b(confidential|plan)\b',
}

def extract_content(msg):
    content = []
    if msg.is_multipart():
        for part in msg.iter_parts():
            content_type = part.get_content_type()
            disposition = part.get_content_disposition()
            if disposition is None:  # Not an attachment
                try:
                    if content_type in ['text/plain', 'text/html']:
                        charset = part.get_content_charset() or 'utf-8'
                        payload = part.get_payload(decode=True).decode(charset)
                        content.append(payload)
                except Exception as e:
                    logging.warning(f"Failed to decode part of type {content_type}: {e}")
            elif disposition and disposition.startswith('attachment'):  # It's an attachment
                content.append(scan_attachment(part))
    else:
        try:
            charset = msg.get_content_charset() or 'utf-8'
            payload = msg.get_payload(decode=True).decode(charset)
            content.append(payload)
        except Exception as e:
            logging.warning(f"Failed to decode email content: {e}")
    
    return "\n".join(content) if content else ""

def scan_attachment(part):
    attachment_content = ""
    filename = part.get_filename()
    if filename:
        if filename.endswith('.pdf'):
            attachment_content = extract_pdf_content(part)
        elif filename.endswith('.docx'):
            attachment_content = extract_docx_content(part)
        elif filename.endswith('.txt') or filename.endswith('.html'):
            try:
                charset = part.get_content_charset() or 'utf-8'
                attachment_content = part.get_payload(decode=True).decode(charset)
            except Exception as e:
                logging.warning(f"Failed to decode text-based attachment {filename}: {e}")
    
    if attachment_content:
        logging.info(f"Scanned attachment {filename}")
    
    return attachment_content

def extract_pdf_content(part):
    content = ""
    try:
        pdf_reader = PyPDF2.PdfFileReader(part.get_payload(decode=True))
        for page in range(pdf_reader.getNumPages()):
            content += pdf_reader.getPage(page).extract_text()
    except Exception as e:
        logging.warning(f"Failed to extract text from PDF: {e}")
    return content

def extract_docx_content(part):
    content = ""
    try:
        doc = docx.Document(part.get_payload(decode=True))
        for para in doc.paragraphs:
            content += para.text + "\n"
    except Exception as e:
        logging.warning(f"Failed to extract text from DOCX: {e}")
    return content

def check_sensitive_data(content, patterns):
    detected = []
    for data_type, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            logging.info(f"Detected {data_type} in the content!")
            detected.append(data_type)
    return detected

def move_to_approval_folder(eml_file):
    approval_folder = os.path.join(os.path.dirname(eml_file), "Approval needed")
    if not os.path.exists(approval_folder):
        os.makedirs(approval_folder)
    
    destination = os.path.join(approval_folder, os.path.basename(eml_file))
    shutil.move(eml_file, destination)
    logging.info(f"Moved file to {approval_folder}")

def check_email_sensitivity(eml_file, patterns):
    try:
        with open(eml_file, 'rb') as f:
            msg = BytesParser(policy=default).parse(f)
    except FileNotFoundError:
        logging.error(f"File not found: {eml_file}")
        return "Error: Email file not found."
    except Exception as e:
        logging.error(f"Failed to parse email: {e}")
        return "Error: Failed to parse email."

    content = extract_content(msg)
    detected_sensitive_data = check_sensitive_data(content, patterns)

    if detected_sensitive_data:
        print(f"Unsafe: Sensitive data detected - {', '.join(detected_sensitive_data)}")
        approval = input("Email needs approval. Type 'yes' to approve and encrypt, 'no' to move to 'Approval needed': ").strip().lower()
        if approval == 'yes':
            # Call the encryption script
            subprocess.run(['python', 'encryption.py', eml_file])
            print(f"Email {eml_file} encrypted and sent.")
        else:
            move_to_approval_folder(eml_file)
            print("Email moved to 'Approval needed'.")
    else:
        # Safe emails will also be encrypted and sent
        subprocess.run(['python', 'encryption.py', eml_file])
        print(f"Email {eml_file} encrypted and sent.")
    
    logging.info(f"Result for {eml_file}: {'Safe' if not detected_sensitive_data else 'Unsafe'}")
    return

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sensitive_info.py <path_to_eml_file>")
        sys.exit(1)

    eml_file = sys.argv[1]
    check_email_sensitivity(eml_file, SENSITIVE_PATTERNS)