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
from talon_one.models.inline_response2005 import InlineResponse2005  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse2005(unittest.TestCase):
    """InlineResponse2005 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2005
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response2005.InlineResponse2005()  # noqa: E501
        if include_optional :
            return InlineResponse2005(
                has_more = True, 
                data = [
                    talon_one.models.coupon.Coupon(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        campaign_id = 56, 
                        value = '0123', 
                        usage_limit = 0, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        usage_counter = 56, 
                        attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                        referral_id = 56, 
                        recipient_integration_id = '0', 
                        import_id = 56, 
                        reservation = True, 
                        batch_id = '0', )
                    ]
            )
        else :
            return InlineResponse2005(
                has_more = True,
                data = [
                    talon_one.models.coupon.Coupon(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        campaign_id = 56, 
                        value = '0123', 
                        usage_limit = 0, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        usage_counter = 56, 
                        attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                        referral_id = 56, 
                        recipient_integration_id = '0', 
                        import_id = 56, 
                        reservation = True, 
                        batch_id = '0', )
                    ],
        )

    def testInlineResponse2005(self):
        """Test InlineResponse2005"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
