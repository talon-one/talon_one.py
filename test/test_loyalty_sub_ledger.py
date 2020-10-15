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
from talon_one.models.loyalty_sub_ledger import LoyaltySubLedger  # noqa: E501
from talon_one.rest import ApiException

class TestLoyaltySubLedger(unittest.TestCase):
    """LoyaltySubLedger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoyaltySubLedger
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.loyalty_sub_ledger.LoyaltySubLedger()  # noqa: E501
        if include_optional :
            return LoyaltySubLedger(
                total = 1.337, 
                total_active_points = 1.337, 
                total_pending_points = 1.337, 
                total_spent_points = 1.337, 
                total_expired_points = 1.337, 
                transactions = [
                    talon_one.models.loyalty_ledger_entry.LoyaltyLedgerEntry(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        program_id = 56, 
                        customer_profile_id = '0', 
                        customer_session_id = '0', 
                        event_id = 56, 
                        type = '0', 
                        amount = 1.337, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        sub_ledger_id = '0', 
                        user_id = 56, )
                    ], 
                expiring_points = [
                    talon_one.models.loyalty_ledger_entry.LoyaltyLedgerEntry(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        program_id = 56, 
                        customer_profile_id = '0', 
                        customer_session_id = '0', 
                        event_id = 56, 
                        type = '0', 
                        amount = 1.337, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        sub_ledger_id = '0', 
                        user_id = 56, )
                    ], 
                active_points = [
                    talon_one.models.loyalty_ledger_entry.LoyaltyLedgerEntry(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        program_id = 56, 
                        customer_profile_id = '0', 
                        customer_session_id = '0', 
                        event_id = 56, 
                        type = '0', 
                        amount = 1.337, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        sub_ledger_id = '0', 
                        user_id = 56, )
                    ], 
                pending_points = [
                    talon_one.models.loyalty_ledger_entry.LoyaltyLedgerEntry(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        program_id = 56, 
                        customer_profile_id = '0', 
                        customer_session_id = '0', 
                        event_id = 56, 
                        type = '0', 
                        amount = 1.337, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        sub_ledger_id = '0', 
                        user_id = 56, )
                    ], 
                expired_points = [
                    talon_one.models.loyalty_ledger_entry.LoyaltyLedgerEntry(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        program_id = 56, 
                        customer_profile_id = '0', 
                        customer_session_id = '0', 
                        event_id = 56, 
                        type = '0', 
                        amount = 1.337, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        sub_ledger_id = '0', 
                        user_id = 56, )
                    ]
            )
        else :
            return LoyaltySubLedger(
                total = 1.337,
                total_active_points = 1.337,
                total_pending_points = 1.337,
                total_spent_points = 1.337,
                total_expired_points = 1.337,
        )

    def testLoyaltySubLedger(self):
        """Test LoyaltySubLedger"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
