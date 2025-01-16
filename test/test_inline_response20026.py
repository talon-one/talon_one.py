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
                has_more = True, 
                data = [
                    talon_one.models.application_session.ApplicationSession(
                        id = 6, 
                        created = '2020-02-07T08:15:22Z', 
                        integration_id = 'URNGV8294NV', 
                        store_integration_id = 'STORE-001', 
                        application_id = 322, 
                        profile_id = 138, 
                        profileintegrationid = '382370BKDB946', 
                        coupon = 'BKDB946', 
                        referral = 'BKDB946', 
                        state = 'closed', 
                        cart_items = [
                            talon_one.models.cart_item.CartItem(
                                name = 'Air Glide', 
                                sku = 'SKU1241028', 
                                quantity = 1, 
                                returned_quantity = 1, 
                                remaining_quantity = 1, 
                                price = 99.99, 
                                category = 'shoes', 
                                product = talon_one.models.product.Product(
                                    name = 'sample_product', ), 
                                weight = 1130.0, 
                                height = 1.337, 
                                width = 1.337, 
                                length = 1.337, 
                                position = 1.337, 
                                attributes = {"image":"11.jpeg","material":"leather"}, 
                                additional_costs = {"shipping":{"price":9}}, 
                                catalog_item_id = 56, )
                            ], 
                        discounts = {
                            'key' : 1.337
                            }, 
                        total_discounts = 100.0, 
                        total = 200.0, 
                        attributes = talon_one.models.attributes.attributes(), )
                    ]
            )
        else :
            return InlineResponse20026(
                data = [
                    talon_one.models.application_session.ApplicationSession(
                        id = 6, 
                        created = '2020-02-07T08:15:22Z', 
                        integration_id = 'URNGV8294NV', 
                        store_integration_id = 'STORE-001', 
                        application_id = 322, 
                        profile_id = 138, 
                        profileintegrationid = '382370BKDB946', 
                        coupon = 'BKDB946', 
                        referral = 'BKDB946', 
                        state = 'closed', 
                        cart_items = [
                            talon_one.models.cart_item.CartItem(
                                name = 'Air Glide', 
                                sku = 'SKU1241028', 
                                quantity = 1, 
                                returned_quantity = 1, 
                                remaining_quantity = 1, 
                                price = 99.99, 
                                category = 'shoes', 
                                product = talon_one.models.product.Product(
                                    name = 'sample_product', ), 
                                weight = 1130.0, 
                                height = 1.337, 
                                width = 1.337, 
                                length = 1.337, 
                                position = 1.337, 
                                attributes = {"image":"11.jpeg","material":"leather"}, 
                                additional_costs = {"shipping":{"price":9}}, 
                                catalog_item_id = 56, )
                            ], 
                        discounts = {
                            'key' : 1.337
                            }, 
                        total_discounts = 100.0, 
                        total = 200.0, 
                        attributes = talon_one.models.attributes.attributes(), )
                    ],
        )

    def testInlineResponse20026(self):
        """Test InlineResponse20026"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
