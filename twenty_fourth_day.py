#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send email
def send_email():
    # Email configuration
    sender_email = 'your_email@gmail.com'  # Replace with your email
    receiver_email = 'receiver_email@gmail.com'  # Replace with receiver's email
    password = 'your_password'  # Replace with your email password

    # Email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Daily Challenge Reminder'

    body = 'Remember to tackle your daily challenge today!'

    message.attach(MIMEText(body, 'plain'))

    # Establishing a connection to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your email account
    server.login(sender_email, password)

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit the server
    server.quit()

# Schedule the email to be sent every day at a specific time (e.g., 8 AM)
schedule.every().day.at("08:00").do(send_email)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)