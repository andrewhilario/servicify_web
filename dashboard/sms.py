from twilio.rest import Client
import environ

from django.conf import settings

# read .env
env = environ.Env()
environ.Env.read_env(".env")

account_sid = env('TWILIO_ACCOUNT_SID')
auth_token = env('TWILIO_AUTH_TOKEN')
msg_srv_sid = env('TWILIO_MSG_SID')


def send_sms(recipient, text_body):
    if settings.SMS_NOTIFICATION:
        client = Client(account_sid, auth_token)

        text_body += '\n\n\
            - SMS notification from Servicify.'
        message = client.messages.create(
            body=text_body,
            messaging_service_sid=msg_srv_sid,
            to=recipient
        )
        print(message.sid)
    else:
        pass
