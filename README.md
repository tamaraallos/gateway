# gateway
For Bad Security Inc (BSI) - Proof of Concept

# Week 1- Tamara Allos
1. Created an Email Parser
2. Write emails into a .log file
3. Search through .log file with a any string
4. Generate script for creating .eml emails

# Week 2 - Tamara Allos
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


# Week 3 - Tamara Allos
1. Uploaded DKIM check
2. Added spf_check
3. Forgot to document the rest

# Week 4 - Tamara Allos
1. Uploaded DKIM check
2. Added spf_check

# Week 3 - 5 Changes - Tamara Allos
1. Worked on refactoring a lot of the code:
    - email generator (createEML.py script I created)
    - Email parser
    - Main - add a CLI for users
    - Log search made more complex
    - added ASCII art
    - email handler - listens in a folder for new emails

# Week 3 - 5 Changes - Bhuvan Virmani

Created a DLP check script that reads all .eml files in a directory and scans them for any sensitive information regex. 
The function is called from a main file after the code is executed it outputs the sensitive information and the file name where it was found. 

### Note - To All - From Tamara
You need to set up a .env if u want it to work

## New note - To All - From Tamara
You need to also add in a password for .env. I added a random password 'test'. It uses that to validate whatever the users input into the prompt. If correct they will proceed else try again.

### What needs to be done
1. Integrate peoples code within mine - I will help for that
2. I need to remove some of my test comments later
3. I need to move around some print statements for it a better

