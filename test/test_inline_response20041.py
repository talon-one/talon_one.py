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
from talon_one.models.inline_response20041 import InlineResponse20041  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20041(unittest.TestCase):
    """InlineResponse20041 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20041
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20041.InlineResponse20041()  # noqa: E501
        if include_optional :
            return InlineResponse20041(
                total_result_size = 1, 
                has_more = True, 
                data = [
                    talon_one.models.change.Change(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        user_id = 388, 
                        application_id = 359, 
                        entity = '/v1/applications/359/campaigns/6727', 
                        old = {}, 
                        new = {"applicationId\"":359,"attributes\"":{},"campaignGroups\"":[],"created\"":"2022-07-08T13:04:02.972762328Z","description\"":"","features\"":["referrals","loyalty"],"id":6727}, 
                        management_key_id = 3, )
                    ]
            )
        else :
            return InlineResponse20041(
                data = [
                    talon_one.models.change.Change(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        user_id = 388, 
                        application_id = 359, 
                        entity = '/v1/applications/359/campaigns/6727', 
                        old = {}, 
                        new = {"applicationId\"":359,"attributes\"":{},"campaignGroups\"":[],"created\"":"2022-07-08T13:04:02.972762328Z","description\"":"","features\"":["referrals","loyalty"],"id":6727}, 
                        management_key_id = 3, )
                    ],
        )

    def testInlineResponse20041(self):
        """Test InlineResponse20041"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
