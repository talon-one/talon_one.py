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
from talon_one.models.inline_response20047 import InlineResponse20047  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20047(unittest.TestCase):
    """InlineResponse20047 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20047
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20047.InlineResponse20047()  # noqa: E501
        if include_optional :
            return InlineResponse20047(
                has_more = True, 
                data = [
                    talon_one.models.achievement_progress.AchievementProgress(
                        achievement_id = 3, 
                        name = 'FreeCoffee10Orders', 
                        title = '50% off on 50th purchase.', 
                        campaign_id = 3, 
                        status = 'completed', 
                        target = 10.0, 
                        progress = 10.0, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        completion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return InlineResponse20047(
                has_more = True,
                data = [
                    talon_one.models.achievement_progress.AchievementProgress(
                        achievement_id = 3, 
                        name = 'FreeCoffee10Orders', 
                        title = '50% off on 50th purchase.', 
                        campaign_id = 3, 
                        status = 'completed', 
                        target = 10.0, 
                        progress = 10.0, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        completion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )

    def testInlineResponse20047(self):
        """Test InlineResponse20047"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()