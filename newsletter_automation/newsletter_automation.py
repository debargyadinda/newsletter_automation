import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Loading recipient data (email IDs and locations)
def load_recipient_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if 'Email' not in data.columns or 'Location' not in data.columns:
            raise ValueError("CSV file must contain 'Email' and 'Location' columns.")
        return data
    except Exception as e:
        print(f"Error loading recipient data: {e}")
        exit()

# Filtering recipients based on location
def filter_recipients_by_location(data, location):
    """
    Filter recipients based on the given location.
    """
    return data[data['Location'] == location]

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Send an email to the recipient.
    """
    try:
        # SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade to secure connection
        server.login(sender_email, sender_password)

        # Create the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Newsletter sent to {recipient_email}")

        
        server.quit()

    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")


def main():
    
    file_path = 'recipients.csv'  

    sender_email = 'senders_email@gmail.com'  
    sender_password = 'senders_password'      

    """If we are using gmail, 
    we can generate a password by enabling App password in gmail
    we can also use environment variables for security"""
    # Newsletter details
    subject = 'Monthly Newsletter'
    body = """
    Hello,

    Here is your monthly newsletter! Stay updated with the latest news and updates.

    Regards,
    Newsletter Team
    """

    # Load recipient data
    data = load_recipient_data(file_path)

    # Get user-specified location for sending emails
    location = input("Enter the location for which to send newsletters: ").strip()

    # Filter recipients by location
    filtered_recipients = filter_recipients_by_location(data, location)

    if filtered_recipients.empty:
        print(f"No recipients found for location: {location}")
        return

    # Send the newsletter to filtered recipients
    for _, recipient in filtered_recipients.iterrows():
        send_email(sender_email, sender_password, recipient['Email'], subject, body)

# Run the script
if __name__ == '__main__':
    main()
