import shutil
import os
import subprocess
import re
import smtplib
from email.mime.text import MIMEText


# Step 1: Backup files using shutil
def backup_files(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    shutil.copytree(source_dir, backup_dir, dirs_exist_ok=True)  # prevents error if folder exists
    print(f"Backup completed from {source_dir} to {backup_dir}")


# Step 2: Execute a system command using subprocess
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Command output: {result.stdout}")
    return result


# Step 3: Parse logs using re
def parse_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    error_lines = [line for line in logs if re.search(r'ERROR', line)]
    return error_lines


# Step 4: Send notification email using smtplib
def send_notification(subject, body, recipient_email):
    sender_email = "your_email@example.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'your_password') #App Password
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Notification sent.")


# Example usage
if __name__ == "__main__":
    # Backup operation
    backup_files('D://PhysicsWalla/Devops-July/Session-16-backup-smtp',
                 'D://PhysicsWalla/Devops-July/backup')

    # Run a system command
    run_command('ls -la')

    # Parse log file for errors
    errors = parse_logs('D://PhysicsWalla/Devops-July/Session-16-backup-smtp/app.log')
    if errors:
        send_notification("Log Errors Detected", "\n".join(errors), "recipient@example.com")
        print("Error Mail Send successfully!")
