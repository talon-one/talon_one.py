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
from talon_one.models.inline_response2006 import InlineResponse2006  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse2006(unittest.TestCase):
    """InlineResponse2006 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2006
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response2006.InlineResponse2006()  # noqa: E501
        if include_optional :
            return InlineResponse2006(
                total_result_size = 1, 
                data = [
                    talon_one.models.campaign.Campaign(
                        id = 4, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        application_id = 322, 
                        user_id = 388, 
                        name = 'Summer promotions', 
                        description = 'Campaign for all summer 2021 promotions', 
                        start_time = '2021-07-20T22:00Z', 
                        end_time = '2021-09-22T22:00Z', 
                        attributes = talon_one.models.attributes.attributes(), 
                        state = 'enabled', 
                        active_ruleset_id = 6, 
                        tags = [summer], 
                        features = [coupons, referrals], 
                        coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                            valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                            coupon_pattern = 'SUMMER-####-####', ), 
                        referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                            valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                            coupon_pattern = 'SUMMER-####-####', ), 
                        limits = [
                            talon_one.models.limit_config.LimitConfig(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                period = 'yearly', 
                                entities = [Coupon], )
                            ], 
                        campaign_groups = [1, 3], 
                        type = 'advanced', 
                        linked_store_ids = [1, 2, 3], 
                        budgets = [
                            talon_one.models.campaign_budget.CampaignBudget(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                counter = 42.0, )
                            ], 
                        coupon_redemption_count = 163, 
                        referral_redemption_count = 3, 
                        discount_count = 288.0, 
                        discount_effect_count = 343, 
                        coupon_creation_count = 16, 
                        custom_effect_count = 0, 
                        referral_creation_count = 8, 
                        add_free_item_effect_count = 0, 
                        awarded_giveaways_count = 9, 
                        created_loyalty_points_count = 9.0, 
                        created_loyalty_points_effect_count = 2, 
                        redeemed_loyalty_points_count = 8.0, 
                        redeemed_loyalty_points_effect_count = 9, 
                        call_api_effect_count = 0, 
                        reservecoupon_effect_count = 9, 
                        last_activity = '2022-11-10T23:00Z', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = 'John Doe', 
                        updated_by = 'Jane Doe', 
                        template_id = 3, 
                        frontend_state = 'running', 
                        stores_imported = True, )
                    ]
            )
        else :
            return InlineResponse2006(
                total_result_size = 1,
                data = [
                    talon_one.models.campaign.Campaign(
                        id = 4, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        application_id = 322, 
                        user_id = 388, 
                        name = 'Summer promotions', 
                        description = 'Campaign for all summer 2021 promotions', 
                        start_time = '2021-07-20T22:00Z', 
                        end_time = '2021-09-22T22:00Z', 
                        attributes = talon_one.models.attributes.attributes(), 
                        state = 'enabled', 
                        active_ruleset_id = 6, 
                        tags = [summer], 
                        features = [coupons, referrals], 
                        coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                            valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                            coupon_pattern = 'SUMMER-####-####', ), 
                        referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                            valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                            coupon_pattern = 'SUMMER-####-####', ), 
                        limits = [
                            talon_one.models.limit_config.LimitConfig(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                period = 'yearly', 
                                entities = [Coupon], )
                            ], 
                        campaign_groups = [1, 3], 
                        type = 'advanced', 
                        linked_store_ids = [1, 2, 3], 
                        budgets = [
                            talon_one.models.campaign_budget.CampaignBudget(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                counter = 42.0, )
                            ], 
                        coupon_redemption_count = 163, 
                        referral_redemption_count = 3, 
                        discount_count = 288.0, 
                        discount_effect_count = 343, 
                        coupon_creation_count = 16, 
                        custom_effect_count = 0, 
                        referral_creation_count = 8, 
                        add_free_item_effect_count = 0, 
                        awarded_giveaways_count = 9, 
                        created_loyalty_points_count = 9.0, 
                        created_loyalty_points_effect_count = 2, 
                        redeemed_loyalty_points_count = 8.0, 
                        redeemed_loyalty_points_effect_count = 9, 
                        call_api_effect_count = 0, 
                        reservecoupon_effect_count = 9, 
                        last_activity = '2022-11-10T23:00Z', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = 'John Doe', 
                        updated_by = 'Jane Doe', 
                        template_id = 3, 
                        frontend_state = 'running', 
                        stores_imported = True, )
                    ],
        )

    def testInlineResponse2006(self):
        """Test InlineResponse2006"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
