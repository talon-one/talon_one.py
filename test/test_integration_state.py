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
from talon_one.models.integration_state import IntegrationState  # noqa: E501
from talon_one.rest import ApiException

class TestIntegrationState(unittest.TestCase):
    """IntegrationState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IntegrationState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.integration_state.IntegrationState()  # noqa: E501
        if include_optional :
            return IntegrationState(
                session = talon_one.models.customer_session.CustomerSession(
                    integration_id = '0', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    application_id = 56, 
                    profile_id = '0', 
                    coupon = '0', 
                    referral = '0', 
                    state = 'open', 
                    cart_items = [
                        talon_one.models.cart_item.CartItem(
                            name = '0', 
                            sku = '0', 
                            quantity = 1, 
                            price = 1.337, 
                            category = '0', 
                            weight = 1.337, 
                            height = 1.337, 
                            width = 1.337, 
                            length = 1.337, 
                            position = 1.337, 
                            attributes = talon_one.models.item_attributes.Item attributes(), )
                        ], 
                    identifiers = [
                        '0'
                        ], 
                    total = 1.337, 
                    attributes = talon_one.models.attributes.attributes(), 
                    first_session = True, 
                    discounts = {
                        'key' : 1.337
                        }, ), 
                profile = talon_one.models.customer_profile.CustomerProfile(
                    integration_id = '0', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    attributes = talon_one.models.attributes.attributes(), 
                    account_id = 56, 
                    closed_sessions = 56, 
                    total_sales = 1.337, 
                    loyalty_memberships = [
                        talon_one.models.loyalty_membership.LoyaltyMembership(
                            joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            loyalty_program_id = 56, )
                        ], 
                    audience_memberships = [
                        talon_one.models.audience_membership.AudienceMembership(
                            id = 56, 
                            name = '0', )
                        ], 
                    last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                event = talon_one.models.event.Event(
                    id = 56, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    application_id = 56, 
                    profile_id = '0', 
                    type = '0', 
                    attributes = talon_one.models.attributes.attributes(), 
                    session_id = '0', 
                    effects = [
                        None
                        ], 
                    ledger_entries = [
                        talon_one.models.ledger_entry.LedgerEntry(
                            id = 56, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            profile_id = '0', 
                            account_id = 56, 
                            loyalty_program_id = 56, 
                            event_id = 56, 
                            amount = 56, 
                            reason = '0', 
                            expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reference_id = 56, )
                        ], 
                    meta = talon_one.models.meta.Meta(
                        campaigns = talon_one.models.campaigns.campaigns(), 
                        coupons = talon_one.models.coupons.coupons(), 
                        coupon_rejection_reason = talon_one.models.coupon_rejection_reason.CouponRejectionReason(
                            campaign_id = 56, 
                            coupon_id = 56, 
                            reason = 'CouponNotFound', ), 
                        referral_rejection_reason = talon_one.models.referral_rejection_reason.ReferralRejectionReason(
                            campaign_id = 56, 
                            referral_id = 56, 
                            reason = 'ReferralNotFound', ), 
                        warnings = talon_one.models.warnings.warnings(), ), ), 
                loyalty = talon_one.models.loyalty.Loyalty(
                    programs = {
                        'key' : talon_one.models.loyalty_program_ledgers.LoyaltyProgramLedgers(
                            id = 56, 
                            title = '0', 
                            name = '0', 
                            ledger = talon_one.models.loyalty_program_balance.LoyaltyProgramBalance(
                                current_balance = 1.337, 
                                pending_balance = 1.337, 
                                expired_balance = 1.337, 
                                spent_balance = 1.337, 
                                tentative_current_balance = 1.337, ), 
                            sub_ledgers = {
                                'key' : talon_one.models.loyalty_program_balance.LoyaltyProgramBalance(
                                    current_balance = 1.337, 
                                    pending_balance = 1.337, 
                                    expired_balance = 1.337, 
                                    spent_balance = 1.337, 
                                    tentative_current_balance = 1.337, )
                                }, )
                        }, ), 
                coupon = talon_one.models.coupon.Coupon(
                    id = 56, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    campaign_id = 56, 
                    value = '0123', 
                    usage_limit = 0, 
                    discount_limit = 0, 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    usage_counter = 56, 
                    discount_counter = 1.337, 
                    discount_remainder = 1.337, 
                    attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                    referral_id = 56, 
                    recipient_integration_id = '0', 
                    import_id = 56, 
                    reservation = True, 
                    batch_id = '0', )
            )
        else :
            return IntegrationState(
                session = talon_one.models.customer_session.CustomerSession(
                    integration_id = '0', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    application_id = 56, 
                    profile_id = '0', 
                    coupon = '0', 
                    referral = '0', 
                    state = 'open', 
                    cart_items = [
                        talon_one.models.cart_item.CartItem(
                            name = '0', 
                            sku = '0', 
                            quantity = 1, 
                            price = 1.337, 
                            category = '0', 
                            weight = 1.337, 
                            height = 1.337, 
                            width = 1.337, 
                            length = 1.337, 
                            position = 1.337, 
                            attributes = talon_one.models.item_attributes.Item attributes(), )
                        ], 
                    identifiers = [
                        '0'
                        ], 
                    total = 1.337, 
                    attributes = talon_one.models.attributes.attributes(), 
                    first_session = True, 
                    discounts = {
                        'key' : 1.337
                        }, ),
                profile = talon_one.models.customer_profile.CustomerProfile(
                    integration_id = '0', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    attributes = talon_one.models.attributes.attributes(), 
                    account_id = 56, 
                    closed_sessions = 56, 
                    total_sales = 1.337, 
                    loyalty_memberships = [
                        talon_one.models.loyalty_membership.LoyaltyMembership(
                            joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            loyalty_program_id = 56, )
                        ], 
                    audience_memberships = [
                        talon_one.models.audience_membership.AudienceMembership(
                            id = 56, 
                            name = '0', )
                        ], 
                    last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                event = talon_one.models.event.Event(
                    id = 56, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    application_id = 56, 
                    profile_id = '0', 
                    type = '0', 
                    attributes = talon_one.models.attributes.attributes(), 
                    session_id = '0', 
                    effects = [
                        None
                        ], 
                    ledger_entries = [
                        talon_one.models.ledger_entry.LedgerEntry(
                            id = 56, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            profile_id = '0', 
                            account_id = 56, 
                            loyalty_program_id = 56, 
                            event_id = 56, 
                            amount = 56, 
                            reason = '0', 
                            expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reference_id = 56, )
                        ], 
                    meta = talon_one.models.meta.Meta(
                        campaigns = talon_one.models.campaigns.campaigns(), 
                        coupons = talon_one.models.coupons.coupons(), 
                        coupon_rejection_reason = talon_one.models.coupon_rejection_reason.CouponRejectionReason(
                            campaign_id = 56, 
                            coupon_id = 56, 
                            reason = 'CouponNotFound', ), 
                        referral_rejection_reason = talon_one.models.referral_rejection_reason.ReferralRejectionReason(
                            campaign_id = 56, 
                            referral_id = 56, 
                            reason = 'ReferralNotFound', ), 
                        warnings = talon_one.models.warnings.warnings(), ), ),
        )

    def testIntegrationState(self):
        """Test IntegrationState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
