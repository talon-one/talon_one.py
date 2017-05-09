import sys, os, hashlib, hmac, json
if sys.version_info[0] == 3:
    from urllib import parse
else:
    from urlparse import urljoin

def build_url(endpoint, path):
    return urljoin(endpoint, path)

def signature(app_key, msg):
    return hmac.new(app_key.decode("hex"), msg.encode("utf-8"), hashlib.md5).hexdigest()

def setup(propValue, envName):
    if propValue == '':
        if envName in os.environ and os.environ[envName] != '':
            return os.environ[envName]
        else:
            return ""
    else:
        return propValue
