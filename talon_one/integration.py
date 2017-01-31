import sys, os, hashlib, hmac
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

    # Properties
    def getEndpoint(self):
        return self.endpoint
    def setEndpoint(self, endpoint):
        self.endpoint = endpoint
    def getAppKey(self):
        return self.app_key
    def setAppKey(self, key):
        self.app_key = key
    def getAppId(self):
        return self.app_id
    def setAppId(self, id):
        self.app_id = id

    # Public API
    def track_event(self, session_id, event_type, value):
        return self.call_api('POST', '/v1/events', { sessionId: session_id, type: event_type, attributes: value })

    def update_customer_session(self, session_id, payload):
        return self.call_api('PUT', '/v1/customer_sessions/%s' % session_id, payload)

    def update_customer_profile(self, integration_id, payload):
        return self.call_api('PUT', '/v1/customer_profiles/%s' % integration_id, payload)

    def close_customer_session(self, session_id):
        return self.update_customer_session(session_id, { state: 'closed' })

    # Helper functions
    def call_api(self, method, path, payload, token=None):
        try:
            url = self.__build_url(path)
            json_payload = json.dumps(payload)

            headers = {}
            headers['Content-Type'] ='application/json',
            headers['Content-Signature'] = 'signer=%s; signature=%s' % (self.app_id, self.__signature(json_payload))

            response = None
            if method == 'POST':
                response = requests.post(url, data=json_payload, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, data=json_payload, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                response = requests.get(url, headers=headers)

            if response.status_code < 400:
                return response.json()
            else:
                raise Exception("Unable to call API - %s, %s, %s => %s" % (method, url, payload, response.status_code))
        except:
            err = sys.exc_info()[0]
            raise Exception("Unable to call API - %s, %s, %s" % (method, url, payload))

    def __build_url(self, path):
        return urljoin(self.endpoint, path)

    def __signature(self, msg):
        return hmac.new(self.app_key.decode('hex'), msg.encode('utf-8'), hashlib.md5).hexdigest()
