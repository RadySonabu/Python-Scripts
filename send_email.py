import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = 'user@gmail.com'
EMAIL_PASSWORD = '<password>'
contacts = ['user2@gmail.com', 'user3@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'This should be a pdf'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

files = ['something.html'] #folder directory

for file in files:
	with open(file, 'rb') as f:
		file_data = f.read()
		file_name = f.name

	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
