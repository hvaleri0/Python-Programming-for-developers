from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

message = MIMEMultipart()  # create a message instance

message["from"] = "Hector Valerio"
message["to"] = "hector.valerio@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))  # attach the body to email
message.attach(
    MIMEImage(Path('big_thumb_7141e020ca8a473c1292c1702bd395f9.jpg').read_bytes()))  # return image file in bynary


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # first step to smtp protocal client and smtp start eith ehlo message
    smtp.starttls()  # start a transfer layer security connection
    smtp.login("hector.valerio@gmail.com",
               "juaeeytrrwdbgbho")  # email and password
    smtp.send_message(message)
    print("Sent....")
