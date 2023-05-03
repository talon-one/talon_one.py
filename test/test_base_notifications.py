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
from talon_one.models.base_notifications import BaseNotifications  # noqa: E501
from talon_one.rest import ApiException

class TestBaseNotifications(unittest.TestCase):
    """BaseNotifications unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BaseNotifications
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.base_notifications.BaseNotifications()  # noqa: E501
        if include_optional :
            return BaseNotifications(
                data = [
                    talon_one.models.base_notification.BaseNotification(
                        policy = talon_one.models.base_notification_policy.BaseNotificationPolicy(), 
                        webhook = talon_one.models.base_notification_webhook.BaseNotificationWebhook(
                            id = 6, 
                            created = '2020-06-10T09:05:27.993483Z', 
                            modified = '2021-09-12T10:12:42Z', 
                            url = 'www.my-company.com/my-endpoint-name', 
                            headers = content-type: application/json, ), 
                        id = 6, )
                    ]
            )
        else :
            return BaseNotifications(
        )

    def testBaseNotifications(self):
        """Test BaseNotifications"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
