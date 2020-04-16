# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.saml_login_endpoint import SamlLoginEndpoint  # noqa: E501
from talon_one.rest import ApiException

class TestSamlLoginEndpoint(unittest.TestCase):
    """SamlLoginEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SamlLoginEndpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.saml_login_endpoint.SamlLoginEndpoint()  # noqa: E501
        if include_optional :
            return SamlLoginEndpoint(
                name = '0', 
                login_url = '0'
            )
        else :
            return SamlLoginEndpoint(
                name = '0',
                login_url = '0',
        )

    def testSamlLoginEndpoint(self):
        """Test SamlLoginEndpoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
