import requests, json

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
                self.message += " - %s" % hints["errors"][0]["title"]

        super(TalonOneAPIError, self).__init__(self.message, *args)
