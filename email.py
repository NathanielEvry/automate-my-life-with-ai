import imaplib
import email

def main():
    # Replace with your Gmail credentials
    username = "your_email@gmail.com"
    password = "your_password_or_app_specific_password"

    # Connect to Gmail over SSL
    gmail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    gmail.login(username, password)

    # Select the mailbox (label) you want to read from
    mailbox_label = "(INBOX)"  # Replace with the desired label
    gmail.select(mailbox_label)

    # Search for all emails (you can customize the search criteria)
    _, data = gmail.search(None, "ALL")
    email_ids = data[0].split()

    # Fetch email subjects and senders
    for email_id in email_ids:
        _, email_data = gmail.fetch(email_id, "(BODY[HEADER.FIELDS (SUBJECT FROM)])")
        email_message = email.message_from_bytes(email_data[0][1])
        subject = email_message["subject"]
        sender = email_message["from"]
        print(f"Email ID {email_id}: Subject: {subject}, From: {sender}")

    # Close the connection
    gmail.logout()

if __name__ == "__main__":
    main()
```

# Please replace `"your_email@gmail.com"` and `"your_password_or_app_specific_password"` with your actual Gmail credentials. You can also modify the `mailbox_label` to select a specific label (e.g., `"Sent"`, `"Drafts"`, etc.). This code connects to Gmail, retrieves email subjects and sender information, and prints them out.

# Feel free to explore more features of `imaplib` based on your requirements! 📧🐍