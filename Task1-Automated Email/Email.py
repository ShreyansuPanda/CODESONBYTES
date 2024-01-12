#CodesonBytes Task 1:Automated Email:- This is a project that automate email sending
from email.message import EmailMessage
import ssl
import smtplib

email_sender=/* Add the sender's email*/
email_password = /* Add app password from gmail*/
email_receiver=/*Add receiver's email*/

subject="CodesonBytes Task 1:Automated Email"
body="""
Test email sent to show that the code is working!
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        print("Email sent successfully!")
except Exception as e:
    print("Error",str(e))
