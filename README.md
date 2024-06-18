# Advanced Logistic Regression for Cybersecurity

This project implements an advanced logistic regression model to predict the likelihood of a user login being malicious based on various parameters. This model aims to enhance cybersecurity without relying solely on multi-factor authentication (MFA).

## Features

- Predicts potential malicious logins based on:
  - User ID
  - Login Time
  - Input Destination
  - End Destination
  - Device Type
  - Browser Type
  - Previous Login Success
  - Number of Failed Attempts
  - Account Age
  - Session Duration
  - User's Typical Login Time
  - IP Reputation Score
  - Geo-location Change
  - Unusual Activity Flag

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   
Navigate to the project directory:
bash
Copy code
cd your-repo

Create a virtual environment:
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:
bash

pip install -r requirements.txt
Usage



User ID
Login Time
Input Destination
End Destination
Device Type
Browser Type
Previous Login Success
Failed Attempts
Account Age
Session Duration
Typical Login Time
IP Reputation
Geo-location Change
Unusual Activity
Malicious
Run the script:

bash
Copy code
python script_name.py
