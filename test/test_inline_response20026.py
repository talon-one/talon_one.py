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
from talon_one.models.inline_response20026 import InlineResponse20026  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20026(unittest.TestCase):
    """InlineResponse20026 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20026
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20026.InlineResponse20026()  # noqa: E501
        if include_optional :
            return InlineResponse20026(
                total_result_size = 56, 
                data = [
                    talon_one.models.user.User(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        email = '0', 
                        account_id = 56, 
                        invite_token = '0', 
                        state = 'invited', 
                        name = '0', 
                        policy = '0', 
                        release_update = True, 
                        latest_feature = '0', 
                        roles = [
                            56
                            ], 
                        application_notification_subscriptions = talon_one.models.application_notification_subscriptions.applicationNotificationSubscriptions(), 
                        auth_method = '0', )
                    ]
            )
        else :
            return InlineResponse20026(
                total_result_size = 56,
                data = [
                    talon_one.models.user.User(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        email = '0', 
                        account_id = 56, 
                        invite_token = '0', 
                        state = 'invited', 
                        name = '0', 
                        policy = '0', 
                        release_update = True, 
                        latest_feature = '0', 
                        roles = [
                            56
                            ], 
                        application_notification_subscriptions = talon_one.models.application_notification_subscriptions.applicationNotificationSubscriptions(), 
                        auth_method = '0', )
                    ],
        )

    def testInlineResponse20026(self):
        """Test InlineResponse20026"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
