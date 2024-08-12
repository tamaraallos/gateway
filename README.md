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
