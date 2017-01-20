import sys, os, base64, datetime, hashlib, hmac, json
from urlparse import urljoin
import requests

class Client(object):
    """
    Client for calling Talon One Integration API.

    :type endpoint: string
    :param endpoint: API endpoint eg. http://example.talon.one
    :type application_id: number
    :param application_id: Application identifier.
    :type application_key: string
    :param application_key: Application secret key.
    """
    def __init__(self, endpoint, application_id, application_key):
        self.endpoint = endpoint
        self.app_id = application_id
        self.app_key = application_key
        self.token = ''

    # Properties
    def setEndpoint(endpoint):
        self.endpoint = endpoint
    def setAppKey(key):
        self.app_key = key
    def setAppId(id):
        self.app_id = id

    # Public API
    def track_event(self, session_id, event_type, value):
        self.call_api('POST', '/v1/events', { sessionId: session_id, type: event_type, attributes: value })

    def update_customer_session(self, session_id, data):
        self.call_api('PUT', '/v1/customer_sessions/%s' % session_id, data)

    def update_customer_profile(self, integration_id, data):
        self.call_api('PUT', '/v1/customer_profiles/%s' % integration_id, data)

    def close_customer_session(self, session_id):
        self.update_customer_session(session_id, { state: 'closed' })

    # Helper functions
    def call_api(self, method, path, data, token=None):
        try:
            url = self.__build_url(path)
            payload = json.dumps(data)

            headers = {}
            headers['Content-Type'] ='application/json',
            headers['Content-Signature'] = 'signer=%s; signature=%s' % (self.app_id, self.__signature(payload))

            print headers

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
                raise Exception("Unable to call API - %s, %s, %s => %s" % (method, url, data, response.status_code))
        except:
            err = sys.exc_info()[0]
            raise Exception("Unable to call API - %s, %s, %s" % (method, url, data))

    def __build_url(self, path):
        return urljoin(self.endpoint, path)

    def __signature(self, msg):
        return hmac.new(self.app_key, msg.encode('utf-8'), hashlib.md5).hexdigest()
