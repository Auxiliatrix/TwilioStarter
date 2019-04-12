from twilio.rest import Client

account_sid = 'AC368bf9b5ff8a94b7349905f62ead1ff6'
auth_token = 'f0e0ebb1cf8c2b15200034c1cde87d85'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://059c6343.ngrok.io/answer',
                        to='+14085317415',
                        from_='+18315349412'
                    )

print(call.sid)