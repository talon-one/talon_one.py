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
                            integration_id = '0', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            application_id = 56, 
                            profile_id = '0', 
                            coupon_codes = [
                                '0'
                                ], 
                            referral_code = '0', 
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
                                    attributes = talon_one.models.item_attributes.Item attributes(), 
                                    adjustment = talon_one.models.cart_item_adjustment.CartItemAdjustment(
                                        pay_from_loyalty_program = 56, 
                                        point_payment = 1, 
                                        remaining_price = 0, ), )
                                ], 
                            additional_costs = {
                                'key' : talon_one.models.additional_cost.AdditionalCost(
                                    price = 1.337, )
                                }, 
                            identifiers = [
                                '0'
                                ], 
                            attributes = talon_one.models.attributes.attributes(), 
                            first_session = True, 
                            total = 1.337, 
                            cart_item_total = 1.337, 
                            additional_cost_total = 1.337, ), 
                        customer_profile = talon_one.models.customer_profile.CustomerProfile(
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
                                    title = '0', 
                                    name = '0', 
                                    ledger = talon_one.models.loyalty_program_balance.LoyaltyProgramBalance(
                                        current_balance = 1.337, ), 
                                    sub_ledgers = {
                                        'key' : talon_one.models.loyalty_program_balance.LoyaltyProgramBalance(
                                            current_balance = 1.337, )
                                        }, )
                                }, ), 
                        referral = talon_one.models.referral.Referral(
                            id = 56, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            campaign_id = 56, 
                            advocate_profile_integration_id = '0', 
                            friend_profile_integration_id = '0', 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            code = '0123', 
                            usage_counter = 56, 
                            usage_limit = 0, ), 
                        coupons = [
                            talon_one.models.coupon.Coupon(
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
                            ], 
                        triggered_campaigns = [
                            talon_one.models.campaign.Campaign(
                                id = 56, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                application_id = 56, 
                                user_id = 56, 
                                name = '0', 
                                description = '0', 
                                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                attributes = talon_one.models.attributes.attributes(), 
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
                                updated_by = '0', )
                            ], 
                        effects = [
                            talon_one.models.effect.Effect(
                                campaign_id = 56, 
                                ruleset_id = 56, 
                                rule_index = 56, 
                                rule_name = '0', 
                                effect_type = '0', 
                                props = talon_one.models.effect_props.EffectProps(), )
                            ], 
                        created_coupons = [
                            talon_one.models.coupon.Coupon(
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
                            ], 
                        created_referrals = [
                            talon_one.models.referral.Referral(
                                id = 56, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                campaign_id = 56, 
                                advocate_profile_integration_id = '0', 
                                friend_profile_integration_id = '0', 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                code = '0123', 
                                usage_counter = 56, 
                                usage_limit = 0, )
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
