#CodesonBytes Task 1:Automated Email:- This is a project that automate email sending
from email.message import EmailMessage
import ssl
import smtplib
import pandas as pd

email_sender="eziomorningstar123@gmail.com"
password=r"E:\programming\Python\CodesonBytes\Task 1-Automated Email\PASSWORD.txt"

#For the email of receivers we are importing the data from an Excel file, Update the path of Excel as required
excel_file_path=r"E:\programming\Python\CodesonBytes\Task 1-Automated Email\Email Receivers.xlsx"


subject="CodesonBytes Task 1:Automated Email"
body="""
Hello, This is a Test email sent to show that the code for automated email is working!
"""

with open(password, 'r') as password:
        email_password = password.read().strip()

df = pd.read_excel(excel_file_path)
email_receiver= df['Email'].tolist()

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
