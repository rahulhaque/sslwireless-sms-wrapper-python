from sslwireless_sms import SslWirelessSms

# username, password and sid provided by sslwireless
SslWirelessSms = SslWirelessSms('username', 'password', 'sid')
# You can change the api url if needed. i.e.
# SslWirelessSms.url = 'new_url'
result = SslWirelessSms.send('123456789','This is a test message.')

print(result)