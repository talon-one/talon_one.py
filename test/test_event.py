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
from talon_one.models.event import Event  # noqa: E501
from talon_one.rest import ApiException

class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Event
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.event.Event()  # noqa: E501
        if include_optional :
            return Event(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                application_id = 322, 
                profile_id = 'URNGV8294NV', 
                store_integration_id = 'STORE-001', 
                type = 'pageViewed', 
                attributes = {"myAttribute":"myValue"}, 
                session_id = '175KJPS947296', 
                effects = [
                    None
                    ], 
                ledger_entries = [
                    talon_one.models.ledger_entry.LedgerEntry(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        profile_id = 'URNGV8294NV', 
                        account_id = 56, 
                        loyalty_program_id = 323414846, 
                        event_id = 3, 
                        amount = 100, 
                        reason = 'Customer appeasement.', 
                        expiry_date = '2022-04-26T11:02:38Z', 
                        reference_id = 56, )
                    ], 
                meta = talon_one.models.meta.Meta(
                    campaigns = talon_one.models.campaigns.campaigns(), 
                    coupons = talon_one.models.coupons.coupons(), 
                    coupon_rejection_reason = talon_one.models.coupon_rejection_reason.CouponRejectionReason(
                        campaign_id = 244, 
                        coupon_id = 4928, 
                        reason = 'CouponNotFound', ), 
                    referral_rejection_reason = talon_one.models.referral_rejection_reason.ReferralRejectionReason(
                        campaign_id = 56, 
                        referral_id = 56, 
                        reason = 'ReferralNotFound', ), 
                    warnings = talon_one.models.warnings.warnings(), )
            )
        else :
            return Event(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                application_id = 322,
                type = 'pageViewed',
                attributes = {"myAttribute":"myValue"},
                effects = [
                    None
                    ],
        )

    def testEvent(self):
        """Test Event"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
