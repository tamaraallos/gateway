# Email Security Gateway

This project is a prototype of an Email Security Gateway, designed to protect an SMTP server by filtering and inspecting email traffic based on threat intelligence. Acting as a proxy, the gateway secures both inbound and outbound emails, protecting against phishing, spam, spoofing, and preventing the leakage of sensitive information.
Moreover, the gateway inspects incoming emails and checks for DKIM, DMARC and SPF checks and blocks any suspicious emails from reaching the user.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [Acknowledgements](#acknowledgements)



## Features
- **User-Friendly Command-Line Interface (CLI)** - This application includes an easy-to-use CLI designed to simplify interaction with the email security features.
- **Searchable Event and Email Logs** - provides comprehensive logging of all email events, allowing user to search logs by date, subject, sender, recipient, type, or action (e.g., block or allow). This feature aids in tracking and auditing email communications.
- **Sender Policy Framework (SPF), DKIM, and DMARC Verification** - ensures that incoming emails are verified through SPF, DKIM, and DMARC checks, protecting against email spoofing and ensuring email authenticity.
- **Data Loss Prevention (DLP)** - monitors outgoing emails for sensitive information and blocks or encrypts emails to prevent data leaks outside Bad Security Inc.
- **Protection against Phishing, Spam, and Spoofing** - filters and blocks phishing attempts, spam, and email spoofing through python scripts, ensuring that malicious emails do not reach the inbox.
- **Content Filtering** - prevents sensitive documents from being sent to unauthorised external recipients by analysing email content and applying policies to block or encrypt sensitive information.
- **Automatic Email Encryption** - encrypts outgoing emails that contain sensitive information to ensure secure communication.

## Installation

### Prerequisites
- List any prerequisites required before installation (e.g., software versions, dependencies).
- Example:
  ```bash
  # Install Watchdog
  pip install watchdog

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
  
### Usage
- Explain how to use the software. Can include examples and screenshots.
  

### Contribution


## Acknowledgements

We would like to express our gratitude to the following team members for their dedication and contributions to this project:

- **Bhuvan Virmani** - Project Manager
- **Tamara Allos** - UX Development Lead
- **Nelchael Kenshi Turija** - Backend Development Lead
- **Sai Veera Venkat Rahul Chagant** - Documentation Lead
- **Nehal Rahuja** - Quality Assurance (Testing) Lead
- **Saksham** - Communication Lead

A special thanks to our supervisor, **Jamie Ooi**, for their invaluable guidance and support throughout the project.

We would also like to acknowledge our clients, **Allen** and **Tom** from **Bad Security Inc.**, for providing us with this opportunity and for their trust in our work.


