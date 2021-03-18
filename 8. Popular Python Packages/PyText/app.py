from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="+16462049138",
    from_="+18156056523",
    body="this is our first message"
)

print(call.date_sent)  # call object has multiple methods and attribttues to use
