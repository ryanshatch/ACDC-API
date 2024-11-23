#* Version 4.0
#* Description: This is a simple API that searches for inmates in the Aiken County Sheriff's Office system.
#* The API accepts a POST request with a JSON payload containing a list of inmates to search for.
#  The main reason for this is to check if certain people I know are or are not in jail.
#  Removed Twilio Alerts.

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Aiken County Inmate search URL
AIKEN_URL = 'https://aikencountysheriff.net/inmate-search/'

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Inmate Search API. Use /check-inmate to search for inmates.'}), 200

@app.route('/check-inmate', methods=['POST'])
def check_inmate():
    data = request.json
    inmates = data.get('inmates', [])

    found_inmates = []

    for inmate in inmates:
        response = requests.post(AIKEN_URL, data=inmate)

        if response.status_code == 200:
            if 'No records found' not in response.text:
                found_inmates.append(inmate)

    if found_inmates:
        return jsonify({'status': 'Inmates found', 'found_inmates': found_inmates}), 200
    else:
        return jsonify({'status': 'No inmates found'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


#* Version Three adding Dalton

# from flask import Flask, request, jsonify
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from twilio.rest import Client

# app = Flask(__name__)

# # Twilio configuration
# TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
# TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
# TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# # Email configuration
# SMTP_SERVER = 'smtp.example.com'
# SMTP_PORT = 587
# EMAIL_USER = 'your_email@example.com'
# EMAIL_PASS = 'your_email_password'

# # Aiken County Inmate search URL
# AIKEN_URL = 'https://aikencountysheriff.net/inmate-search'

# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({'message': 'Welcome to the Inmate Search API. Use /check-inmate to see if Dalton Jones and the babies sperm donor are still locked up.'}), 200

# @app.route('/check-inmate', methods=['POST'])
# def check_inmate():
#     data = request.json
#     alert_email = data.get('alert_email')
#     alert_phone = data.get('alert_phone')

#     inmates = [
#         {'firstName': 'Foster', 'lastName': 'Fech'},
#         {'firstName': 'Dalton', 'lastName': 'Jones'}
#     ]

#     found_inmates = []

#     for inmate in inmates:
#         response = requests.post(AIKEN_URL, data=inmate)

#         if response.status_code == 200:
#             inmate_found = 'No records found' not in response.text

#             if inmate_found:
#                 found_inmates.append(inmate)
#                 message = f"Inmate {inmate['firstName']} {inmate['lastName']} has been located in the Aiken County system."
#                 if alert_email:
#                     send_email_alert(alert_email, message)
#                 if alert_phone:
#                     send_sms_alert(alert_phone, message)

#     if found_inmates:
#         return jsonify({'status': 'Inmates found., ', 'found_inmates': found_inmates}), 200
#     else:
#         return jsonify({'status': 'No inmates found'}), 200

# def send_email_alert(to_email, message):
#     msg = MIMEText(message)
#     msg['Subject'] = 'Inmate Search Alert'
#     msg['From'] = EMAIL_USER
#     msg['To'] = to_email

#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(EMAIL_USER, EMAIL_PASS)
#             server.sendmail(EMAIL_USER, to_email, msg.as_string())
#     except Exception as e:
#         print(f'Failed to send email: {e}')

# def send_sms_alert(to_phone, message):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#     try:
#         client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE_NUMBER,
#             to=to_phone
#         )
#     except Exception as e:
#         print(f'Failed to send SMS: {e}')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)


## VERSION 2.0

# from flask import Flask, request, jsonify
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from twilio.rest import Client
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# # Twilio configuration
# TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
# TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
# TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# # Email configuration
# SMTP_SERVER = 'smtp.example.com'
# SMTP_PORT = 587
# EMAIL_USER = 'your_email@example.com'
# EMAIL_PASS = 'your_email_password'

# # Aiken County Inmate search URL
# AIKEN_URL = 'https://aikencountysheriff.net/inmate-search'

# @app.route('/check-inmate', methods=['POST'])
# def check_inmate():
#     data = request.json
#     alert_email = data.get('alert_email')
#     alert_phone = data.get('alert_phone')

#     # Perform a GET request to the Aiken County Inmate search page
#     response = requests.get(AIKEN_URL)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Assuming there's a form for searching inmates
#         form_data = {
#             'firstName': 'Foster',
#             'lastName': 'Fech'
#         }

#         # This example assumes that there's an endpoint we can post the search to,
#         # and we need to find this in the form's action attribute.
#         search_form = soup.find('form')
#         if search_form and 'action' in search_form.attrs:
#             search_action_url = search_form['action']
#             search_url = f"https://aikencountysheriff.net{search_action_url}"
            
#             # Perform the search request
#             search_response = requests.post(search_url, data=form_data)

#             if search_response.status_code == 200:
#                 inmate_found = 'No records found' not in search_response.text

#                 # Send an alert if the inmate is found
#                 if inmate_found:
#                     message = f'Inmate Foster Fech has been located in the Aiken County system.'
#                     if alert_email:
#                         send_email_alert(alert_email, message)
#                     if alert_phone:
#                         send_sms_alert(alert_phone, message)
#                     return jsonify({'status': 'Inmate found, alert sent'}), 200
#                 else:
#                     return jsonify({'status': 'Inmate not found'}), 200
#             else:
#                 return jsonify({'status': 'Error performing search'}), 500
#         else:
#             return jsonify({'status': 'Search form not found on the page'}), 500
#     else:
#         return jsonify({'status': 'Error accessing inmate search page'}), 500

# def send_email_alert(to_email, message):
#     msg = MIMEText(message)
#     msg['Subject'] = 'Inmate Search Alert'
#     msg['From'] = EMAIL_USER
#     msg['To'] = to_email

#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(EMAIL_USER, EMAIL_PASS)
#             server.sendmail(EMAIL_USER, to_email, msg.as_string())
#     except Exception as e:
#         print(f'Failed to send email: {e}')

# def send_sms_alert(to_phone, message):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#     try:
#         client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE_NUMBER,
#             to=to_phone
#         )
#     except Exception as e:
#         print(f'Failed to send SMS: {e}')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

## VERSION 1.0

# from flask import Flask, request, jsonify
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from twilio.rest import Client

# app = Flask(__name__)

# # Twilio configuration
# TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
# TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
# TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# # Email configuration
# SMTP_SERVER = 'smtp.example.com'
# SMTP_PORT = 587
# EMAIL_USER = 'your_email@example.com'
# EMAIL_PASS = 'your_email_password'

# # Aiken County Inmate search URL
# AIKEN_URL = 'https://aikencountysheriff.net/inmate-search'

# @app.route('/check-inmate', methods=['POST'])
# def check_inmate():
#     data = request.json
#     # inmate_name = data.get('inmate_name')
#     alert_email = data.get('alert_email')
#     alert_phone = data.get('alert_phone')

#     # Perform a GET request to the Aiken County Inmate search
#     response = requests.post(AIKEN_URL, data={'firstName': 'Foster', 'lastName': 'Fech'})

#     if response.status_code == 200:
#         inmate_found = 'No records found' not in response.text

#         # Send an alert if the inmate is found
#         if inmate_found:
#             message = f'Inmate Foster Fech has been located in the Aiken County system.'
#             if alert_email:
#                 send_email_alert(alert_email, message)
#             if alert_phone:
#                 send_sms_alert(alert_phone, message)
#             return jsonify({'status': 'Inmate found, alert sent'}), 200
#         else:
#             return jsonify({'status': 'Inmate not found'}), 200
#     else:
#         return jsonify({'status': 'Error searching for inmate'}), 500

# def send_email_alert(to_email, message):
#     msg = MIMEText(message)
#     msg['Subject'] = 'Inmate Search Alert'
#     msg['From'] = EMAIL_USER
#     msg['To'] = to_email

#     try:
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(EMAIL_USER, EMAIL_PASS)
#             server.sendmail(EMAIL_USER, to_email, msg.as_string())
#     except Exception as e:
#         print(f'Failed to send email: {e}')

# def send_sms_alert(to_phone, message):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#     try:
#         client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE_NUMBER,
#             to=to_phone
#         )
#     except Exception as e:
#         print(f'Failed to send SMS: {e}')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
