import os
import sys
import getpass

# ASCII logo for the BAD SECURITY ADMIN CONSOLE
def print_logo():
    logo = """
    ======================================
    ||     BAD SECURITY ADMIN CONSOLE    ||
    ======================================
    """
    print(logo)

# Function to check login credentials
def login():
    username = input("Enter user ID: ").strip()
    password = getpass.getpass("Enter password: ").strip()  # Hides the password input
    
    if username == "admin" and password == "admin":
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

# Function to run the email monitor script
def run_email_monitor():
    script_name = "email_monitor.py"
    if os.path.exists(script_name):
        print("\nStarting the email monitor system...\n")
        os.system(f"python {script_name}")
    else:
        print(f"{script_name} not found. Please ensure the script is in the same directory.")

def main():
    print_logo()
    if login():
        run_email_monitor()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
