# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.scim_user import ScimUser  # noqa: E501
from talon_one.rest import ApiException

class TestScimUser(unittest.TestCase):
    """ScimUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScimUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.scim_user.ScimUser()  # noqa: E501
        if include_optional :
            return ScimUser(
                active = True, 
                display_name = 'John Doe', 
                user_name = 'john.doe@example.com', 
                name = talon_one.models.scim_base_user_name.ScimBaseUser_name(
                    formatted = 'Mr. John J Doe', ), 
                id = '359'
            )
        else :
            return ScimUser(
                user_name = 'john.doe@example.com',
                id = '359',
        )

    def testScimUser(self):
        """Test ScimUser"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
