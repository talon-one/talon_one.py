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
                    created = '2020-02-07T08:15:22Z', 
                    application_id = 322, 
                    profile_id = 'URNGV8294NV', 
                    coupon = 'XMAS-2021', 
                    referral = '2740-tbjua-6720', 
                    state = 'open', 
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
                    identifiers = [91.11.156.141], 
                    total = 1.337, 
                    attributes = talon_one.models.attributes.attributes(), 
                    first_session = True, 
                    discounts = {
                        'key' : 1.337
                        }, 
                    updated = '2021-09-12T10:12:42Z', ), 
                profile = talon_one.models.customer_profile.CustomerProfile(
                    id = 6, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    integration_id = 'URNGV8294NV', 
                    attributes = {"Language":"english","ShippingCountry":"DE"}, 
                    account_id = 31, 
                    closed_sessions = 3, 
                    total_sales = 299.99, 
                    loyalty_memberships = [
                        talon_one.models.loyalty_membership.LoyaltyMembership(
                            joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            loyalty_program_id = 323414846, )
                        ], 
                    audience_memberships = [
                        talon_one.models.audience_membership.AudienceMembership(
                            id = 2, 
                            name = 'Travel audience', )
                        ], 
                    last_activity = '2020-02-08T14:15:20Z', 
                    sandbox = False, ), 
                event = talon_one.models.event.Event(
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
                        warnings = talon_one.models.warnings.warnings(), ), ), 
                loyalty = talon_one.models.loyalty.Loyalty(
                    cards = [
                        talon_one.models.loyalty_card.LoyaltyCard(
                            id = 6, 
                            created = '2020-06-10T09:05:27.993483Z', 
                            program_id = 125, 
                            status = 'active', 
                            block_reason = 'Current card lost. Customer needs a new card.', 
                            identifier = 'summer-loyalty-card-0543', 
                            users_per_card_limit = 111, 
                            profiles = [
                                talon_one.models.loyalty_card_profile_registration.LoyaltyCardProfileRegistration(
                                    integration_id = 'R195412', 
                                    timestamp = '2021-09-12T10:12:42Z', )
                                ], 
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
                                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    downgrade_policy = 'one_down', ), 
                                points_to_next_tier = 20.0, ), 
                            subledgers = {
                                'key' : talon_one.models.ledger_info.LedgerInfo(
                                    current_balance = 100.0, 
                                    pending_balance = 10.0, 
                                    expired_balance = 0.0, 
                                    spent_balance = 0.0, 
                                    tentative_current_balance = 100.0, 
                                    tentative_pending_balance = 20.0, 
                                    points_to_next_tier = 20.0, )
                                }, 
                            modified = '2021-09-12T10:12:42Z', 
                            old_card_identifier = 'summer-loyalty-card-0543', 
                            new_card_identifier = 'summer-loyalty-card-0543', )
                        ], 
                    programs = {
                        'key' : talon_one.models.loyalty_program_ledgers.LoyaltyProgramLedgers(
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
                                points_to_next_tier = 20.0, ), 
                            sub_ledgers = {
                                'key' : talon_one.models.ledger_info.LedgerInfo(
                                    current_balance = 100.0, 
                                    pending_balance = 10.0, 
                                    expired_balance = 0.0, 
                                    spent_balance = 0.0, 
                                    tentative_current_balance = 100.0, 
                                    tentative_pending_balance = 20.0, 
                                    points_to_next_tier = 20.0, )
                                }, )
                        }, ), 
                coupon = talon_one.models.coupon.Coupon(
                    id = 6, 
                    created = '2020-06-10T09:05:27.993483Z', 
                    campaign_id = 211, 
                    value = 'XMAS-20-2021', 
                    usage_limit = 100, 
                    discount_limit = 30.0, 
                    reservation_limit = 45, 
                    start_date = '2020-01-24T14:15:22Z', 
                    expiry_date = '2023-08-24T14:15:22Z', 
                    limits = [
                        talon_one.models.limit_config.LimitConfig(
                            action = 'createCoupon', 
                            limit = 1000.0, 
                            period = 'yearly', 
                            entities = [Coupon], )
                        ], 
                    usage_counter = 10, 
                    discount_counter = 10.0, 
                    discount_remainder = 5.0, 
                    reservation_counter = 1.0, 
                    attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                    referral_id = 326632952, 
                    recipient_integration_id = 'URNGV8294NV', 
                    import_id = 4, 
                    reservation = False, 
                    batch_id = '32535-43255', 
                    is_reservation_mandatory = False, 
                    implicitly_reserved = False, )
            )
        else :
            return IntegrationState(
                session = talon_one.models.customer_session.CustomerSession(
                    integration_id = '0', 
                    created = '2020-02-07T08:15:22Z', 
                    application_id = 322, 
                    profile_id = 'URNGV8294NV', 
                    coupon = 'XMAS-2021', 
                    referral = '2740-tbjua-6720', 
                    state = 'open', 
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
                    identifiers = [91.11.156.141], 
                    total = 1.337, 
                    attributes = talon_one.models.attributes.attributes(), 
                    first_session = True, 
                    discounts = {
                        'key' : 1.337
                        }, 
                    updated = '2021-09-12T10:12:42Z', ),
                profile = talon_one.models.customer_profile.CustomerProfile(
                    id = 6, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    integration_id = 'URNGV8294NV', 
                    attributes = {"Language":"english","ShippingCountry":"DE"}, 
                    account_id = 31, 
                    closed_sessions = 3, 
                    total_sales = 299.99, 
                    loyalty_memberships = [
                        talon_one.models.loyalty_membership.LoyaltyMembership(
                            joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            loyalty_program_id = 323414846, )
                        ], 
                    audience_memberships = [
                        talon_one.models.audience_membership.AudienceMembership(
                            id = 2, 
                            name = 'Travel audience', )
                        ], 
                    last_activity = '2020-02-08T14:15:20Z', 
                    sandbox = False, ),
                event = talon_one.models.event.Event(
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
                        warnings = talon_one.models.warnings.warnings(), ), ),
        )

    def testIntegrationState(self):
        """Test IntegrationState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
