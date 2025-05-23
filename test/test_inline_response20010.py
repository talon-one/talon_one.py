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
from talon_one.models.inline_response20010 import InlineResponse20010  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20010(unittest.TestCase):
    """InlineResponse20010 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20010
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20010.InlineResponse20010()  # noqa: E501
        if include_optional :
            return InlineResponse20010(
                total_result_size = 1, 
                data = [
                    talon_one.models.coupon.Coupon(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        campaign_id = 211, 
                        value = 'XMAS-20-2021', 
                        usage_limit = 100, 
                        discount_limit = 30.0, 
                        reservation_limit = 45, 
                        start_date = '2020-01-24T14:15:22Z', 
                        expiry_date = '2023-08-24T14:15:22Z', 
                        limits = [
                            talon_one.models.limit_config.LimitConfig(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                period = 'yearly', 
                                entities = [Coupon], )
                            ], 
                        usage_counter = 10, 
                        discount_counter = 10.0, 
                        discount_remainder = 5.0, 
                        reservation_counter = 1.0, 
                        attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                        referral_id = 326632952, 
                        recipient_integration_id = 'URNGV8294NV', 
                        import_id = 4, 
                        reservation = False, 
                        batch_id = '32535-43255', 
                        is_reservation_mandatory = False, 
                        implicitly_reserved = False, )
                    ]
            )
        else :
            return InlineResponse20010(
                total_result_size = 1,
                data = [
                    talon_one.models.coupon.Coupon(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        campaign_id = 211, 
                        value = 'XMAS-20-2021', 
                        usage_limit = 100, 
                        discount_limit = 30.0, 
                        reservation_limit = 45, 
                        start_date = '2020-01-24T14:15:22Z', 
                        expiry_date = '2023-08-24T14:15:22Z', 
                        limits = [
                            talon_one.models.limit_config.LimitConfig(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                period = 'yearly', 
                                entities = [Coupon], )
                            ], 
                        usage_counter = 10, 
                        discount_counter = 10.0, 
                        discount_remainder = 5.0, 
                        reservation_counter = 1.0, 
                        attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                        referral_id = 326632952, 
                        recipient_integration_id = 'URNGV8294NV', 
                        import_id = 4, 
                        reservation = False, 
                        batch_id = '32535-43255', 
                        is_reservation_mandatory = False, 
                        implicitly_reserved = False, )
                    ],
        )

    def testInlineResponse20010(self):
        """Test InlineResponse20010"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
