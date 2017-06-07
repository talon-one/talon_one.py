import os
import sys
import hmac
import hashlib

if sys.version_info[0] == 3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

"""
Utilities shared both integration and management API
"""
def build_url(endpoint, path):
    return urljoin(endpoint, path)

def signature(app_key, msg):
    return hmac.new(app_key.decode("hex"), msg.encode("utf-8"), hashlib.md5).hexdigest()

def setup(prop_value, env_name):
    if prop_value == '':
        if env_name in os.environ and os.environ[env_name] != '':
            return os.environ[env_name]
        else:
            return ""
    else:
        return prop_value
