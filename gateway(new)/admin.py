import os
import subprocess
import sys
import time

# Directories
EMAILS_DIR = "emails"
APPROVED_DIR = "approved"
DECLINED_DIR = "declined"
LOGS_DIR = "logging"
KEYWORDS_DIR = "keywords"
CHECKS_DIR = "checks"

# Main menu
def main_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Check Emails")
        print("2. View Logs")
        print("3. View Approved Emails")
        print("4. View Declined Emails")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            check_emails()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            view_approved_emails()
        elif choice == "4":
            view_declined_emails()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

# Check emails in the "emails" folder
def check_emails():
    email_files = os.listdir(EMAILS_DIR)
    if not email_files:
        print("No emails to check.")
        return

    for idx, email_file in enumerate(email_files, start=1):
        print(f"{idx}. {email_file}")

    choice = input("Select an email to check (or 'q' to quit): ").strip()

    if choice.lower() == 'q':
        return

    try:
        choice = int(choice) - 1
        if choice < 0 or choice >= len(email_files):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_email = email_files[choice]
    email_path = os.path.join(EMAILS_DIR, selected_email)

    perform_checks(email_path)

# Perform checks on a selected email
def perform_checks(email_path):
    while True:
        print("\nSelect a check to perform:")
        print("1. DKIM Check")
        print("2. SPF Check")
        print("3. DMARC Check")
        print("4. DLP Check")
        print("5. Phishing Check")
        print("6. Spam Check")
        print("7. Approve Email")
        print("8. Decline Email")
        print("9. Go back to the previous menu")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "DKIM_check.py"), email_path])
        elif choice == "2":
            subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "spf_check.py"), email_path])
        elif choice == "3":
            subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "dmarc_check.py"), email_path])
        elif choice == "4":
            subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "sensitive_info.py"), email_path])
        elif choice == "5":
            subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "phishingtest.py"), email_path])
        elif choice == "6":
            subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "spamtest.py"), email_path])
        elif choice == "7":
            approve_email(email_path)
            break
        elif choice == "8":
            decline_email(email_path)
            break
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select again.")

# Approve an email
def approve_email(email_path):
    email_file = os.path.basename(email_path)
    new_path = os.path.join(APPROVED_DIR, email_file)
    os.rename(email_path, new_path)
    print(f"Email {email_file} approved and moved to {APPROVED_DIR}.")
    log_action("Approved", email_path)

# Decline an email
def decline_email(email_path):
    email_file = os.path.basename(email_path)
    new_path = os.path.join(DECLINED_DIR, email_file)
    os.rename(email_path, new_path)
    print(f"Email {email_file} declined and moved to {DECLINED_DIR}.")
    log_action("Declined", email_path)

# View approved emails
def view_approved_emails():
    approved_files = os.listdir(APPROVED_DIR)
    if not approved_files:
        print("No approved emails.")
        return

    print("\nApproved Emails:")
    for email_file in approved_files:
        print(email_file)

# View declined emails
def view_declined_emails():
    declined_files = os.listdir(DECLINED_DIR)
    if not declined_files:
        print("No declined emails.")
        return

    print("\nDeclined Emails:")
    for email_file in declined_files:
        print(email_file)

# Log actions
def log_action(action, email_path):
    with open(os.path.join(LOGS_DIR, "email_logs.log"), 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action}: {email_path}\n")

# View logs
def view_logs():
    subprocess.run([sys.executable, os.path.join(CHECKS_DIR, "view_logs.py")])

if __name__ == "__main__":
    main_menu()
