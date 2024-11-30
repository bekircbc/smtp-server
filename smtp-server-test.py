import smtplib

# Define SMTP server and port
SMTP_SERVER = "localhost"
SMTP_PORT = 1025

# Send a test email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.sendmail(
            "from@example.com",
            "to@example.com",
            "Subject: Test Email\n\nThis is a test email from the SMTP server."
        )
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
