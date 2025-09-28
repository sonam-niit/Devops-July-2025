# Configure Email Integartion with Jenkins

- setting in jenkins --> click on system --> Scroll down a bit
- Email notification
- smtp server- smtp.gmail.com
- click on Advanced:
- SMTP Authentication check - add user name and app password
- check on SSL and the port: 465
- click on Test Configuration by sending an email and check email received or not
- if verification done then created project

# Build Project

- create simple free style project
- add description
- build step - execute shell - type exit 1 (this will fail your job)
- post build action - select email notification - click on both check boxes
- build job
- when build fails your job will send you a failed job email.
