# coding: utf-8

# flake8: noqa

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "7.0.0"

# import apis into sdk package
from talon_one.api.integration_api import IntegrationApi
from talon_one.api.management_api import ManagementApi

# import ApiClient
from talon_one.api_client import ApiClient
from talon_one.configuration import Configuration
from talon_one.exceptions import OpenApiException
from talon_one.exceptions import ApiTypeError
from talon_one.exceptions import ApiValueError
from talon_one.exceptions import ApiKeyError
from talon_one.exceptions import ApiException
# import models into sdk package
from talon_one.models.api_error import APIError
from talon_one.models.accept_coupon_effect_props import AcceptCouponEffectProps
from talon_one.models.accept_referral_effect_props import AcceptReferralEffectProps
from talon_one.models.access_log_entry import AccessLogEntry
from talon_one.models.account import Account
from talon_one.models.account_additional_cost import AccountAdditionalCost
from talon_one.models.account_analytics import AccountAnalytics
from talon_one.models.account_dashboard_statistic import AccountDashboardStatistic
from talon_one.models.account_dashboard_statistic_campaigns import AccountDashboardStatisticCampaigns
from talon_one.models.account_dashboard_statistic_discount import AccountDashboardStatisticDiscount
from talon_one.models.account_dashboard_statistic_loyalty_points import AccountDashboardStatisticLoyaltyPoints
from talon_one.models.account_dashboard_statistic_referrals import AccountDashboardStatisticReferrals
from talon_one.models.account_dashboard_statistic_revenue import AccountDashboardStatisticRevenue
from talon_one.models.account_entity import AccountEntity
from talon_one.models.account_limits import AccountLimits
from talon_one.models.achievement import Achievement
from talon_one.models.achievement_additional_properties import AchievementAdditionalProperties
from talon_one.models.achievement_progress import AchievementProgress
from talon_one.models.add_free_item_effect_props import AddFreeItemEffectProps
from talon_one.models.add_item_catalog_action import AddItemCatalogAction
from talon_one.models.add_loyalty_points import AddLoyaltyPoints
from talon_one.models.add_loyalty_points_effect_props import AddLoyaltyPointsEffectProps
from talon_one.models.add_to_audience_effect_props import AddToAudienceEffectProps
from talon_one.models.added_deducted_points_notification_policy import AddedDeductedPointsNotificationPolicy
from talon_one.models.additional_campaign_properties import AdditionalCampaignProperties
from talon_one.models.additional_cost import AdditionalCost
from talon_one.models.analytics_data_point import AnalyticsDataPoint
from talon_one.models.analytics_data_point_with_trend import AnalyticsDataPointWithTrend
from talon_one.models.analytics_data_point_with_trend_and_influenced_rate import AnalyticsDataPointWithTrendAndInfluencedRate
from talon_one.models.analytics_data_point_with_trend_and_uplift import AnalyticsDataPointWithTrendAndUplift
from talon_one.models.analytics_product import AnalyticsProduct
from talon_one.models.analytics_product_sku import AnalyticsProductSKU
from talon_one.models.application import Application
from talon_one.models.application_api_key import ApplicationAPIKey
from talon_one.models.application_analytics_data_point import ApplicationAnalyticsDataPoint
from talon_one.models.application_api_health import ApplicationApiHealth
from talon_one.models.application_cif import ApplicationCIF
from talon_one.models.application_cif_expression import ApplicationCIFExpression
from talon_one.models.application_campaign_analytics import ApplicationCampaignAnalytics
from talon_one.models.application_campaign_stats import ApplicationCampaignStats
from talon_one.models.application_customer import ApplicationCustomer
from talon_one.models.application_customer_entity import ApplicationCustomerEntity
from talon_one.models.application_entity import ApplicationEntity
from talon_one.models.application_event import ApplicationEvent
from talon_one.models.application_notification import ApplicationNotification
from talon_one.models.application_referee import ApplicationReferee
from talon_one.models.application_session import ApplicationSession
from talon_one.models.application_session_entity import ApplicationSessionEntity
from talon_one.models.application_store_entity import ApplicationStoreEntity
from talon_one.models.async_coupon_creation_response import AsyncCouponCreationResponse
from talon_one.models.async_coupon_deletion_job_response import AsyncCouponDeletionJobResponse
from talon_one.models.attribute import Attribute
from talon_one.models.attributes_mandatory import AttributesMandatory
from talon_one.models.attributes_settings import AttributesSettings
from talon_one.models.audience import Audience
from talon_one.models.audience_analytics import AudienceAnalytics
from talon_one.models.audience_customer import AudienceCustomer
from talon_one.models.audience_integration_id import AudienceIntegrationID
from talon_one.models.audience_membership import AudienceMembership
from talon_one.models.award_giveaway_effect_props import AwardGiveawayEffectProps
from talon_one.models.base_campaign import BaseCampaign
from talon_one.models.base_loyalty_program import BaseLoyaltyProgram
from talon_one.models.base_notification import BaseNotification
from talon_one.models.base_notification_entity import BaseNotificationEntity
from talon_one.models.base_notification_webhook import BaseNotificationWebhook
from talon_one.models.base_notifications import BaseNotifications
from talon_one.models.base_saml_connection import BaseSamlConnection
from talon_one.models.binding import Binding
from talon_one.models.bulk_application_notification import BulkApplicationNotification
from talon_one.models.bulk_campaign_notification import BulkCampaignNotification
from talon_one.models.bulk_operation_on_campaigns import BulkOperationOnCampaigns
from talon_one.models.campaign import Campaign
from talon_one.models.campaign_activation_request import CampaignActivationRequest
from talon_one.models.campaign_analytics import CampaignAnalytics
from talon_one.models.campaign_budget import CampaignBudget
from talon_one.models.campaign_collection import CampaignCollection
from talon_one.models.campaign_collection_edited_notification import CampaignCollectionEditedNotification
from talon_one.models.campaign_collection_without_payload import CampaignCollectionWithoutPayload
from talon_one.models.campaign_copy import CampaignCopy
from talon_one.models.campaign_created_notification import CampaignCreatedNotification
from talon_one.models.campaign_deleted_notification import CampaignDeletedNotification
from talon_one.models.campaign_edited_notification import CampaignEditedNotification
from talon_one.models.campaign_entity import CampaignEntity
from talon_one.models.campaign_evaluation_group import CampaignEvaluationGroup
from talon_one.models.campaign_evaluation_position import CampaignEvaluationPosition
from talon_one.models.campaign_evaluation_tree_changed_notification import CampaignEvaluationTreeChangedNotification
from talon_one.models.campaign_group import CampaignGroup
from talon_one.models.campaign_group_entity import CampaignGroupEntity
from talon_one.models.campaign_notification import CampaignNotification
from talon_one.models.campaign_notification_policy import CampaignNotificationPolicy
from talon_one.models.campaign_ruleset_changed_notification import CampaignRulesetChangedNotification
from talon_one.models.campaign_search import CampaignSearch
from talon_one.models.campaign_set import CampaignSet
from talon_one.models.campaign_set_branch_node import CampaignSetBranchNode
from talon_one.models.campaign_set_leaf_node import CampaignSetLeafNode
from talon_one.models.campaign_set_node import CampaignSetNode
from talon_one.models.campaign_state_changed_notification import CampaignStateChangedNotification
from talon_one.models.campaign_store_budget import CampaignStoreBudget
from talon_one.models.campaign_template import CampaignTemplate
from talon_one.models.campaign_template_collection import CampaignTemplateCollection
from talon_one.models.campaign_template_coupon_reservation_settings import CampaignTemplateCouponReservationSettings
from talon_one.models.campaign_template_params import CampaignTemplateParams
from talon_one.models.campaign_versions import CampaignVersions
from talon_one.models.card_added_deducted_points_notification_policy import CardAddedDeductedPointsNotificationPolicy
from talon_one.models.card_expiring_points_notification_policy import CardExpiringPointsNotificationPolicy
from talon_one.models.card_expiring_points_notification_trigger import CardExpiringPointsNotificationTrigger
from talon_one.models.card_ledger_points_entry_integration_api import CardLedgerPointsEntryIntegrationAPI
from talon_one.models.card_ledger_transaction_log_entry import CardLedgerTransactionLogEntry
from talon_one.models.card_ledger_transaction_log_entry_integration_api import CardLedgerTransactionLogEntryIntegrationAPI
from talon_one.models.cart_item import CartItem
from talon_one.models.catalog import Catalog
from talon_one.models.catalog_action import CatalogAction
from talon_one.models.catalog_action_filter import CatalogActionFilter
from talon_one.models.catalog_item import CatalogItem
from talon_one.models.catalog_sync_request import CatalogSyncRequest
from talon_one.models.catalogs_strikethrough_notification_policy import CatalogsStrikethroughNotificationPolicy
from talon_one.models.change import Change
from talon_one.models.change_loyalty_tier_level_effect_props import ChangeLoyaltyTierLevelEffectProps
from talon_one.models.change_profile_password import ChangeProfilePassword
from talon_one.models.code_generator_settings import CodeGeneratorSettings
from talon_one.models.collection import Collection
from talon_one.models.collection_item import CollectionItem
from talon_one.models.collection_without_payload import CollectionWithoutPayload
from talon_one.models.coupon import Coupon
from talon_one.models.coupon_constraints import CouponConstraints
from talon_one.models.coupon_created_effect_props import CouponCreatedEffectProps
from talon_one.models.coupon_creation_job import CouponCreationJob
from talon_one.models.coupon_deletion_filters import CouponDeletionFilters
from talon_one.models.coupon_deletion_job import CouponDeletionJob
from talon_one.models.coupon_limit_configs import CouponLimitConfigs
from talon_one.models.coupon_rejection_reason import CouponRejectionReason
from talon_one.models.coupon_reservations import CouponReservations
from talon_one.models.coupon_search import CouponSearch
from talon_one.models.coupon_value import CouponValue
from talon_one.models.coupons_notification_policy import CouponsNotificationPolicy
from talon_one.models.create_achievement import CreateAchievement
from talon_one.models.create_application_api_key import CreateApplicationAPIKey
from talon_one.models.create_management_key import CreateManagementKey
from talon_one.models.create_template_campaign import CreateTemplateCampaign
from talon_one.models.create_template_campaign_response import CreateTemplateCampaignResponse
from talon_one.models.custom_effect import CustomEffect
from talon_one.models.custom_effect_props import CustomEffectProps
from talon_one.models.customer_activity_report import CustomerActivityReport
from talon_one.models.customer_analytics import CustomerAnalytics
from talon_one.models.customer_inventory import CustomerInventory
from talon_one.models.customer_profile import CustomerProfile
from talon_one.models.customer_profile_audience_request import CustomerProfileAudienceRequest
from talon_one.models.customer_profile_audience_request_item import CustomerProfileAudienceRequestItem
from talon_one.models.customer_profile_integration_request_v2 import CustomerProfileIntegrationRequestV2
from talon_one.models.customer_profile_integration_response_v2 import CustomerProfileIntegrationResponseV2
from talon_one.models.customer_profile_search_query import CustomerProfileSearchQuery
from talon_one.models.customer_profile_update_v2_response import CustomerProfileUpdateV2Response
from talon_one.models.customer_session import CustomerSession
from talon_one.models.customer_session_v2 import CustomerSessionV2
from talon_one.models.deactivate_user_request import DeactivateUserRequest
from talon_one.models.deduct_loyalty_points import DeductLoyaltyPoints
from talon_one.models.deduct_loyalty_points_effect_props import DeductLoyaltyPointsEffectProps
from talon_one.models.effect import Effect
from talon_one.models.effect_entity import EffectEntity
from talon_one.models.email_entity import EmailEntity
from talon_one.models.endpoint import Endpoint
from talon_one.models.entity import Entity
from talon_one.models.entity_with_talang_visible_id import EntityWithTalangVisibleID
from talon_one.models.environment import Environment
from talon_one.models.error_effect_props import ErrorEffectProps
from talon_one.models.error_response import ErrorResponse
from talon_one.models.error_response_with_status import ErrorResponseWithStatus
from talon_one.models.error_source import ErrorSource
from talon_one.models.evaluable_campaign_ids import EvaluableCampaignIds
from talon_one.models.event import Event
from talon_one.models.event_type import EventType
from talon_one.models.event_v2 import EventV2
from talon_one.models.expiring_coupons_notification_policy import ExpiringCouponsNotificationPolicy
from talon_one.models.expiring_coupons_notification_trigger import ExpiringCouponsNotificationTrigger
from talon_one.models.expiring_points_notification_policy import ExpiringPointsNotificationPolicy
from talon_one.models.expiring_points_notification_trigger import ExpiringPointsNotificationTrigger
from talon_one.models.export import Export
from talon_one.models.feature_flag import FeatureFlag
from talon_one.models.features_feed import FeaturesFeed
from talon_one.models.func_arg_def import FuncArgDef
from talon_one.models.function_def import FunctionDef
from talon_one.models.generate_campaign_description import GenerateCampaignDescription
from talon_one.models.generate_campaign_tags import GenerateCampaignTags
from talon_one.models.generate_item_filter_description import GenerateItemFilterDescription
from talon_one.models.generate_loyalty_card import GenerateLoyaltyCard
from talon_one.models.generate_rule_title import GenerateRuleTitle
from talon_one.models.generate_rule_title_rule import GenerateRuleTitleRule
from talon_one.models.get_integration_coupon_request import GetIntegrationCouponRequest
from talon_one.models.giveaway import Giveaway
from talon_one.models.giveaways_pool import GiveawaysPool
from talon_one.models.identifiable_entity import IdentifiableEntity
from talon_one.models.import_entity import ImportEntity
from talon_one.models.increase_achievement_progress_effect_props import IncreaseAchievementProgressEffectProps
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
from talon_one.models.inline_response20031 import InlineResponse20031
from talon_one.models.inline_response20032 import InlineResponse20032
from talon_one.models.inline_response20033 import InlineResponse20033
from talon_one.models.inline_response20034 import InlineResponse20034
from talon_one.models.inline_response20035 import InlineResponse20035
from talon_one.models.inline_response20036 import InlineResponse20036
from talon_one.models.inline_response20037 import InlineResponse20037
from talon_one.models.inline_response20038 import InlineResponse20038
from talon_one.models.inline_response20039 import InlineResponse20039
from talon_one.models.inline_response2004 import InlineResponse2004
from talon_one.models.inline_response20040 import InlineResponse20040
from talon_one.models.inline_response20041 import InlineResponse20041
from talon_one.models.inline_response20042 import InlineResponse20042
from talon_one.models.inline_response20043 import InlineResponse20043
from talon_one.models.inline_response20044 import InlineResponse20044
from talon_one.models.inline_response20045 import InlineResponse20045
from talon_one.models.inline_response20046 import InlineResponse20046
from talon_one.models.inline_response2005 import InlineResponse2005
from talon_one.models.inline_response2006 import InlineResponse2006
from talon_one.models.inline_response2007 import InlineResponse2007
from talon_one.models.inline_response2008 import InlineResponse2008
from talon_one.models.inline_response2009 import InlineResponse2009
from talon_one.models.inline_response201 import InlineResponse201
from talon_one.models.integration_coupon import IntegrationCoupon
from talon_one.models.integration_customer_session_response import IntegrationCustomerSessionResponse
from talon_one.models.integration_entity import IntegrationEntity
from talon_one.models.integration_event import IntegrationEvent
from talon_one.models.integration_event_v2_request import IntegrationEventV2Request
from talon_one.models.integration_profile_entity import IntegrationProfileEntity
from talon_one.models.integration_request import IntegrationRequest
from talon_one.models.integration_state import IntegrationState
from talon_one.models.integration_state_v2 import IntegrationStateV2
from talon_one.models.integration_store_entity import IntegrationStoreEntity
from talon_one.models.inventory_coupon import InventoryCoupon
from talon_one.models.inventory_referral import InventoryReferral
from talon_one.models.item_attribute import ItemAttribute
from talon_one.models.ledger_entry import LedgerEntry
from talon_one.models.ledger_info import LedgerInfo
from talon_one.models.ledger_points_entry_integration_api import LedgerPointsEntryIntegrationAPI
from talon_one.models.ledger_transaction_log_entry_integration_api import LedgerTransactionLogEntryIntegrationAPI
from talon_one.models.library_attribute import LibraryAttribute
from talon_one.models.limit_config import LimitConfig
from talon_one.models.limit_counter import LimitCounter
from talon_one.models.list_campaign_store_budgets import ListCampaignStoreBudgets
from talon_one.models.list_campaign_store_budgets_store import ListCampaignStoreBudgetsStore
from talon_one.models.login_params import LoginParams
from talon_one.models.loyalty import Loyalty
from talon_one.models.loyalty_balance import LoyaltyBalance
from talon_one.models.loyalty_balance_with_tier import LoyaltyBalanceWithTier
from talon_one.models.loyalty_balances import LoyaltyBalances
from talon_one.models.loyalty_balances_with_tiers import LoyaltyBalancesWithTiers
from talon_one.models.loyalty_card import LoyaltyCard
from talon_one.models.loyalty_card_balances import LoyaltyCardBalances
from talon_one.models.loyalty_card_batch import LoyaltyCardBatch
from talon_one.models.loyalty_card_batch_response import LoyaltyCardBatchResponse
from talon_one.models.loyalty_card_profile_registration import LoyaltyCardProfileRegistration
from talon_one.models.loyalty_card_registration import LoyaltyCardRegistration
from talon_one.models.loyalty_dashboard_data import LoyaltyDashboardData
from talon_one.models.loyalty_dashboard_points_breakdown import LoyaltyDashboardPointsBreakdown
from talon_one.models.loyalty_ledger import LoyaltyLedger
from talon_one.models.loyalty_ledger_entry import LoyaltyLedgerEntry
from talon_one.models.loyalty_ledger_transactions import LoyaltyLedgerTransactions
from talon_one.models.loyalty_membership import LoyaltyMembership
from talon_one.models.loyalty_program import LoyaltyProgram
from talon_one.models.loyalty_program_balance import LoyaltyProgramBalance
from talon_one.models.loyalty_program_entity import LoyaltyProgramEntity
from talon_one.models.loyalty_program_ledgers import LoyaltyProgramLedgers
from talon_one.models.loyalty_program_transaction import LoyaltyProgramTransaction
from talon_one.models.loyalty_sub_ledger import LoyaltySubLedger
from talon_one.models.loyalty_tier import LoyaltyTier
from talon_one.models.management_key import ManagementKey
from talon_one.models.manager_config import ManagerConfig
from talon_one.models.message_log_entries import MessageLogEntries
from talon_one.models.message_log_entry import MessageLogEntry
from talon_one.models.message_log_request import MessageLogRequest
from talon_one.models.message_log_response import MessageLogResponse
from talon_one.models.meta import Meta
from talon_one.models.model_import import ModelImport
from talon_one.models.model_return import ModelReturn
from talon_one.models.multi_application_entity import MultiApplicationEntity
from talon_one.models.multiple_attribute import MultipleAttribute
from talon_one.models.multiple_audiences import MultipleAudiences
from talon_one.models.multiple_audiences_item import MultipleAudiencesItem
from talon_one.models.multiple_customer_profile_integration_request import MultipleCustomerProfileIntegrationRequest
from talon_one.models.multiple_customer_profile_integration_request_item import MultipleCustomerProfileIntegrationRequestItem
from talon_one.models.multiple_customer_profile_integration_response_v2 import MultipleCustomerProfileIntegrationResponseV2
from talon_one.models.multiple_new_attribute import MultipleNewAttribute
from talon_one.models.multiple_new_audiences import MultipleNewAudiences
from talon_one.models.mutable_entity import MutableEntity
from talon_one.models.new_account import NewAccount
from talon_one.models.new_account_sign_up import NewAccountSignUp
from talon_one.models.new_additional_cost import NewAdditionalCost
from talon_one.models.new_app_wide_coupon_deletion_job import NewAppWideCouponDeletionJob
from talon_one.models.new_application import NewApplication
from talon_one.models.new_application_api_key import NewApplicationAPIKey
from talon_one.models.new_application_cif import NewApplicationCIF
from talon_one.models.new_application_cif_expression import NewApplicationCIFExpression
from talon_one.models.new_attribute import NewAttribute
from talon_one.models.new_audience import NewAudience
from talon_one.models.new_base_notification import NewBaseNotification
from talon_one.models.new_campaign import NewCampaign
from talon_one.models.new_campaign_collection import NewCampaignCollection
from talon_one.models.new_campaign_evaluation_group import NewCampaignEvaluationGroup
from talon_one.models.new_campaign_group import NewCampaignGroup
from talon_one.models.new_campaign_set import NewCampaignSet
from talon_one.models.new_campaign_store_budget import NewCampaignStoreBudget
from talon_one.models.new_campaign_store_budget_store_limit import NewCampaignStoreBudgetStoreLimit
from talon_one.models.new_campaign_template import NewCampaignTemplate
from talon_one.models.new_catalog import NewCatalog
from talon_one.models.new_collection import NewCollection
from talon_one.models.new_coupon_creation_job import NewCouponCreationJob
from talon_one.models.new_coupon_deletion_job import NewCouponDeletionJob
from talon_one.models.new_coupons import NewCoupons
from talon_one.models.new_coupons_for_multiple_recipients import NewCouponsForMultipleRecipients
from talon_one.models.new_custom_effect import NewCustomEffect
from talon_one.models.new_customer_profile import NewCustomerProfile
from talon_one.models.new_customer_session import NewCustomerSession
from talon_one.models.new_customer_session_v2 import NewCustomerSessionV2
from talon_one.models.new_event import NewEvent
from talon_one.models.new_event_type import NewEventType
from talon_one.models.new_external_invitation import NewExternalInvitation
from talon_one.models.new_giveaways_pool import NewGiveawaysPool
from talon_one.models.new_internal_audience import NewInternalAudience
from talon_one.models.new_invitation import NewInvitation
from talon_one.models.new_invite_email import NewInviteEmail
from talon_one.models.new_loyalty_program import NewLoyaltyProgram
from talon_one.models.new_loyalty_tier import NewLoyaltyTier
from talon_one.models.new_management_key import NewManagementKey
from talon_one.models.new_multiple_audiences_item import NewMultipleAudiencesItem
from talon_one.models.new_notification_test import NewNotificationTest
from talon_one.models.new_notification_webhook import NewNotificationWebhook
from talon_one.models.new_outgoing_integration_webhook import NewOutgoingIntegrationWebhook
from talon_one.models.new_password import NewPassword
from talon_one.models.new_password_email import NewPasswordEmail
from talon_one.models.new_picklist import NewPicklist
from talon_one.models.new_referral import NewReferral
from talon_one.models.new_referrals_for_multiple_advocates import NewReferralsForMultipleAdvocates
from talon_one.models.new_return import NewReturn
from talon_one.models.new_revision_version import NewRevisionVersion
from talon_one.models.new_role import NewRole
from talon_one.models.new_role_v2 import NewRoleV2
from talon_one.models.new_ruleset import NewRuleset
from talon_one.models.new_saml_connection import NewSamlConnection
from talon_one.models.new_store import NewStore
from talon_one.models.new_template_def import NewTemplateDef
from talon_one.models.new_user import NewUser
from talon_one.models.new_webhook import NewWebhook
from talon_one.models.notification import Notification
from talon_one.models.notification_activation import NotificationActivation
from talon_one.models.notification_list_item import NotificationListItem
from talon_one.models.notification_test import NotificationTest
from talon_one.models.okta_event import OktaEvent
from talon_one.models.okta_event_payload import OktaEventPayload
from talon_one.models.okta_event_payload_data import OktaEventPayloadData
from talon_one.models.okta_event_target import OktaEventTarget
from talon_one.models.one_time_code import OneTimeCode
from talon_one.models.outgoing_integration_braze_policy import OutgoingIntegrationBrazePolicy
from talon_one.models.outgoing_integration_clever_tap_policy import OutgoingIntegrationCleverTapPolicy
from talon_one.models.outgoing_integration_configuration import OutgoingIntegrationConfiguration
from talon_one.models.outgoing_integration_iterable_policy import OutgoingIntegrationIterablePolicy
from talon_one.models.outgoing_integration_mo_engage_policy import OutgoingIntegrationMoEngagePolicy
from talon_one.models.outgoing_integration_template import OutgoingIntegrationTemplate
from talon_one.models.outgoing_integration_template_with_configuration_details import OutgoingIntegrationTemplateWithConfigurationDetails
from talon_one.models.outgoing_integration_templates import OutgoingIntegrationTemplates
from talon_one.models.outgoing_integration_type import OutgoingIntegrationType
from talon_one.models.outgoing_integration_types import OutgoingIntegrationTypes
from talon_one.models.patch_item_catalog_action import PatchItemCatalogAction
from talon_one.models.patch_many_items_catalog_action import PatchManyItemsCatalogAction
from talon_one.models.pending_points_notification_policy import PendingPointsNotificationPolicy
from talon_one.models.picklist import Picklist
from talon_one.models.product import Product
from talon_one.models.product_search_match import ProductSearchMatch
from talon_one.models.product_sku_unit_analytics import ProductSkuUnitAnalytics
from talon_one.models.product_unit_analytics import ProductUnitAnalytics
from talon_one.models.profile_audiences_changes import ProfileAudiencesChanges
from talon_one.models.projected_tier import ProjectedTier
from talon_one.models.redeem_referral_effect_props import RedeemReferralEffectProps
from talon_one.models.referral import Referral
from talon_one.models.referral_constraints import ReferralConstraints
from talon_one.models.referral_created_effect_props import ReferralCreatedEffectProps
from talon_one.models.referral_rejection_reason import ReferralRejectionReason
from talon_one.models.reject_coupon_effect_props import RejectCouponEffectProps
from talon_one.models.reject_referral_effect_props import RejectReferralEffectProps
from talon_one.models.remove_from_audience_effect_props import RemoveFromAudienceEffectProps
from talon_one.models.remove_item_catalog_action import RemoveItemCatalogAction
from talon_one.models.remove_many_items_catalog_action import RemoveManyItemsCatalogAction
from talon_one.models.reopen_session_response import ReopenSessionResponse
from talon_one.models.reserve_coupon_effect_props import ReserveCouponEffectProps
from talon_one.models.return_integration_request import ReturnIntegrationRequest
from talon_one.models.returned_cart_item import ReturnedCartItem
from talon_one.models.revision import Revision
from talon_one.models.revision_activation import RevisionActivation
from talon_one.models.revision_version import RevisionVersion
from talon_one.models.role import Role
from talon_one.models.role_assign import RoleAssign
from talon_one.models.role_membership import RoleMembership
from talon_one.models.role_v2 import RoleV2
from talon_one.models.role_v2_application_details import RoleV2ApplicationDetails
from talon_one.models.role_v2_base import RoleV2Base
from talon_one.models.role_v2_permission_set import RoleV2PermissionSet
from talon_one.models.role_v2_permissions import RoleV2Permissions
from talon_one.models.role_v2_roles_group import RoleV2RolesGroup
from talon_one.models.rollback_added_loyalty_points_effect_props import RollbackAddedLoyaltyPointsEffectProps
from talon_one.models.rollback_coupon_effect_props import RollbackCouponEffectProps
from talon_one.models.rollback_deducted_loyalty_points_effect_props import RollbackDeductedLoyaltyPointsEffectProps
from talon_one.models.rollback_discount_effect_props import RollbackDiscountEffectProps
from talon_one.models.rollback_increased_achievement_progress_effect_props import RollbackIncreasedAchievementProgressEffectProps
from talon_one.models.rollback_referral_effect_props import RollbackReferralEffectProps
from talon_one.models.rule import Rule
from talon_one.models.rule_failure_reason import RuleFailureReason
from talon_one.models.ruleset import Ruleset
from talon_one.models.sso_config import SSOConfig
from talon_one.models.saml_connection import SamlConnection
from talon_one.models.saml_connection_internal import SamlConnectionInternal
from talon_one.models.saml_connection_metadata import SamlConnectionMetadata
from talon_one.models.saml_login_endpoint import SamlLoginEndpoint
from talon_one.models.scim_base_user import ScimBaseUser
from talon_one.models.scim_base_user_name import ScimBaseUserName
from talon_one.models.scim_new_user import ScimNewUser
from talon_one.models.scim_patch_operation import ScimPatchOperation
from talon_one.models.scim_patch_request import ScimPatchRequest
from talon_one.models.scim_resource import ScimResource
from talon_one.models.scim_resource_types_list_response import ScimResourceTypesListResponse
from talon_one.models.scim_schema_resource import ScimSchemaResource
from talon_one.models.scim_schemas_list_response import ScimSchemasListResponse
from talon_one.models.scim_service_provider_config_response import ScimServiceProviderConfigResponse
from talon_one.models.scim_service_provider_config_response_bulk import ScimServiceProviderConfigResponseBulk
from talon_one.models.scim_service_provider_config_response_change_password import ScimServiceProviderConfigResponseChangePassword
from talon_one.models.scim_service_provider_config_response_filter import ScimServiceProviderConfigResponseFilter
from talon_one.models.scim_service_provider_config_response_patch import ScimServiceProviderConfigResponsePatch
from talon_one.models.scim_service_provider_config_response_sort import ScimServiceProviderConfigResponseSort
from talon_one.models.scim_user import ScimUser
from talon_one.models.scim_users_list_response import ScimUsersListResponse
from talon_one.models.session import Session
from talon_one.models.set_discount_effect_props import SetDiscountEffectProps
from talon_one.models.set_discount_per_additional_cost_effect_props import SetDiscountPerAdditionalCostEffectProps
from talon_one.models.set_discount_per_additional_cost_per_item_effect_props import SetDiscountPerAdditionalCostPerItemEffectProps
from talon_one.models.set_discount_per_item_effect_props import SetDiscountPerItemEffectProps
from talon_one.models.show_bundle_metadata_effect_props import ShowBundleMetadataEffectProps
from talon_one.models.show_notification_effect_props import ShowNotificationEffectProps
from talon_one.models.slot_def import SlotDef
from talon_one.models.store import Store
from talon_one.models.strikethrough_changed_item import StrikethroughChangedItem
from talon_one.models.strikethrough_custom_effect_per_item_props import StrikethroughCustomEffectPerItemProps
from talon_one.models.strikethrough_debug_response import StrikethroughDebugResponse
from talon_one.models.strikethrough_effect import StrikethroughEffect
from talon_one.models.strikethrough_labeling_notification import StrikethroughLabelingNotification
from talon_one.models.strikethrough_set_discount_per_item_effect_props import StrikethroughSetDiscountPerItemEffectProps
from talon_one.models.strikethrough_trigger import StrikethroughTrigger
from talon_one.models.summary_campaign_store_budget import SummaryCampaignStoreBudget
from talon_one.models.talang_attribute import TalangAttribute
from talon_one.models.talang_attribute_visibility import TalangAttributeVisibility
from talon_one.models.template_arg_def import TemplateArgDef
from talon_one.models.template_def import TemplateDef
from talon_one.models.template_limit_config import TemplateLimitConfig
from talon_one.models.tier import Tier
from talon_one.models.tier_downgrade_notification_policy import TierDowngradeNotificationPolicy
from talon_one.models.tier_upgrade_notification_policy import TierUpgradeNotificationPolicy
from talon_one.models.tier_will_downgrade_notification_policy import TierWillDowngradeNotificationPolicy
from talon_one.models.tier_will_downgrade_notification_trigger import TierWillDowngradeNotificationTrigger
from talon_one.models.time_point import TimePoint
from talon_one.models.track_event_v2_response import TrackEventV2Response
from talon_one.models.transfer_loyalty_card import TransferLoyaltyCard
from talon_one.models.trigger_webhook_effect_props import TriggerWebhookEffectProps
from talon_one.models.two_fa_config import TwoFAConfig
from talon_one.models.update_account import UpdateAccount
from talon_one.models.update_achievement import UpdateAchievement
from talon_one.models.update_application import UpdateApplication
from talon_one.models.update_application_api_key import UpdateApplicationAPIKey
from talon_one.models.update_application_cif import UpdateApplicationCIF
from talon_one.models.update_attribute_effect_props import UpdateAttributeEffectProps
from talon_one.models.update_audience import UpdateAudience
from talon_one.models.update_campaign import UpdateCampaign
from talon_one.models.update_campaign_collection import UpdateCampaignCollection
from talon_one.models.update_campaign_evaluation_group import UpdateCampaignEvaluationGroup
from talon_one.models.update_campaign_group import UpdateCampaignGroup
from talon_one.models.update_campaign_template import UpdateCampaignTemplate
from talon_one.models.update_catalog import UpdateCatalog
from talon_one.models.update_collection import UpdateCollection
from talon_one.models.update_coupon import UpdateCoupon
from talon_one.models.update_coupon_batch import UpdateCouponBatch
from talon_one.models.update_loyalty_card import UpdateLoyaltyCard
from talon_one.models.update_loyalty_program import UpdateLoyaltyProgram
from talon_one.models.update_loyalty_program_tier import UpdateLoyaltyProgramTier
from talon_one.models.update_picklist import UpdatePicklist
from talon_one.models.update_referral import UpdateReferral
from talon_one.models.update_referral_batch import UpdateReferralBatch
from talon_one.models.update_role import UpdateRole
from talon_one.models.update_store import UpdateStore
from talon_one.models.update_user import UpdateUser
from talon_one.models.user import User
from talon_one.models.user_entity import UserEntity
from talon_one.models.value_map import ValueMap
from talon_one.models.webhook import Webhook
from talon_one.models.webhook_activation_log_entry import WebhookActivationLogEntry
from talon_one.models.webhook_log_entry import WebhookLogEntry
from talon_one.models.webhook_with_outgoing_integration_details import WebhookWithOutgoingIntegrationDetails
from talon_one.models.will_award_giveaway_effect_props import WillAwardGiveawayEffectProps

