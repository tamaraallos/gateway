# Email Security Gateway

This project is a prototype of an Email Security Gateway, designed to protect an SMTP server by filtering and inspecting email traffic based on threat intelligence. Acting as a proxy, the gateway secures both inbound and outbound emails, protecting against phishing, spam, spoofing, and preventing the leakage of sensitive information.
Moreover, the gateway inspects incoming emails and checks for DKIM, DMARC and SPF checks and blocks any suspicious emails from reaching the user.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Acknowledgements](#acknowledgements)


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

### Configurations

#### Step 1: Clone the Repository
- Start by cloning the repository to your local machine. You can do this by running the following command in your terminal:

  ```bash
  git clone https://github.com/yourusername/gateway.git
  
- Make sure to replace the placeholder with your actual username
#### Step 2: Set Up Environment Variables
- After cloning the repository, navigate to the project directory:

  ```bash
  cd gateway
- You will need to set up a .env file to store your environment variables. This file will contain sensitive information such as directory paths and passwords, so make sure to keep it secure.

- Create a .env file in the root directory of the project and add the following environment variables:


  ```bash
  ROOT_DIR=/path/to/your/root/directory
  EMAIL_FOLDER=/path/to/your/email/folder
  LOG_PATH=/path/to/log/files
  LOG_EMAIL_ARCHIVE=/path/to/email/archive
  LOG_EMAIL_PROCESSED=/path/to/processed/emails
  PASSWORD=yourpasswordhere

  Configuration Details:
  
  ROOT_DIR: The root directory where your project is located.
  EMAIL_FOLDER: The directory where incoming emails are stored.
  LOG_PATH: The directory where log files will be saved.
  LOG_EMAIL_ARCHIVE: The directory where archived emails will be stored.
  LOG_EMAIL_PROCESSED: The directory for storing processed emails.
  PASSWORD: The password for using the gateway.
- Make sure to replace the placeholder paths and values with your actual directory paths and a secure password.

#### Step 3: Additional Configuration
- Ensure that the directories you specify in the .env file are correctly set up and have the necessary read/write permissions.


## Usage
This script allows you to interact with email logs, view, search, and process them using a command-line interface (CLI). On running the script, you will be prompted to enter your username and password for authentication. After logging in, you will see a menu with four options. The four options are as follows:
- **Command 1:** This allows the user to view the email logs.
- **Command 2:** This allows the user to search through the email logs.
This would then ask the user for 8 different options. 1 is to search for a specific string.
2 is to search for a specific date. 3 is to search for a keyword in the email's subject.
4 is to search for the sender's email address. 5 is to search for the receiver's email address. 6 is to search for a type of email that fails the check e.g. phishing or spam. 7 is to search for an action status such as blocked or allowed. And lastly, 8 returns back to the homepage.
- **Command 3:** This allows the user to see the processed emails by name.
- **Command 4:** This allows the user to exit the program.

## Additional Script: createEML.py
This is an additional feature added outside of the POC. It is a script that generates emails for testing or demonstration purposes. It allows users to create customisable emails, which can be sued for testing different parts of the email security gateway solution. Features include:
- Customisable email fields such as sender, recipient, subject, action status, email type and body.
- Provides easy way to simulate a real-world email data. <br>
**To Use**
1. Have a .env set up and specify where you want the emails saved.
2. Run the script using python in terminal: 
  ```python createEML.py```

## Acknowledgements

We would like to express our gratitude to the following team members for their dedication and contributions to this project:

- **Tamara Allos**
- **Bhuvan Virmani** 
- **Nelchael Kenshi Turija** 
- **Sai Veera Venkat Rahul Chagant** 
- **Nehal Rahuja** 
- **Saksham**

A special thanks to our supervisor, **Jamie Ooi**, for their invaluable guidance and support throughout the project.

We would also like to acknowledge our clients, **Allen** and **Tom** from **Bad Security Inc.**, for providing us with this opportunity and for their trust in our work.
