# Email Security Gateway

This project is a prototype of an Email Security Gateway, designed to protect an SMTP server by filtering and inspecting email traffic based on threat intelligence. Acting as a proxy, the gateway secures both inbound and outbound emails, protecting against phishing, spam, spoofing, and preventing the leakage of sensitive information.
Moreover, the gateway inspects incoming emails and checks for DKIM, DMARC and SPF checks and blocks any suspicious emails from reaching the user.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Contributing](#contributing)
4. [Acknowledgements](#acknowledgements)

## Features

- List the key features and functions of the software.
  
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
  




## Acknowledgements

- thank anyone for their contribution here
