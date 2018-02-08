import requests
import random
import xmltodict
import json
import datetime

class SslWirelessSms:

    url = 'http://sms.sslwireless.com/pushapi/dynamic/server.php'

    def __init__(self, username, password, sid):
        '''
        Set default authentication parameters

        :param username:
        :param password:
        :param sid:
        '''
        self.username = username
        self.password = password
        self.sid = sid

    def send(self, phone, message):
        '''
        Send the message to desired number

        :param phone:
        :param message:
        :return: json
        '''
        result = requests.post(
            self.url,
            data={
                'user': self.username,
                'pass': self.password,
                'sms[0][0]': phone,
                'sms[0][1]': message,
                'sms[0][2]': random.randint(1, 99999999),
                'sid': self.sid
            }
        )

        parsed_result = xmltodict.parse(result.text)

        if 'SMSINFO' in parsed_result['REPLY']:
            
            if 'REFERENCEID' in parsed_result['REPLY']['SMSINFO']:

                return json.dump({
                    'status': 'success',
                    'result': 'sms sent',
                    'phone': phone,
                    'message': message,
                    'reference_no': parsed_result['REPLY']['SMSINFO']['CSMSID'],
                    'ssl_reference_no': parsed_result['REPLY']['SMSINFO']['REFERENCEID'],
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                })

            elif 'SMSVALUE' in parsed_result['REPLY']['SMSINFO']:

                return json.dumps({
                    'status': 'failed',
                    'result': 'invalid mobile or text',
                    'phone': phone,
                    'message': message,
                    'reference_no': '',
                    'ssl_reference_no': '',
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                })

            elif 'MSISDNSTATUS' in parsed_result['REPLY']['SMSINFO']:

                return json.dumps({
                    'status': 'failed',
                    'result': 'invalid mobile',
                    'phone': phone,
                    'message': message,
                    'reference_no': '',
                    'ssl_reference_no': '',
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                })

        else:

            return json.dumps({
                    'status': 'failed',
                    'result': 'invalid credentials',
                    'phone': phone,
                    'message': message,
                    'reference_no': '',
                    'ssl_reference_no': '',
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                })

