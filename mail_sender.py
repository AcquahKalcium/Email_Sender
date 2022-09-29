from email.message import EmailMessage
import ssl
import smtplib

mail_sender = 'kalcium3@gmail.com'
mail_password = 'xhgpkdtdppdzmhew'

email_reciever ='jnxuire639@tormails.com'

subject ='dont forget to subscribe'
body = """
when you watch a video,please hit subscribe
"""

em = EmailMessage()
em['From'] = mail_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(mail_sender, mail_password)
    smtp.sendmail(mail_sender, email_reciever, em.as_string())














#xhgpkdtdppdzmhew