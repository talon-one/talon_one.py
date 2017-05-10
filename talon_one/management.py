import sys
import json
import requests
import simplejson
from talon_one import exceptions
from talon_one import utils

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
    def __init__(self, endpoint="", email="", passwd=""):
        self.endpoint = endpoint
        self.email = email
        self.passwd = passwd
        self.token = None

        # maybe set value from ENV vars
        setattr(self, "endpoint", utils.setup(self.endpoint, "TALONONE_ENDPOINT"))
        setattr(self, "email", utils.setup(self.email, "TALONONE_EMAIL"))
        setattr(self, "passwd", utils.setup(self.passwd, "TALONONE_PASSWORD"))
        setattr(self, "token", utils.setup(self.token, "TALONONE_SESSION_TOKEN"))

    # Properties
    def get_token(self):
        return self.token
    def get_endpoint(self):
        return self.endpoint
    def set_endpoint(self, endpoint):
        self.endpoint = endpoint
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_password(self):
        return self.passwd
    def set_password(self, passwd):
        self.passwd = passwd

    # Public API
    def login(self):
        response = self.post("/v1/sessions", {"email": self.email, "password": self.passwd})
        self.token = response["token"]
        return response

    def create_application(self, name, api_key, integration_type="Own Shop System (API)", tz="UTC", currency="EUR"):
        payload = {"name":     name,
                   "type":     integration_type,
                   "timezone": tz,
                   "currency": currency,
                   "key":      api_key}
        return self.post("/v1/applications", payload)

    def delete_application(self, id):
        return self.delete("/v1/applications/%d" % id)

    # Low level REST API
    def get(self, path):
        return self.call_api("GET", path)

    def put(self, path, payload):
        return self.call_api("PUT", path, payload)

    def post(self, path, payload):
        return self.call_api("POST", path, payload)

    def delete(self, path):
        return self.call_api("DELETE", path)

    # Helper functions
    def call_api(self, method, path, payload={}):
        try:
            url = utils.build_url(self.endpoint, path)

            headers = {}
            headers["Content-Type"] = "application/json",
            headers["Authorization"] = "Bearer %s" % self.token

            response = None
            if method == "POST":
                response = requests.post(url, data=json.dumps(payload), headers=headers)
            elif method == "PUT":
                response = requests.put(url, data=json.dumps(payload), headers=headers)
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
            raise exceptions.TalonOneAPIError("Management API", je)
        except requests.HTTPError as he:
            raise exceptions.TalonOneAPIError("Management API", he)
        except:
            raise exceptions.TalonOneAPIError("Management API", url, sys.exc_info()[1])
