#!/usr/bin/env python

#
# Client for calling Talon One Management API
#

import sys, os, base64, datetime, hashlib, hmac, json
from urlparse import urljoin
import requests

class Client(object):
    """
    Client for calling Talon One Management API.

    :type endpoint: string
    :param endpoint: API endpoint eg. http://example.talon.one
    :type email: string
    :param email: The email address associated with your account.
    :type passwd: string
    :param passwd: The password for your account.
    """
    def __init__(self, endpoint, email, passwd):
        self.endpoint = endpoint
        self.email = email
        self.passwd = passwd

    # Properties
    def setEndpoint(endpoint):
        self.endpoint = endpoint
    def setEmail(email):
        self.email = email
    def setPassword(passwd):
        self.passwd = passwd


    # Public API
    def login(self):
        data = self.call_api('POST', "/v1/sessions", {'email': self.email, 'password': self.passwd})
        self.token = data['token']
        return True

    def create_account(self, companyName, email, passwd):
        params = {'companyName': companyName, 'email': self.email, 'password': self.passwd}
        data = self.call_api('POST', "/v1/accounts", params)
        self.token = data['token']

    def create_application(self, name, api_key, integration_type='Own Shop System (API)', tz='UTC', currency='EUR'):
        data = {'name':     name,
                'type':     integration_type,
                'timezone': tz,
                'currency': currency,
                'key':      api_key
        }
        return self.call_api('POST', "/v1/applications", data)

    # Helper functions
    def call_api(self, method, path, data, token=None):
        try:
            url = self.__build_url(path)

            headers = {}
            headers['Content-Type'] ='application/json',
            headers['Authorization'] = 'Bearer %s' % token

            payload = json.dumps(data)

            response = None
            if method == 'POST':
                response = requests.post(url, data=payload, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, data=payload, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                response = requests.get(url, headers=headers)

            if response.status_code < 400:
                return response.json()
            else:
                raise Exception("Unable to call API - %s, %s => %s" % (method, url, response.status_code))
        except:
            err = sys.exc_info()[0]
            raise Exception("Unable to call API - %s, %s - %s" % (method, url, err))

    def __build_url(self, path):
        return urljoin(self.endpoint, path)
