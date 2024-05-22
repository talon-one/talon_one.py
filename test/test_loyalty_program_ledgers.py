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
from talon_one.models.loyalty_program_ledgers import LoyaltyProgramLedgers  # noqa: E501
from talon_one.rest import ApiException

class TestLoyaltyProgramLedgers(unittest.TestCase):
    """LoyaltyProgramLedgers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoyaltyProgramLedgers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.loyalty_program_ledgers.LoyaltyProgramLedgers()  # noqa: E501
        if include_optional :
            return LoyaltyProgramLedgers(
                id = 5, 
                title = 'My loyalty program', 
                name = 'program1', 
                join_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                ledger = talon_one.models.ledger_info.LedgerInfo(
                    current_balance = 100.0, 
                    pending_balance = 10.0, 
                    expired_balance = 0.0, 
                    spent_balance = 0.0, 
                    tentative_current_balance = 100.0, 
                    tentative_pending_balance = 20.0, 
                    current_tier = talon_one.models.tier.Tier(
                        id = 11, 
                        name = 'bronze', 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        downgrade_policy = 'one_down', ), 
                    points_to_next_tier = 20.0, ), 
                sub_ledgers = {
                    'key' : talon_one.models.ledger_info.LedgerInfo(
                        current_balance = 100.0, 
                        pending_balance = 10.0, 
                        expired_balance = 0.0, 
                        spent_balance = 0.0, 
                        tentative_current_balance = 100.0, 
                        tentative_pending_balance = 20.0, 
                        current_tier = talon_one.models.tier.Tier(
                            id = 11, 
                            name = 'bronze', 
                            expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            downgrade_policy = 'one_down', ), 
                        points_to_next_tier = 20.0, )
                    }
            )
        else :
            return LoyaltyProgramLedgers(
                id = 5,
                title = 'My loyalty program',
                name = 'program1',
                ledger = talon_one.models.ledger_info.LedgerInfo(
                    current_balance = 100.0, 
                    pending_balance = 10.0, 
                    expired_balance = 0.0, 
                    spent_balance = 0.0, 
                    tentative_current_balance = 100.0, 
                    tentative_pending_balance = 20.0, 
                    current_tier = talon_one.models.tier.Tier(
                        id = 11, 
                        name = 'bronze', 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        downgrade_policy = 'one_down', ), 
                    points_to_next_tier = 20.0, ),
        )

    def testLoyaltyProgramLedgers(self):
        """Test LoyaltyProgramLedgers"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
