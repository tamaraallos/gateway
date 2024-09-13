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
- Install Python [Download & Install Python](https://www.python.org/downloads/)
  ```bash
  # Verify the installation
  $ python --version
  ```

- Install pip as it is required to install project dependencies
  ```bash
  # Download the get-pip.py file from bootstrap.pypa.io/get-pip.py.
  $ curl bootstrap.pypa.io/get-pip.py
  ```
  ```bash
  # Run the following command in Command Prompt from the directory where get-pip.py is downloaded:
  $ python get-pip.py
  ```
  ```bash
  # Verify the installation
  pip --version
  ```
  
- Install Git [Download & Install Git](https://git-scm.com/downloads). to clone the git repository or instead you can download the repository from [github](https://github.com/tamaraallos/gateway.git)
  ```bash
  # Verify the installation
  $ git --version
  ```
- Install Watchdog for file system handling
  ```bash
  # Install Watchdog
  $ pip install watchdog
  ```
- Install Cryptography
  ```bash
  # Install Cryptography
  $ pip install crytography
  ```
- Install Dnspython fir querying DNS records
  ```bash
  # Install DNS toolkit
  $ pip install dnspython
  ```
- Install Email

### Set up
1. **Clone the repo**:
2 continue...


### Usage
[THIS SECTION IS MAINLY ABOUT THE CLI]
- **Command 1:** 'Talk about how to use this command'


### more...



### Note - To All - From Tamara
You need to set up a .env if u want it to work

## New note - To All - From Tamara
You need to also add in a password for .env. I added a random password 'test'. It uses that to validate whatever the users input into the prompt. If correct they will proceed else try again.

### What needs to be done
1. Integrate peoples code within mine - I will help for that
2. I need to remove some of my test comments later
3. I need to move around some print statements for it a better

