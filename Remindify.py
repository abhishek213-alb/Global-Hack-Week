from twilio.rest import Client 
 
account_sid = '' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:no',  
                              body='remindertext',      
                              to='whatsapp:' 
                          ) 
 
print(message.sid)
