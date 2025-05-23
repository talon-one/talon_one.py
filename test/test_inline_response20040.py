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
from talon_one.models.inline_response20040 import InlineResponse20040  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20040(unittest.TestCase):
    """InlineResponse20040 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20040
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20040.InlineResponse20040()  # noqa: E501
        if include_optional :
            return InlineResponse20040(
                total_result_size = 1, 
                data = [
                    talon_one.models.webhook_activation_log_entry.WebhookActivationLogEntry(
                        integration_request_uuid = '6d3699cf-95bd-444a-b62f-80d6e8391dc9', 
                        webhook_id = 1, 
                        application_id = 13, 
                        campaign_id = 86, 
                        created = '2023-03-21T13:55:08.571144Z', )
                    ]
            )
        else :
            return InlineResponse20040(
                total_result_size = 1,
                data = [
                    talon_one.models.webhook_activation_log_entry.WebhookActivationLogEntry(
                        integration_request_uuid = '6d3699cf-95bd-444a-b62f-80d6e8391dc9', 
                        webhook_id = 1, 
                        application_id = 13, 
                        campaign_id = 86, 
                        created = '2023-03-21T13:55:08.571144Z', )
                    ],
        )

    def testInlineResponse20040(self):
        """Test InlineResponse20040"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
