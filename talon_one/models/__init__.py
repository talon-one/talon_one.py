# coding: utf-8

# flake8: noqa
"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from talon_one.models.api_error import APIError
from talon_one.models.accept_coupon_effect_props import AcceptCouponEffectProps
from talon_one.models.accept_referral_effect_props import AcceptReferralEffectProps
from talon_one.models.access_log_entry import AccessLogEntry
from talon_one.models.account import Account
from talon_one.models.account_additional_cost import AccountAdditionalCost
from talon_one.models.account_analytics import AccountAnalytics
from talon_one.models.account_entity import AccountEntity
from talon_one.models.account_limits import AccountLimits
from talon_one.models.add_free_item_effect_props import AddFreeItemEffectProps
from talon_one.models.add_loyalty_points_effect_props import AddLoyaltyPointsEffectProps
from talon_one.models.additional_cost import AdditionalCost
from talon_one.models.application import Application
from talon_one.models.application_api_key import ApplicationAPIKey
from talon_one.models.application_api_health import ApplicationApiHealth
from talon_one.models.application_customer import ApplicationCustomer
from talon_one.models.application_customer_entity import ApplicationCustomerEntity
from talon_one.models.application_customer_search import ApplicationCustomerSearch
from talon_one.models.application_entity import ApplicationEntity
from talon_one.models.application_event import ApplicationEvent
from talon_one.models.application_session import ApplicationSession
from talon_one.models.application_session_entity import ApplicationSessionEntity
from talon_one.models.attribute import Attribute
from talon_one.models.attributes_mandatory import AttributesMandatory
from talon_one.models.attributes_settings import AttributesSettings
from talon_one.models.audience import Audience
from talon_one.models.audience_membership import AudienceMembership
from talon_one.models.base_saml_connection import BaseSamlConnection
from talon_one.models.binding import Binding
from talon_one.models.campaign import Campaign
from talon_one.models.campaign_analytics import CampaignAnalytics
from talon_one.models.campaign_copy import CampaignCopy
from talon_one.models.campaign_entity import CampaignEntity
from talon_one.models.campaign_group import CampaignGroup
from talon_one.models.campaign_group_entity import CampaignGroupEntity
from talon_one.models.campaign_search import CampaignSearch
from talon_one.models.campaign_set import CampaignSet
from talon_one.models.campaign_set_branch_node import CampaignSetBranchNode
from talon_one.models.campaign_set_leaf_node import CampaignSetLeafNode
from talon_one.models.campaign_set_node import CampaignSetNode
from talon_one.models.cart_item import CartItem
from talon_one.models.cart_item_adjustment import CartItemAdjustment
from talon_one.models.change import Change
from talon_one.models.change_profile_password import ChangeProfilePassword
from talon_one.models.code_generator_settings import CodeGeneratorSettings
from talon_one.models.coupon import Coupon
from talon_one.models.coupon_constraints import CouponConstraints
from talon_one.models.coupon_created_effect_props import CouponCreatedEffectProps
from talon_one.models.coupon_rejection_reason import CouponRejectionReason
from talon_one.models.coupon_reservations import CouponReservations
from talon_one.models.coupon_search import CouponSearch
from talon_one.models.coupon_value import CouponValue
from talon_one.models.create_application_api_key import CreateApplicationAPIKey
from talon_one.models.customer_activity_report import CustomerActivityReport
from talon_one.models.customer_analytics import CustomerAnalytics
from talon_one.models.customer_inventory import CustomerInventory
from talon_one.models.customer_profile import CustomerProfile
from talon_one.models.customer_profile_audience_request import CustomerProfileAudienceRequest
from talon_one.models.customer_profile_audience_request_item import CustomerProfileAudienceRequestItem
from talon_one.models.customer_profile_integration_request_v2 import CustomerProfileIntegrationRequestV2
from talon_one.models.customer_profile_search_query import CustomerProfileSearchQuery
from talon_one.models.customer_session import CustomerSession
from talon_one.models.customer_session_v2 import CustomerSessionV2
from talon_one.models.deduct_loyalty_points_effect_props import DeductLoyaltyPointsEffectProps
from talon_one.models.effect import Effect
from talon_one.models.effect_entity import EffectEntity
from talon_one.models.email_entity import EmailEntity
from talon_one.models.entity import Entity
from talon_one.models.entity_with_talang_visible_id import EntityWithTalangVisibleID
from talon_one.models.environment import Environment
from talon_one.models.error_effect_props import ErrorEffectProps
from talon_one.models.error_response import ErrorResponse
from talon_one.models.error_source import ErrorSource
from talon_one.models.event import Event
from talon_one.models.event_type import EventType
from talon_one.models.export import Export
from talon_one.models.feature_flag import FeatureFlag
from talon_one.models.feature_flags import FeatureFlags
from talon_one.models.features_feed import FeaturesFeed
from talon_one.models.feed_notification import FeedNotification
from talon_one.models.func_arg_def import FuncArgDef
from talon_one.models.function_def import FunctionDef
from talon_one.models.import_coupons import ImportCoupons
from talon_one.models.inline_response200 import InlineResponse200
from talon_one.models.inline_response2001 import InlineResponse2001
from talon_one.models.inline_response20010 import InlineResponse20010
from talon_one.models.inline_response20011 import InlineResponse20011
from talon_one.models.inline_response20012 import InlineResponse20012
from talon_one.models.inline_response20013 import InlineResponse20013
from talon_one.models.inline_response20014 import InlineResponse20014
from talon_one.models.inline_response20015 import InlineResponse20015
from talon_one.models.inline_response20016 import InlineResponse20016
from talon_one.models.inline_response20017 import InlineResponse20017
from talon_one.models.inline_response20018 import InlineResponse20018
from talon_one.models.inline_response20019 import InlineResponse20019
from talon_one.models.inline_response2002 import InlineResponse2002
from talon_one.models.inline_response20020 import InlineResponse20020
from talon_one.models.inline_response20021 import InlineResponse20021
from talon_one.models.inline_response20022 import InlineResponse20022
from talon_one.models.inline_response20023 import InlineResponse20023
from talon_one.models.inline_response20024 import InlineResponse20024
from talon_one.models.inline_response20025 import InlineResponse20025
from talon_one.models.inline_response20026 import InlineResponse20026
from talon_one.models.inline_response20027 import InlineResponse20027
from talon_one.models.inline_response20028 import InlineResponse20028
from talon_one.models.inline_response20029 import InlineResponse20029
from talon_one.models.inline_response2003 import InlineResponse2003
from talon_one.models.inline_response20030 import InlineResponse20030
from talon_one.models.inline_response2004 import InlineResponse2004
from talon_one.models.inline_response2005 import InlineResponse2005
from talon_one.models.inline_response2006 import InlineResponse2006
from talon_one.models.inline_response2007 import InlineResponse2007
from talon_one.models.inline_response2008 import InlineResponse2008
from talon_one.models.inline_response2009 import InlineResponse2009
from talon_one.models.integration_entity import IntegrationEntity
from talon_one.models.integration_event import IntegrationEvent
from talon_one.models.integration_profile_entity import IntegrationProfileEntity
from talon_one.models.integration_request import IntegrationRequest
from talon_one.models.integration_state import IntegrationState
from talon_one.models.integration_state_v2 import IntegrationStateV2
from talon_one.models.ledger_entry import LedgerEntry
from talon_one.models.library_attribute import LibraryAttribute
from talon_one.models.limit_config import LimitConfig
from talon_one.models.login_params import LoginParams
from talon_one.models.loyalty import Loyalty
from talon_one.models.loyalty_ledger import LoyaltyLedger
from talon_one.models.loyalty_ledger_entry import LoyaltyLedgerEntry
from talon_one.models.loyalty_membership import LoyaltyMembership
from talon_one.models.loyalty_points import LoyaltyPoints
from talon_one.models.loyalty_program import LoyaltyProgram
from talon_one.models.loyalty_program_balance import LoyaltyProgramBalance
from talon_one.models.loyalty_program_ledgers import LoyaltyProgramLedgers
from talon_one.models.loyalty_statistics import LoyaltyStatistics
from talon_one.models.loyalty_sub_ledger import LoyaltySubLedger
from talon_one.models.manager_config import ManagerConfig
from talon_one.models.meta import Meta
from talon_one.models.model_import import ModelImport
from talon_one.models.multi_application_entity import MultiApplicationEntity
from talon_one.models.multiple_customer_profile_integration_request import MultipleCustomerProfileIntegrationRequest
from talon_one.models.multiple_customer_profile_integration_request_item import MultipleCustomerProfileIntegrationRequestItem
from talon_one.models.multiple_customer_profile_integration_response_v2 import MultipleCustomerProfileIntegrationResponseV2
from talon_one.models.mutable_entity import MutableEntity
from talon_one.models.new_account import NewAccount
from talon_one.models.new_account_sign_up import NewAccountSignUp
from talon_one.models.new_additional_cost import NewAdditionalCost
from talon_one.models.new_application import NewApplication
from talon_one.models.new_application_api_key import NewApplicationAPIKey
from talon_one.models.new_attribute import NewAttribute
from talon_one.models.new_audience import NewAudience
from talon_one.models.new_campaign import NewCampaign
from talon_one.models.new_campaign_group import NewCampaignGroup
from talon_one.models.new_campaign_set import NewCampaignSet
from talon_one.models.new_coupons import NewCoupons
from talon_one.models.new_customer_profile import NewCustomerProfile
from talon_one.models.new_customer_session import NewCustomerSession
from talon_one.models.new_customer_session_v2 import NewCustomerSessionV2
from talon_one.models.new_event import NewEvent
from talon_one.models.new_event_type import NewEventType
from talon_one.models.new_feature_flags import NewFeatureFlags
from talon_one.models.new_import import NewImport
from talon_one.models.new_invitation import NewInvitation
from talon_one.models.new_invite_email import NewInviteEmail
from talon_one.models.new_loyalty_program import NewLoyaltyProgram
from talon_one.models.new_password import NewPassword
from talon_one.models.new_password_email import NewPasswordEmail
from talon_one.models.new_referral import NewReferral
from talon_one.models.new_role import NewRole
from talon_one.models.new_ruleset import NewRuleset
from talon_one.models.new_saml_connection import NewSamlConnection
from talon_one.models.new_template_def import NewTemplateDef
from talon_one.models.new_user import NewUser
from talon_one.models.new_webhook import NewWebhook
from talon_one.models.notification import Notification
from talon_one.models.redeem_referral_effect_props import RedeemReferralEffectProps
from talon_one.models.referral import Referral
from talon_one.models.referral_created_effect_props import ReferralCreatedEffectProps
from talon_one.models.referral_rejection_reason import ReferralRejectionReason
from talon_one.models.reject_coupon_effect_props import RejectCouponEffectProps
from talon_one.models.reject_referral_effect_props import RejectReferralEffectProps
from talon_one.models.role import Role
from talon_one.models.role_assign import RoleAssign
from talon_one.models.role_membership import RoleMembership
from talon_one.models.rollback_coupon_effect_props import RollbackCouponEffectProps
from talon_one.models.rollback_discount_effect_props import RollbackDiscountEffectProps
from talon_one.models.rule import Rule
from talon_one.models.ruleset import Ruleset
from talon_one.models.saml_connection import SamlConnection
from talon_one.models.saml_connection_metadata import SamlConnectionMetadata
from talon_one.models.saml_login_endpoint import SamlLoginEndpoint
from talon_one.models.session import Session
from talon_one.models.set_discount_effect_props import SetDiscountEffectProps
from talon_one.models.set_discount_per_item_effect_props import SetDiscountPerItemEffectProps
from talon_one.models.show_bundle_metadata_effect_props import ShowBundleMetadataEffectProps
from talon_one.models.show_notification_effect_props import ShowNotificationEffectProps
from talon_one.models.slot_def import SlotDef
from talon_one.models.template_arg_def import TemplateArgDef
from talon_one.models.template_def import TemplateDef
from talon_one.models.trigger_webhook_effect_props import TriggerWebhookEffectProps
from talon_one.models.update_account import UpdateAccount
from talon_one.models.update_application import UpdateApplication
from talon_one.models.update_attribute_effect_props import UpdateAttributeEffectProps
from talon_one.models.update_audience import UpdateAudience
from talon_one.models.update_campaign import UpdateCampaign
from talon_one.models.update_campaign_group import UpdateCampaignGroup
from talon_one.models.update_coupon import UpdateCoupon
from talon_one.models.update_coupon_batch import UpdateCouponBatch
from talon_one.models.update_loyalty_program import UpdateLoyaltyProgram
from talon_one.models.update_role import UpdateRole
from talon_one.models.update_user import UpdateUser
from talon_one.models.update_user_latest_feed_timestamp import UpdateUserLatestFeedTimestamp
from talon_one.models.user import User
from talon_one.models.user_entity import UserEntity
from talon_one.models.user_feed_notifications import UserFeedNotifications
from talon_one.models.webhook import Webhook
from talon_one.models.webhook_activation_log_entry import WebhookActivationLogEntry
from talon_one.models.webhook_log_entry import WebhookLogEntry
