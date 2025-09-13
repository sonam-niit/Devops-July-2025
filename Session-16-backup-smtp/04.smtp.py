import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    send_email="<your_email_id>"
    receiver_email="sonam_skills@pw.live"
    password="<your_generated_app_password>"
    # google account : manage account
    # search for app-password
    # generate password and use it here
    msg=MIMEText(body) 
    msg["subject"]=subject
    msg["from"]=send_email
    msg["to"]=receiver_email
    
    # filename="app.log"
    # with open(filename,'rb') as attachment:
        
    
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() # encrypt the connection
        server.login(send_email,password)
        server.send_message(msg)
        print("Message sent successfully!")
        
send_email("BackUp Completed","Backup Created Successfully!")