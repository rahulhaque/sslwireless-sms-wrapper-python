from sslwireless_sms import SSLWirelessSMS

# username, password and sid provided by sslwireless
# A fourth parameter 'decode_response' can be passed to determine the return type of data
# By default 'decode_response' is set to 'False' so it will return json data as result
# Set 'decode_response' to 'True' to get python dict as result
SSLWirelessSMS = SSLWirelessSMS('username', 'password', 'sid')
# You can change the api url if needed. i.e.
# SSLWirelessSMS.url = 'new_url'
result = SSLWirelessSMS.send('123456789','This is a test message.')

print(result)