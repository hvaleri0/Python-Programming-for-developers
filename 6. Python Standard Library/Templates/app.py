from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# read html & convert template to string
template = Template(Path("template.html").read_text())

message = MIMEMultipart()

message["from"] = "Hector Valerio"
message["to"] = "hector.valerio@gmail.com"
message["subject"] = "This is a test"

# substitute variables in Html
body = template.substitute({"name": "Hector"})  # dictionary with all varibles
# Alternatively you can pass a keyword argument
body = template.substitute(name="Hector")

message.attach(MIMEText(body, "html"))
message.attach(
    MIMEImage(Path('big_thumb_7141e020ca8a473c1292c1702bd395f9.jpg').read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("hector.valerio@gmail.com",
               "juaeeytrrwdbgbho")
    smtp.send_message(message)
    print("Sent....")
