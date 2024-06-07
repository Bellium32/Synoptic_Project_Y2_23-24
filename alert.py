import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['To'] = to

        user = "uea.synoptic.group77.2024@gmail.com"
        msg['From'] = user
        password = "tpxujjkbucjzhrzz"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    email_alert("Hey", "hello world", "2496881840@txt.bellmobility.com")
