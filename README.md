# gateway
For Bad Security Inc (BSI) - Proof of Concept

# Day 1 - Tamara Allos
1. Created an Email Parser
2. Write emails into a .log file
3. Search through .log file with a any string
4. Generate script for creating .eml emails

# day 2 - Tamara Allos
1. Updated the email generator. This is so it follows a consistent naming convention (emailN - n being number of emails already created)
2. Updated email_parser file:
   - Changed email_parser name to email_processor
   - removed the search_log
   - Added additional functionalities for automation. This includes:
        -  processed_email_storage: Stores *email name* to a different log file
        - load_emails_processed: loads emails that have been processed and adds them to a set (allows   no dupes)
        - process_all_emails: function that calls new functions created. Logs emails only if haven't already
3. Moved search_log function into a seperate file called log_search.py
4. Created a main.py
    - This is where I will be calling the functions and building the CLI
    - I created a .env file where I store my path names. (used in main)
5. Generated new emails, deleted old emails stored in the email folder.
6. Created two new log files (one for email archives and another storing emails names)
7. Created a Checks folder (I will upload my dkim, dmarc, and spf check files later)
8. Uploaded the dmarc_check file and refactored the code partially.