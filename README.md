# Newsletter Automation Script

This Python script automates the process of sending newsletters to recipients based on their location. It reads recipient data from a CSV file, filters them by the specified location, and sends newsletters using Gmail's SMTP server.

---

## Features
- **CSV-Based Recipient Management**: Loads recipient data from a CSV file containing `Email` and `Location` columns.
- **Location-Based Filtering**: Sends newsletters only to recipients from a specific location.
- **Automated Email Sending**: Uses Gmail's SMTP server for sending emails.
- **Security Recommendation**: Environment variables can be used to store email credentials for enhanced security.

---

## Prerequisites
- Python 3.x installed on your system.
- Required Python libraries: `smtplib`, `pandas`, `email`.

---

## How to Use

### 1. Enable App Password for Gmail
To use Gmail for sending emails, you need to enable **App Passwords**:
1. Go to your [Google Account Security Settings]
2. Enable **2-Step Verification**.
3. Under "Sign-in & security," select **App Passwords**.
4. Generate a password for "Mail" and "Computer" (or a device of your choice).
5. Use this password in the script instead of your regular email password.

---

### 2. Prepare the CSV File
Create a CSV file named `recipients.csv` with the following format:
```csv
Email,Location
user1@example.com,India
user2@example.com,Japan


---

## Run the Script

1. Place the script and `recipients.csv` file in the same directory.
2. Update the script with your email credentials.

### Run the file

```bash
python3 newsletter_automation.py



run the script
python3 newsletter_automation.py

