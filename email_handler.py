from watchdog.events import FileSystemEventHandler
from email_processor import process_all_emails

# handles the event which is when a new email file is created
def on_created_email(event, email_dire, log_archive_path, log_email_processed_path):
    if event.is_directory: # edge case if event is for dire then ignore
        return 
    if event.src_path.endswith(".eml"): # only process .eml files
         #print(f"new mail detected: {event.src_path}") # testing purposes
        process_all_emails(email_dire, log_archive_path, log_email_processed_path)


# creates and return a file system event handler 
def create_event_handler(email_dire, log_archive_path, log_email_processed_path):
    # create a instance of FileSystemEventHandler
    handler = FileSystemEventHandler()
    # lambda function passes event and other parameters 
    handler.on_created = lambda event: on_created_email(event, email_dire, log_archive_path, log_email_processed_path)
    return handler

        
