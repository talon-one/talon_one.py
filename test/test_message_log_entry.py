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
from talon_one.models.message_log_entry import MessageLogEntry  # noqa: E501
from talon_one.rest import ApiException

class TestMessageLogEntry(unittest.TestCase):
    """MessageLogEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageLogEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.message_log_entry.MessageLogEntry()  # noqa: E501
        if include_optional :
            return MessageLogEntry(
                id = '123e4567-e89b-12d3-a456-426614174000', 
                service = 'NotificationService', 
                change_type = 'Update', 
                notification_id = 101, 
                notification_name = 'My campaign notification', 
                webhook_id = 101, 
                webhook_name = 'My webhook', 
                request = talon_one.models.message_log_request.MessageLogRequest(
                    created_at = '2021-07-20T21:59Z', 
                    request = 'SGVsbG8sIHdvcmxkIQ==', ), 
                response = talon_one.models.message_log_response.MessageLogResponse(
                    created_at = '2021-07-20T22:00:50Z', 
                    status = 200, ), 
                created_at = '2021-07-20T22:00Z', 
                entity_type = 'loyalty_program', 
                url = 'www.my-company.com/my-endpoint-name', 
                application_id = 5, 
                loyalty_program_id = 2, 
                campaign_id = 2
            )
        else :
            return MessageLogEntry(
                id = '123e4567-e89b-12d3-a456-426614174000',
                service = 'NotificationService',
                created_at = '2021-07-20T22:00Z',
                entity_type = 'loyalty_program',
        )

    def testMessageLogEntry(self):
        """Test MessageLogEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
