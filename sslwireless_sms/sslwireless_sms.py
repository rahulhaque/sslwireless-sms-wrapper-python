import requests
import random
import xmltodict
import json
import datetime


class SSLWirelessSMS:

    url = 'http://sms.sslwireless.com/pushapi/dynamic/server.php'

    def __init__(self, username, password, sid, decode_response = False):
        '''
        Set default authentication parameters

        :param username:
        :param password:
        :param sid:
        :param decode_response:
        '''
        self.username = username
        self.password = password
        self.sid = sid
        self.decode_response = decode_response

    def send(self, phone, message):
        '''
        Send the message to desired number

        :param phone:
        :param message:
        :return: json
        '''
        result = requests.post(
            self.url,
            data = {
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
                response = {
                    'status': 'success',
                    'result': 'sms sent',
                    'phone': phone,
                    'message': message,
                    'reference_no': parsed_result['REPLY']['SMSINFO']['CSMSID'],
                    'ssl_reference_no': parsed_result['REPLY']['SMSINFO']['REFERENCEID'],
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                }
                return self._make_response(response)

            elif 'SMSVALUE' in parsed_result['REPLY']['SMSINFO']:
                response = {
                    'status': 'failed',
                    'result': 'invalid mobile or text',
                    'phone': phone,
                    'message': message,
                    'reference_no': '',
                    'ssl_reference_no': '',
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                }
                return self._make_response(response)

            elif 'MSISDNSTATUS' in parsed_result['REPLY']['SMSINFO']:
                response = {
                    'status': 'failed',
                    'result': 'invalid mobile',
                    'phone': phone,
                    'message': message,
                    'reference_no': '',
                    'ssl_reference_no': '',
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                }
                return self._make_response(response)

        else:
            response = {
                    'status': 'failed',
                    'result': 'invalid credentials',
                    'phone': phone,
                    'message': message,
                    'reference_no': '',
                    'ssl_reference_no': '',
                    'datetime': datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')
                }
            return self._make_response(response)

    def _make_response(self, data):
        '''
        Decides whether the response to be json or dict

        :param data:
        :return:
        '''
        if self.decode_response:
            return data
        return json.dumps(data)

