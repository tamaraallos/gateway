import os

# Function to view and search logs in the logging folder.
def view_logs():
    log_file_path = "logging/email_logs.log"
    archive_log_path = "logging/email_archives.log"

    while True:
        print("\nLog Viewing Options:")
        print("1. View Email Check Logs")
        print("2. View Email Archive Logs")
        print("3. Search Logs")
        print("4. Go back to the previous menu")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            view_log_content(log_file_path)
        elif choice == "2":
            view_log_content(archive_log_path)
        elif choice == "3":
            search_logs(log_file_path, archive_log_path)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select again.")

def view_log_content(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print("\nLog Content:\n")
            print(file.read())
    else:
        print(f"Error: Log file {file_path} does not exist.")

def search_logs(check_log_file, archive_log_file):
    search_term = input("Enter the search term: ").strip().lower()
    found = False

    def search_in_file(file_path):
        nonlocal found
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    if search_term in line.lower():
                        print(line.strip())
                        found = True

    print("\nSearch Results:")
    search_in_file(check_log_file)
    search_in_file(archive_log_file)

    if not found:
        print("No matching logs found.")

# Example usage (should be invoked in admin.py):
# view_logs()
