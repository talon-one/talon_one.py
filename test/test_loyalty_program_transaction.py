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
from talon_one.models.loyalty_program_transaction import LoyaltyProgramTransaction  # noqa: E501
from talon_one.rest import ApiException

class TestLoyaltyProgramTransaction(unittest.TestCase):
    """LoyaltyProgramTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoyaltyProgramTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.loyalty_program_transaction.LoyaltyProgramTransaction()  # noqa: E501
        if include_optional :
            return LoyaltyProgramTransaction(
                id = 123, 
                program_id = 324, 
                campaign_id = 324, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                type = 'addition', 
                amount = 10.25, 
                name = 'Reward 50 points for each $500 purchase', 
                start_date = '2022-01-02T15:04:05Z07:00', 
                expiry_date = '2022-01-02T15:04:05Z07:00', 
                customer_profile_id = 'kda0fajs0-fad9f-fd9dfsa9-fd9dasjf9', 
                card_identifier = 'summer-loyalty-card-0543', 
                subledger_id = 'sub-123', 
                customer_session_id = '05c2da0d-48fa-4aa1-b629-898f58f1584d', 
                import_id = 4, 
                user_id = 5, 
                user_email = 'john.doe@example.com', 
                ruleset_id = 11, 
                rule_name = '10 points for every $100 spent', 
                flags = talon_one.models.loyalty_ledger_entry_flags.LoyaltyLedgerEntryFlags(
                    creates_negative_balance = True, )
            )
        else :
            return LoyaltyProgramTransaction(
                id = 123,
                program_id = 324,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'addition',
                amount = 10.25,
                name = 'Reward 50 points for each $500 purchase',
                start_date = '2022-01-02T15:04:05Z07:00',
                expiry_date = '2022-01-02T15:04:05Z07:00',
                subledger_id = 'sub-123',
        )

    def testLoyaltyProgramTransaction(self):
        """Test LoyaltyProgramTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
