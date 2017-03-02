import sys, os, hashlib, hmac, cjson
from urlparse import urljoin
from talon_one import exceptions
import requests
import simplejson

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
    def __init__(self, endpoint="", application_id="", application_key=""):
        self.endpoint = endpoint if "" else os.environ["TALONONE_ENDPOINT"]
        self.app_id = application_id if "" else os.environ["TALONONE_APP_ID"]
        self.app_key = application_key if None else os.environ["TALONONE_APP_KEY"]
        self.debug = False

    # Properties
    def get_endpoint(self):
        return self.endpoint
    def set_endpoint(self, endpoint):
        self.endpoint = endpoint
    def get_app_key(self):
        return self.app_key
    def set_app_key(self, key):
        self.app_key = key
    def get_app_id(self):
        return self.app_id
    def set_app_id(self, app_id):
        self.app_id = app_id
    def set_debug(self, enable):
        self.debug = enable

    # Public API
    def track_event(self, integration_id, session_id, event_type, value={}):
        return self.call_api("POST", "/v1/events", {"profileId": integration_id,
                                                    "sessionId": session_id,
                                                    "type": event_type,
                                                    "attributes": value})

    def update_customer_session(self, session_id, payload):
        return  self.call_api("PUT", "/v1/customer_sessions/%s" % session_id, payload)

    def update_customer_profile(self, integration_id, payload):
        return  self.call_api("PUT", "/v1/customer_profiles/%s" % integration_id, payload)

    def close_customer_session(self, session_id):
        return  self.update_customer_session(session_id, { "state": "closed" })

    def create_referral_code(self, payload):
        return self.call_api("POST", "/v1/referrals", payload)

    # Helper functions
    def call_api(self, method, path, payload, token=None):
        try:
            url = self.__build_url(path)
            json_payload = cjson.encode(payload)

            headers = {}
            headers["Content-Type"] ="application/json",
            headers["Content-Signature"] = "signer=%s; signature=%s" % (self.app_id, self.__signature(json_payload))

            if self.debug:
                print "Auth: %s" % headers["Content-Signature"]
                print "JSON: %s" % json_payload

            response = None
            if method == "POST":
                response = requests.post(url, data=json_payload, headers=headers)
            elif method == "PUT":
                response = requests.put(url, data=json_payload, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                response = requests.get(url, headers=headers)

            # raise HTTP error if present
            response.raise_for_status()

            if response.status_code == 204:
                return response
            else:
                return response.json()
        except simplejson.scanner.JSONDecodeError as je:
            raise exceptions.TalonOneAPIError("Integration API", je)
        except requests.HTTPError as he:
            raise exceptions.TalonOneAPIError("Integration API", he)
        except exceptions.TalonOneAPIError:
            err = sys.exc_info()[0]
            raise exceptions.TalonOneAPIError("Integration API", err, url)

    def __build_url(self, path):
        return urljoin(self.endpoint, path)

    def __signature(self, msg):
        return hmac.new(self.app_key.decode("hex"), msg.encode("utf-8"), hashlib.md5).hexdigest()
