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
    def getEndpoint(self):
        return self.endpoint
    def setEndpoint(self, endpoint):
        self.endpoint = endpoint
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
    def getPassword(self):
        return self.passwd
    def setPassword(self, passwd):
        self.passwd = passwd

    # Public API
    def login(self):
        response = self.post("/v1/sessions", {'email': self.email, 'password': self.passwd})
        self.token = response['token']
        return response

    def logout(self):
        response = self.call_api('DELETE', "/v1/sessions", {'email': self.email, 'password': self.passwd})
        self.token = None
        self.email = None
        self.passwd = None
        return response

    def create_account(self, companyName, email, passwd):
        payload = {'companyName': companyName, 'email': self.email, 'password': self.passwd}
        response = self.post("/v1/accounts", payload)
        self.token = response['token']
        return response

    def create_application(self, name, api_key, integration_type='Own Shop System (API)', tz='UTC', currency='EUR'):
        payload = {'name':     name,
                   'type':     integration_type,
                   'timezone': tz,
                   'currency': currency,
                   'key':      api_key
        }
        return self.post("/v1/applications", payload)

    # Low level API
    def get(self, path):
        return self.call_api("GET", path)

    def put(self, path, payload):
        return self.call_api("PUT", path, payload)

    def post(self, path, payload):
        return self.call_api("POST", path, payload)

    def delete(self, path):
        return self.call_api("DELETE", path)

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
