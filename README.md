# SslWireless Sms Api Wrapper for Python
A simple python wrapper for sslwireless sms api.

## Requirements
- requests
- xmltodict

## Usage
- Clone the repository
- Install the dependencies with `pip install -r requirements.txt` or `pip install requests xmltodict`
- Import the class and create instance to access its functions.
### Or
- Install the package with `pip install sslwireless-sms`

## Example
```python
from sslwireless_sms import SSLWirelessSMS  # previously was SslWirelessSms

# username, password and sid provided by sslwireless
# and decode_response for receive response as json or dictionary
sslwireless = SSLWirelessSMS('username', 'password', 'sid', decode_response=False)
# if you want to receive response as dictionary set "decode_response=True"
# and for json set "decode_response=False"
# You can change the api url if needed. i.e.
# sslwireless.url = 'new_url'
result = sslwireless.send('123456789','This is a test message.')

print(result)
```

## Output
The output will always be in JSON format.
```javascript
{
  "status": "success", // or "failed"
  "result": "sms sent", // or "invalid mobile or text" or "invalid mobile" or "invalid credentials"
  "phone": "123456789", // number to send message
  "message": "This is a test message.", // message sent
  "reference_no": "randomly_generated_unique_no", // client generated reference no
  "ssl_reference_no": "returned_sslwirless_reference_no", // api generated reference no
  "datetime": "2018-02-07 01:35AM" // datetime of process
}
```

#### N.B: `SslWirelessSms` class name has changed to `SSLWirelessSMS`
