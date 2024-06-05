import smtplib
from email.message import EmailMessage

def email_alert(subject,body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "ashishjoseph552@gmail.com"
    password = ""

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)

    server.quit()

    if __name__ == '__main__':
        email_alert("hey", "ash", "ashishJsoeph553@gmail.com")
