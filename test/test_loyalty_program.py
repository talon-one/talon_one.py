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
from talon_one.models.loyalty_program import LoyaltyProgram  # noqa: E501
from talon_one.rest import ApiException

class TestLoyaltyProgram(unittest.TestCase):
    """LoyaltyProgram unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoyaltyProgram
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.loyalty_program.LoyaltyProgram()  # noqa: E501
        if include_optional :
            return LoyaltyProgram(
                id = 56, 
                created = '2020-06-10T09:05:27.993483Z', 
                title = 'Point collection', 
                description = 'Customers collect 10 points per 1$ spent', 
                subscribed_applications = [132, 97], 
                default_validity = '2W_U', 
                default_pending = 'immediate', 
                allow_subledger = False, 
                users_per_card_limit = 111, 
                sandbox = True, 
                program_join_policy = 'not_join', 
                tiers_expiration_policy = 'tier_start_date', 
                tiers_start_date = '2021-09-12T10:12:42Z', 
                tiers_expire_in = '27W_U', 
                tiers_downgrade_policy = 'one_down', 
                card_code_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                    valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                    coupon_pattern = 'SUMMER-####-####', ), 
                account_id = 1, 
                name = 'my_program', 
                tiers = [{name=Gold, minPoints=300, id=3, created=2021-06-10T09:05:27.993483Z, programID=139}, {name=Silver, minPoints=200, id=2, created=2021-06-10T09:04:59.355258Z, programId=139}, {name=Bronze, minPoints=100, id=1, created=2021-06-10T09:04:39.355258Z, programId=139}], 
                timezone = 'Europe/Berlin', 
                card_based = True, 
                can_update_tiers = True, 
                can_update_join_policy = True, 
                can_update_tier_expiration_policy = True, 
                can_upgrade_to_advanced_tiers = True
            )
        else :
            return LoyaltyProgram(
                id = 56,
                created = '2020-06-10T09:05:27.993483Z',
                title = 'Point collection',
                description = 'Customers collect 10 points per 1$ spent',
                subscribed_applications = [132, 97],
                default_validity = '2W_U',
                default_pending = 'immediate',
                allow_subledger = False,
                sandbox = True,
                account_id = 1,
                name = 'my_program',
                timezone = 'Europe/Berlin',
                card_based = True,
        )

    def testLoyaltyProgram(self):
        """Test LoyaltyProgram"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
