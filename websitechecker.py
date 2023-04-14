# Chuma, Nepta and Dany's python script (Absolute Quantum)
# Supported by ChatGPT-3.
# This idea came from another script i've seen on the internet, ChatGPT-3 did most of the sketch.

#Library imports, MIME overall wasn't needed but it was needed so emails could have a body.
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
#This username and password will be tbe emails you will use to login as the "sentinel" or email sender.
SMTP_USERNAME = "smtpemail@gmail.com"  #Login Email
SMTP_PASSWORD = "----"  #Login gmail token (since gmail uses token rather than password)
#Since you can't login using password but a token, you need to provide google's password Token.
EMAIL_FROM = "emailfrom@gmail.com"
EMAIL_TO = "emailto@gmail.com"  #This is the email where you have to send the notification to.
EMAIL_SUBJECT = "Website Status Notification"


# Website configuration
URL = "https://www.pcgamer.com"
EXPECTED_STATUS_CODE = 200
EXPECTED_CONTENT = "THE GLOBAL AUTHORITY ON PC GAMES"

#We will use PCGamer as a test... We are expecting it to be code 200 so it works

# Check website status
response = requests.get(URL)
if response.status_code == EXPECTED_STATUS_CODE and EXPECTED_CONTENT in response.text:
    website_status = "up and running"
elif response.status_code == 404:
            website_status = "Page not found"
else:
    website_status = "Page Down"
#The Else was added to check other types of codes.


# Prepare email message
email_body = f"The website {URL} is {website_status}."
msg = MIMEMultipart()
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO
msg['Subject'] = EMAIL_SUBJECT
msg.attach(MIMEText(email_body, 'plain'))

# Send email
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SMTP_USERNAME, SMTP_PASSWORD)
server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
server.quit()

# Print status message
print("Email notification sent.")

#The next are other statuses but they would be a lot to work on so they are code left overs.

#statuses = {
#200: "Website Available",
#301: "Permanent Redirect",
#302: "Temporary Redirect",
#404: "Not Found",
#500: "Internal Server Error",
#503: "Service Unavailable"
#}