import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("APP_PASSWORD")

if not my_email or not password:
    raise ValueError("Missing EMAIL_ADDRESS or APP_PASSWORD in .env file.")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(my_email, password)

print("--- CLI EMAIL CLIENT ---")
recipient = input("To: ")
subject = input("Subject: ")
body = input("Message:\n")

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = my_email
msg['To'] = recipient
msg.set_content(body)

print("\nConnecting to server...")
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() 
        server.login(my_email, password)  
        server.send_message(msg)
        
    print("✅ Email sent successfully!")
    
except Exception as e:
    print(f"Failed to send email. Error: {e}")
          
