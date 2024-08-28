
from dlp_patterns import check_dlp, DLP_PATTERNS
import os;

EMAIL_FOLDER_PATH = 'D:\EmailSecurity-main\EmailSecurity-main\emails'#path/to/email/folder

def dlp_check_emails(email_folder_path, dlp_patterns):
    """Check all parsed emails for DLP violations."""
    results = []
    for filename in os.listdir(email_folder_path):
        if filename.lower().endswith('.eml'):
            file_path = os.path.join(email_folder_path, filename)
            if os.path.isfile(file_path):
                # IMP: Call your custom email parsing function here
                email_content = your_email_parsing_function(file_path)
                findings = check_dlp(email_content, dlp_patterns)
                if findings:
                    results.append((filename, findings))
    return results


def main():
    # Perform DLP checks on parsed emails in the specified folder
    dlp_results = dlp_check_emails(EMAIL_FOLDER_PATH, DLP_PATTERNS)

    # Display results
    if dlp_results:
        print("DLP violations found in the following emails:")
        for email, findings in dlp_results:
            print(f"Email: {email}")
            for pattern, matches in findings.items():
                print(f"  {pattern}: {', '.join(matches)}")
    else:
        print("No DLP violations found.")

if __name__ == "__main__":
    main()
