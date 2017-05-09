import sys, json, requests, simplejson
from talon_one import exceptions
from talon_one import utils

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
        self.endpoint = endpoint
        self.application_id = application_id
        self.application_key = application_key
        self.debug = False

        # maybe set value from ENV vars
        setattr(self, "endpoint",        utils.setup(self.endpoint,        "TALONONE_ENDPOINT"))
        setattr(self, "application_id",  utils.setup(self.application_id,  "TALONONE_APP_ID"))
        setattr(self, "application_key", utils.setup(self.application_key, "TALONONE_APP_KEY"))

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
        return  self.update_customer_session(session_id, {"state": "closed"})

    def create_referral_code(self, payload):
        return self.call_api("POST", "/v1/referrals", payload)

    # Helper functions
    def call_api(self, method, path, payload):
        try:
            url = utils.build_url(self.endpoint, path)
            json_payload = json.dumps(payload)
            signature = utils.signature(self.application_key, json_payload)

            headers = {}
            headers["Content-Type"] = "application/json",
            headers["Content-Signature"] = "signer=%s; signature=%s" % (self.application_id, signature)

            if self.debug:
                print("Auth: %s" % headers["Content-Signature"])
                print("JSON: %s" % json_payload)

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
