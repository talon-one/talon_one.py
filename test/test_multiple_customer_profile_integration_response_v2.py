# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.multiple_customer_profile_integration_response_v2 import MultipleCustomerProfileIntegrationResponseV2  # noqa: E501
from talon_one.rest import ApiException

class TestMultipleCustomerProfileIntegrationResponseV2(unittest.TestCase):
    """MultipleCustomerProfileIntegrationResponseV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MultipleCustomerProfileIntegrationResponseV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.multiple_customer_profile_integration_response_v2.MultipleCustomerProfileIntegrationResponseV2()  # noqa: E501
        if include_optional :
            return MultipleCustomerProfileIntegrationResponseV2(
                integration_states = [
                    talon_one.models.integration_state_v2.IntegrationStateV2(
                        customer_session = talon_one.models.customer_session_v2.CustomerSessionV2(
                            id = 6, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            integration_id = 'URNGV8294NV', 
                            application_id = 322, 
                            profile_id = 'URNGV8294NV', 
                            coupon_codes = [XMAS-20-2021], 
                            referral_code = 'NT2K54D9', 
                            loyalty_cards = [loyalty-card-1], 
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
                                    weight = 1130.0, 
                                    height = 1.337, 
                                    width = 1.337, 
                                    length = 1.337, 
                                    position = 1.337, 
                                    attributes = {"image":"11.jpeg","material":"leather"}, 
                                    additional_costs = {"shipping":{"price":9}}, 
                                    catalog_item_id = 56, )
                                ], 
                            additional_costs = {"shipping":{"price":9}}, 
                            identifiers = [91.11.156.141], 
                            attributes = {"ShippingCity":"Berlin"}, 
                            first_session = True, 
                            total = 119.99, 
                            cart_item_total = 99.99, 
                            additional_cost_total = 20.0, 
                            updated = '2020-02-08T14:15:22Z', ), 
                        customer_profile = talon_one.models.customer_profile.CustomerProfile(
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
                            last_activity = '2020-02-08T14:15:20Z', ), 
                        event = talon_one.models.event.Event(
                            id = 6, 
                            created = '2020-06-10T09:05:27.993483Z', 
                            application_id = 322, 
                            profile_id = 'URNGV8294NV', 
                            type = 'pageViews', 
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
                                    status = '0', 
                                    identifier = '0', 
                                    users_per_card_limit = 111, 
                                    profiles = [
                                        talon_one.models.loyalty_card_profile_registration.LoyaltyCardProfileRegistration(
                                            integration_id = '0', 
                                            timestamp = '2021-09-12T10:12:42Z', )
                                        ], 
                                    ledger = talon_one.models.ledger_info.LedgerInfo(
                                        current_balance = 46.0, 
                                        pending_balance = 10.0, 
                                        expired_balance = 30.0, 
                                        spent_balance = 84.0, 
                                        tentative_current_balance = 56.0, 
                                        current_tier = talon_one.models.tier.Tier(
                                            id = 11, 
                                            name = 'bronze', ), 
                                        points_to_next_tier = 20.0, 
                                        projection = talon_one.models.loyalty_projection.LoyaltyProjection(
                                            projections = [
                                                talon_one.models.loyalty_projection_data.LoyaltyProjectionData(
                                                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    expiring_points = 14.0, 
                                                    activating_points = 25.0, 
                                                    projected_balance = 57.0, )
                                                ], 
                                            total_expiring_points = 10.0, 
                                            total_activating_points = 40.0, ), ), 
                                    subledgers = {
                                        'key' : talon_one.models.ledger_info.LedgerInfo(
                                            current_balance = 46.0, 
                                            pending_balance = 10.0, 
                                            expired_balance = 30.0, 
                                            spent_balance = 84.0, 
                                            tentative_current_balance = 56.0, 
                                            points_to_next_tier = 20.0, )
                                        }, 
                                    modified = '2021-09-12T10:12:42Z', )
                                ], 
                            programs = {
                                'key' : talon_one.models.loyalty_program_ledgers.LoyaltyProgramLedgers(
                                    id = 5, 
                                    title = 'My loyalty program', 
                                    name = 'program1', 
                                    ledger = talon_one.models.ledger_info.LedgerInfo(
                                        current_balance = 46.0, 
                                        pending_balance = 10.0, 
                                        expired_balance = 30.0, 
                                        spent_balance = 84.0, 
                                        tentative_current_balance = 56.0, 
                                        points_to_next_tier = 20.0, ), 
                                    sub_ledgers = {
                                        'key' : talon_one.models.ledger_info.LedgerInfo(
                                            current_balance = 46.0, 
                                            pending_balance = 10.0, 
                                            expired_balance = 30.0, 
                                            spent_balance = 84.0, 
                                            tentative_current_balance = 56.0, 
                                            points_to_next_tier = 20.0, )
                                        }, )
                                }, ), 
                        referral = talon_one.models.inventory_referral.InventoryReferral(
                            id = 6, 
                            created = '2020-06-10T09:05:27.993483Z', 
                            start_date = '2020-11-10T23:00Z', 
                            expiry_date = '2021-11-10T23:00Z', 
                            usage_limit = 1, 
                            campaign_id = 78, 
                            advocate_profile_integration_id = 'URNGV8294NV', 
                            friend_profile_integration_id = 'BZGGC2454PA', 
                            attributes = talon_one.models.attributes.attributes(), 
                            import_id = 56, 
                            code = '27G47Y54VH9L', 
                            usage_counter = 1, 
                            batch_id = 'tqyrgahe', 
                            referred_customers = [
                                '0'
                                ], ), 
                        coupons = [
                            talon_one.models.coupon.Coupon(
                                id = 6, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                campaign_id = 211, 
                                value = 'XMAS-20-2021', 
                                usage_limit = 100, 
                                discount_limit = 30.0, 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                limits = [
                                    talon_one.models.limit_config.LimitConfig(
                                        action = 'createCoupon', 
                                        limit = 1000.0, 
                                        period = 'yearly', 
                                        entities = [Coupon], )
                                    ], 
                                usage_counter = 10, 
                                discount_counter = 1.337, 
                                discount_remainder = 1.337, 
                                attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                                referral_id = 326632952, 
                                recipient_integration_id = 'URNGV8294NV', 
                                import_id = 56, 
                                reservation = False, 
                                batch_id = '32535-43255', )
                            ], 
                        triggered_campaigns = [
                            talon_one.models.campaign.Campaign(
                                id = 56, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                application_id = 322, 
                                user_id = 56, 
                                name = 'Summer promotions', 
                                description = 'Campaign for all summer 2021 promotions', 
                                start_time = '2021-07-20T22:00Z', 
                                end_time = '2021-09-22T22:00Z', 
                                attributes = talon_one.models.attributes.attributes(), 
                                state = 'enabled', 
                                active_ruleset_id = 56, 
                                tags = [summer], 
                                features = [coupons, referrals], 
                                coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                                    valid_characters = [A, B, C, D, E, 2, 0], 
                                    coupon_pattern = 'SUMMER-####-####', ), 
                                referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                                    valid_characters = [A, B, C, D, E, 2, 0], 
                                    coupon_pattern = 'SUMMER-####-####', ), 
                                limits = [
                                    talon_one.models.limit_config.LimitConfig(
                                        action = 'createCoupon', 
                                        limit = 1000.0, 
                                        period = 'yearly', 
                                        entities = [Coupon], )
                                    ], 
                                campaign_groups = [1, 3], 
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
                                last_activity = '2022-11-10T23:00Z', 
                                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_by = 'John Doe', 
                                updated_by = 'Jane Doe', 
                                template_id = 3, )
                            ], 
                        effects = [
                            talon_one.models.effect.Effect(
                                campaign_id = 244, 
                                ruleset_id = 73, 
                                rule_index = 2, 
                                rule_name = 'Give 20% discount', 
                                effect_type = 'rejectCoupon', 
                                triggered_by_coupon = 4928, 
                                triggered_for_catalog_item = 786, 
                                props = talon_one.models.effect_props.EffectProps(), )
                            ], 
                        rule_failure_reasons = [
                            talon_one.models.rule_failure_reason.RuleFailureReason(
                                campaign_id = 56, 
                                campaign_name = '0', 
                                ruleset_id = 56, 
                                coupon_id = 4928, 
                                coupon_value = '0', 
                                referral_id = 56, 
                                referral_value = '0', 
                                rule_index = 56, 
                                rule_name = '0', 
                                condition_index = 56, 
                                effect_index = 56, 
                                details = '0', )
                            ], 
                        created_coupons = [
                            talon_one.models.coupon.Coupon(
                                id = 6, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                campaign_id = 211, 
                                value = 'XMAS-20-2021', 
                                usage_limit = 100, 
                                discount_limit = 30.0, 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                usage_counter = 10, 
                                discount_counter = 1.337, 
                                discount_remainder = 1.337, 
                                attributes = talon_one.models.attributes_of_coupon.Attributes of coupon(), 
                                referral_id = 326632952, 
                                recipient_integration_id = 'URNGV8294NV', 
                                import_id = 56, 
                                reservation = False, 
                                batch_id = '32535-43255', )
                            ], 
                        created_referrals = [
                            talon_one.models.referral.Referral(
                                id = 6, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                start_date = '2020-11-10T23:00Z', 
                                expiry_date = '2021-11-10T23:00Z', 
                                usage_limit = 1, 
                                campaign_id = 78, 
                                advocate_profile_integration_id = 'URNGV8294NV', 
                                friend_profile_integration_id = 'BZGGC2454PA', 
                                attributes = talon_one.models.attributes.attributes(), 
                                import_id = 56, 
                                code = '27G47Y54VH9L', 
                                usage_counter = 1, 
                                batch_id = 'tqyrgahe', )
                            ], 
                        awarded_giveaways = [
                            talon_one.models.giveaway.Giveaway(
                                id = 6, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                code = '0', 
                                pool_id = 56, 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                attributes = talon_one.models.attributes.attributes(), 
                                used = True, 
                                import_id = 56, )
                            ], 
                        return = talon_one.models.return.Return(
                            id = 6, 
                            created = '2020-06-10T09:05:27.993483Z', 
                            application_id = 322, 
                            account_id = 3886, 
                            returned_cart_items = [
                                talon_one.models.returned_cart_item.ReturnedCartItem(
                                    position = 2, 
                                    quantity = 1, )
                                ], 
                            event_id = 123, 
                            session_id = 123, 
                            session_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c', 
                            profile_id = 123, 
                            profile_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c', 
                            created_by = 123, ), 
                        previous_returns = [
                            talon_one.models.return.Return(
                                id = 6, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                application_id = 322, 
                                account_id = 3886, 
                                returned_cart_items = [
                                    talon_one.models.returned_cart_item.ReturnedCartItem(
                                        position = 2, 
                                        quantity = 1, )
                                    ], 
                                event_id = 123, 
                                session_id = 123, 
                                session_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c', 
                                profile_id = 123, 
                                profile_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c', 
                                created_by = 123, )
                            ], )
                    ]
            )
        else :
            return MultipleCustomerProfileIntegrationResponseV2(
        )

    def testMultipleCustomerProfileIntegrationResponseV2(self):
        """Test MultipleCustomerProfileIntegrationResponseV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
