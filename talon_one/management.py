import sys, os, hashlib, hmac, cjson
from urlparse import urljoin
from talon_one import exceptions
import requests
import simplejson

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
        self.endpoint = endpoint if "" else os.environ["TALONONE_ENDPOINT"]
        self.email = email if "" else os.environ["TALONONE_EMAIL"]
        self.passwd = passwd if "" else os.environ["TALONONE_PASSWORD"]
        self.token = os.environ["TALONONE_SESSION_TOKEN"] if "" else None

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
                   "key":      api_key
        }
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
    def call_api(self, method, path, payload={}, token=None):
        try:
            url = self.__build_url(path)

            headers = {}
            headers["Content-Type"] ="application/json",
            headers["Authorization"] = "Bearer %s" % self.token

            response = None
            if method == "POST":
                response = requests.post(url, data=cjson.encode(payload), headers=headers)
            elif method == "PUT":
                response = requests.put(url, data=cjson.encode(payload), headers=headers)
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
            err = sys.exc_info()[0]
            raise exceptions.TalonOneAPIError("Management API", url, err)

    def __build_url(self, path):
        return urljoin(self.endpoint, path)
