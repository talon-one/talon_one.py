# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.user import User  # noqa: E501
from talon_one.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                modified = '2021-09-12T10:12:42Z', 
                email = 'john.doe@example.com', 
                account_id = 3886, 
                invite_token = 'Gy9b8w1irmQtEPo5RmbMmSPheL5h4', 
                state = 'invited', 
                name = 'John Doe', 
                policy = {"Role":127}, 
                latest_feed_timestamp = '2020-06-01T00:00Z', 
                roles = [71], 
                application_notification_subscriptions = None, 
                auth_method = 'basic_auth'
            )
        else :
            return User(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                modified = '2021-09-12T10:12:42Z',
                email = 'john.doe@example.com',
                account_id = 3886,
                invite_token = 'Gy9b8w1irmQtEPo5RmbMmSPheL5h4',
                state = 'invited',
                name = 'John Doe',
                policy = {"Role":127},
        )

    def testUser(self):
        """Test User"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
