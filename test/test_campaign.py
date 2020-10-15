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
from talon_one.models.campaign import Campaign  # noqa: E501
from talon_one.rest import ApiException

class TestCampaign(unittest.TestCase):
    """Campaign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Campaign
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.campaign.Campaign()  # noqa: E501
        if include_optional :
            return Campaign(
                id = 56, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                application_id = 56, 
                user_id = 56, 
                name = '0', 
                description = '0', 
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                attributes = None, 
                state = 'enabled', 
                active_ruleset_id = 56, 
                tags = [
                    '0'
                    ], 
                features = [
                    'coupons'
                    ], 
                coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                    valid_characters = [
                        '0'
                        ], 
                    coupon_pattern = '012', ), 
                referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                    valid_characters = [
                        '0'
                        ], 
                    coupon_pattern = '012', ), 
                limits = [
                    talon_one.models.limit_config.LimitConfig(
                        action = 'redeemCoupon', 
                        limit = 0, 
                        entities = [
                            'Coupon'
                            ], )
                    ], 
                campaign_groups = [
                    56
                    ], 
                coupon_redemption_count = 56, 
                referral_redemption_count = 56, 
                discount_count = 56, 
                discount_effect_count = 56, 
                coupon_creation_count = 56, 
                last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                updated_by = '0'
            )
        else :
            return Campaign(
                id = 56,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                application_id = 56,
                user_id = 56,
                name = '0',
                description = '0',
                state = 'enabled',
                tags = [
                    '0'
                    ],
                features = [
                    'coupons'
                    ],
                limits = [
                    talon_one.models.limit_config.LimitConfig(
                        action = 'redeemCoupon', 
                        limit = 0, 
                        entities = [
                            'Coupon'
                            ], )
                    ],
        )

    def testCampaign(self):
        """Test Campaign"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
