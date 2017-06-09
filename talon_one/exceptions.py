import json
import requests

class TalonOneAPIError(Exception):
    """
    TalonOne API Exceptions
    """
    def __init__(self, message, *args):
        self.message = message

        # try to enhance with detailed error from API
        if len(args) > 0 and isinstance(args[0], requests.exceptions.HTTPError):
            hints = json.loads(args[0].response.text)

            if "errors" in hints:
                self.message += " - {}".format(hints["errors"][0]["title"])

            if "message" in hints:
                self.message += " - {}".format(hints["message"])

        super(TalonOneAPIError, self).__init__(self.message, *args)
