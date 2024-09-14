For the people working on the README below is a template you can follow.
Make it look better, and go into depth

# Project Title
## Description
- Description of project, purpose and it's aim, mention client

## Features
- **User-Friendly Command-Line Interface (CLI)** - This application includes an easy-to-use CLI designed to simplify interaction with the email security features.
- **Searchable Event and Email Logs** - provides comprehensive logging of all email events, allowing user to search logs by date, subject, sender, recipient, type, or action (e.g., block or allow). This feature aids in tracking and auditing email communications.
- **Sender Policy Framework (SPF), DKIM, and DMARC Verification** - ensures that incoming emails are verified through SPF, DKIM, and DMARC checks, protecting against email spoofing and ensuring email authenticity.
- **Data Loss Prevention (DLP)** - monitors outgoing emails for sensitive information and blocks or encrypts emails to prevent data leaks outside Bad Security Inc.
- **Protection against Phishing, Spam, and Spoofing** - filters and blocks phishing attempts, spam, and email spoofing through python scripts, ensuring that malicious emails do not reach the inbox.
- **Content Filtering** - prevents sensitive documents from being sent to unauthorised external recipients by analysing email content and applying policies to block or encrypt sensitive information.
- **Automatic Email Encryption** - encrypts outgoing emails that contain sensitive information to ensure secure communication.

## Installation
does anything need to be set up,
e.g vsc, downloading the libraries we used
(look through the files and u can see which ones we need)

### Prerequisites
Make sure that you have all of the pre-requisites installed on your development machine
1. Install Python [Download & Install Python](https://www.python.org/downloads/)
   Verify the installation
  ```bash
  $ python --version
  ```

2. Install pip as it is required to install project dependencies
   Download the get-pip.py file from bootstrap.pypa.io/get-pip.py.
   ```bash
   $ curl bootstrap.pypa.io/get-pip.py
   ```
   Run the following command in Command Prompt from the directory where get-pip.py is downloaded:
   ```bash
   $ python get-pip.py
   ```
   Verify the installation
   ```bash
   $ pip --version
   ```

3. Install Git [Download & Install Git](https://git-scm.com/downloads). to clone the git repository or instead you can download the repository from [github](https://github.com/tamaraallos/gateway.git)
  Verify the installation
  ```bash
  $ git --version
  ```

4. Install Python Modules
  - Install dotenv module for environment variables
    ```bash
    $ pip install python-dotenv
    ```
  - Install Watchdog for file system handling
    ```bash
    $ pip install watchdog
    ```
  - Install Cryptography for email encryption
    ```bash
    $ pip install crytography
    ```    
  - Install SPF for Sender Policy Framework
    ```bash
    $ pip install pyspf
    ```
  - Install DKIM for DomainKeys Identified Mail
    ```bash
    $ pip install dkimpy
    ```
  - Install Dnspython for querying DNS records
    ```bash
    $ pip install dnspython
    ```

### Set up
1. **Clone the repo**:
2 continue...


### Usage
This script allows you to interact with email logs, view, search, and process them using a command-line interface (CLI). On running the script, you will be prompted to enter your username and password for authentication. After logging in, you will see a menu with four options. The four options are as follows:
- **Command 1:** This allows the user to view the email logs
- **Command 2:** This allows the user to search through the email logs.
This would then ask the user for 8 different options. 1 is to search for a specific string.
2 is to search for a specific date. 3 is to search for a keyword in the email's subject.
4 is to search for the sender's email address. 5 is to search for the receiver's email address. 6 is to search for a type of email that fails the check e.g. phishing or spam. 7 is to search for an action status such as blocked or allowed. And lastly, 8 returns back to the homepage.
- **Command 3:** This allows the user to see the processed emails by name.
- **Command 4:** This allows the user to exit the program.



### Note - To All - From Tamara
You need to set up a .env if u want it to work

## New note - To All - From Tamara
You need to also add in a password for .env. I added a random password 'test'. It uses that to validate whatever the users input into the prompt. If correct they will proceed else try again.

### What needs to be done
1. Integrate peoples code within mine - I will help for that
2. I need to remove some of my test comments later
3. I need to move around some print statements for it a better

