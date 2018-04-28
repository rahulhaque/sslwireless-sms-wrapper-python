SSLWireless SMS Api Wrapper for Python
======================================

A simple python wrapper for sslwireless sms api.

Requirements
------------

-  requests
-  xmltodict

Usage
-----

-  Clone the repository
-  Install the dependencies with ``pip install -r requirements.txt`` or
   ``pip install requests xmltodict``
-  Import the class and create instance to access its functions.
Or
---
-  Install the package with ``pip install sslwireless-sms``

Example
-------

.. code:: python

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

Output
------

The default output will always be in JSON format unless you set
``decode_response`` to be ``True``.

.. code:: javascript

    {
      "status": "success", // or "failed"
      "result": "sms sent", // or "invalid mobile or text" or "invalid mobile" or "invalid credentials"
      "phone": "123456789", // number to send message
      "message": "This is a test message.", // message sent
      "reference_no": "randomly_generated_unique_no", // client generated reference no
      "ssl_reference_no": "returned_sslwirless_reference_no", // api generated reference no
      "datetime": "2018-02-07 01:35AM" // datetime of process
    }

