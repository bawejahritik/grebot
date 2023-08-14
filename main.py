from email.message import EmailMessage
import ssl
import smtplib
import pandas as pd
import random
import os


email_sender = 'hritikbaweja2@gmail.com'
email_password = 'qktslijdhvpmyuzs'
email_receiver = 'shrianshchaabra@gmail.com'

subject = "Todays List of 10 Words"

df = pd.read_csv('temp.csv')

size_of_df = len(df)

numbers = []

while len(numbers) < 10:
	x = random.randint(0, size_of_df)
	if x not in numbers:
		numbers.append(x)

words = []
mailbody = ""
for num in numbers:
	mailbody += df.loc[[num]]['word'].values[0]
	mailbody += " ----- "
	mailbody += df.loc[[num]]['definition'].values[0]
	mailbody += '\n \n'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(mailbody)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())