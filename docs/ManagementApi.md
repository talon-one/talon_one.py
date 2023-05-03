# talon_one.ManagementApi

All URIs are relative to *https://yourbaseurl.talon.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_loyalty_card_points**](ManagementApi.md#add_loyalty_card_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/add_points | Add points to card
[**add_loyalty_points**](ManagementApi.md#add_loyalty_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/add_points | Add points to customer profile
[**copy_campaign_to_applications**](ManagementApi.md#copy_campaign_to_applications) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/copy | Copy the campaign into the specified Application
[**create_account_collection**](ManagementApi.md#create_account_collection) | **POST** /v1/collections | Create account-level collection
[**create_additional_cost**](ManagementApi.md#create_additional_cost) | **POST** /v1/additional_costs | Create additional cost
[**create_attribute**](ManagementApi.md#create_attribute) | **POST** /v1/attributes | Create custom attribute
[**create_campaign_from_template**](ManagementApi.md#create_campaign_from_template) | **POST** /v1/applications/{applicationId}/create_campaign_from_template | Create campaign from campaign template
[**create_collection**](ManagementApi.md#create_collection) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/collections | Create collection
[**create_coupons**](ManagementApi.md#create_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Create coupons
[**create_coupons_async**](ManagementApi.md#create_coupons_async) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_async | Create coupons asynchronously
[**create_coupons_for_multiple_recipients**](ManagementApi.md#create_coupons_for_multiple_recipients) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_with_recipients | Create coupons for multiple recipients
[**create_notification_webhook**](ManagementApi.md#create_notification_webhook) | **POST** /v1/applications/{applicationId}/notification_webhooks | Create notification about campaign-related changes
[**create_password_recovery_email**](ManagementApi.md#create_password_recovery_email) | **POST** /v1/password_recovery_emails | Request a password reset
[**create_session**](ManagementApi.md#create_session) | **POST** /v1/sessions | Create session
[**deduct_loyalty_card_points**](ManagementApi.md#deduct_loyalty_card_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/deduct_points | Deduct points from card
[**delete_account_collection**](ManagementApi.md#delete_account_collection) | **DELETE** /v1/collections/{collectionId} | Delete account-level collection
[**delete_campaign**](ManagementApi.md#delete_campaign) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId} | Delete campaign
[**delete_collection**](ManagementApi.md#delete_collection) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Delete collection
[**delete_coupon**](ManagementApi.md#delete_coupon) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Delete coupon
[**delete_coupons**](ManagementApi.md#delete_coupons) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Delete coupons
[**delete_loyalty_card**](ManagementApi.md#delete_loyalty_card) | **DELETE** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId} | Delete loyalty card
[**delete_notification_webhook**](ManagementApi.md#delete_notification_webhook) | **DELETE** /v1/applications/{applicationId}/notification_webhooks/{notificationWebhookId} | Delete notification about campaign-related changes
[**delete_referral**](ManagementApi.md#delete_referral) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Delete referral
[**destroy_session**](ManagementApi.md#destroy_session) | **DELETE** /v1/sessions | Destroy session
[**export_account_collection_items**](ManagementApi.md#export_account_collection_items) | **GET** /v1/collections/{collectionId}/export | Export account-level collection&#39;s items
[**export_collection_items**](ManagementApi.md#export_collection_items) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId}/export | Export a collection&#39;s items
[**export_coupons**](ManagementApi.md#export_coupons) | **GET** /v1/applications/{applicationId}/export_coupons | Export coupons
[**export_customer_sessions**](ManagementApi.md#export_customer_sessions) | **GET** /v1/applications/{applicationId}/export_customer_sessions | Export customer sessions
[**export_effects**](ManagementApi.md#export_effects) | **GET** /v1/applications/{applicationId}/export_effects | Export triggered effects
[**export_loyalty_balance**](ManagementApi.md#export_loyalty_balance) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_customer_balance | Export customer loyalty balance to CSV
[**export_loyalty_balances**](ManagementApi.md#export_loyalty_balances) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_customer_balances | Export customer loyalty balances
[**export_loyalty_card_balances**](ManagementApi.md#export_loyalty_card_balances) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_card_balances | Export all card transaction logs
[**export_loyalty_card_ledger**](ManagementApi.md#export_loyalty_card_ledger) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/export_log | Export card&#39;s ledger log
[**export_loyalty_ledger**](ManagementApi.md#export_loyalty_ledger) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/export_log | Export customer&#39;s transaction logs
[**export_referrals**](ManagementApi.md#export_referrals) | **GET** /v1/applications/{applicationId}/export_referrals | Export referrals
[**get_access_logs_without_total_count**](ManagementApi.md#get_access_logs_without_total_count) | **GET** /v1/applications/{applicationId}/access_logs/no_total | Get access logs for Application
[**get_account**](ManagementApi.md#get_account) | **GET** /v1/accounts/{accountId} | Get account details
[**get_account_analytics**](ManagementApi.md#get_account_analytics) | **GET** /v1/accounts/{accountId}/analytics | Get account analytics
[**get_account_collection**](ManagementApi.md#get_account_collection) | **GET** /v1/collections/{collectionId} | Get account-level collection
[**get_additional_cost**](ManagementApi.md#get_additional_cost) | **GET** /v1/additional_costs/{additionalCostId} | Get additional cost
[**get_additional_costs**](ManagementApi.md#get_additional_costs) | **GET** /v1/additional_costs | List additional costs
[**get_all_access_logs**](ManagementApi.md#get_all_access_logs) | **GET** /v1/access_logs | List access logs
[**get_all_roles**](ManagementApi.md#get_all_roles) | **GET** /v1/roles | List roles
[**get_application**](ManagementApi.md#get_application) | **GET** /v1/applications/{applicationId} | Get Application
[**get_application_api_health**](ManagementApi.md#get_application_api_health) | **GET** /v1/applications/{applicationId}/health_report | Get Application health
[**get_application_customer**](ManagementApi.md#get_application_customer) | **GET** /v1/applications/{applicationId}/customers/{customerId} | Get application&#39;s customer
[**get_application_customer_friends**](ManagementApi.md#get_application_customer_friends) | **GET** /v1/applications/{applicationId}/profile/{integrationId}/friends | List friends referred by customer profile
[**get_application_customers**](ManagementApi.md#get_application_customers) | **GET** /v1/applications/{applicationId}/customers | List application&#39;s customers
[**get_application_customers_by_attributes**](ManagementApi.md#get_application_customers_by_attributes) | **POST** /v1/applications/{applicationId}/customer_search | List application customers matching the given attributes
[**get_application_event_types**](ManagementApi.md#get_application_event_types) | **GET** /v1/applications/{applicationId}/event_types | List Applications event types
[**get_application_events_without_total_count**](ManagementApi.md#get_application_events_without_total_count) | **GET** /v1/applications/{applicationId}/events/no_total | List Applications events
[**get_application_session**](ManagementApi.md#get_application_session) | **GET** /v1/applications/{applicationId}/sessions/{sessionId} | Get Application session
[**get_application_sessions**](ManagementApi.md#get_application_sessions) | **GET** /v1/applications/{applicationId}/sessions | List Application sessions
[**get_applications**](ManagementApi.md#get_applications) | **GET** /v1/applications | List Applications
[**get_attribute**](ManagementApi.md#get_attribute) | **GET** /v1/attributes/{attributeId} | Get custom attribute
[**get_attributes**](ManagementApi.md#get_attributes) | **GET** /v1/attributes | List custom attributes
[**get_audiences**](ManagementApi.md#get_audiences) | **GET** /v1/audiences | List audiences
[**get_campaign**](ManagementApi.md#get_campaign) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId} | Get campaign
[**get_campaign_analytics**](ManagementApi.md#get_campaign_analytics) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/analytics | Get analytics of campaigns
[**get_campaign_by_attributes**](ManagementApi.md#get_campaign_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns_search | List campaigns that match the given attributes
[**get_campaign_templates**](ManagementApi.md#get_campaign_templates) | **GET** /v1/campaign_templates | List campaign templates
[**get_campaigns**](ManagementApi.md#get_campaigns) | **GET** /v1/applications/{applicationId}/campaigns | List campaigns
[**get_changes**](ManagementApi.md#get_changes) | **GET** /v1/changes | Get audit logs for an account
[**get_collection**](ManagementApi.md#get_collection) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Get collection
[**get_collection_items**](ManagementApi.md#get_collection_items) | **GET** /v1/collections/{collectionId}/items | Get collection items
[**get_coupons_without_total_count**](ManagementApi.md#get_coupons_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/no_total | List coupons
[**get_customer_activity_report**](ManagementApi.md#get_customer_activity_report) | **GET** /v1/applications/{applicationId}/customer_activity_reports/{customerId} | Get customer&#39;s activity report
[**get_customer_activity_reports_without_total_count**](ManagementApi.md#get_customer_activity_reports_without_total_count) | **GET** /v1/applications/{applicationId}/customer_activity_reports/no_total | Get Activity Reports for Application Customers
[**get_customer_analytics**](ManagementApi.md#get_customer_analytics) | **GET** /v1/applications/{applicationId}/customers/{customerId}/analytics | Get customer&#39;s analytics report
[**get_customer_profile**](ManagementApi.md#get_customer_profile) | **GET** /v1/customers/{customerId} | Get customer profile
[**get_customer_profiles**](ManagementApi.md#get_customer_profiles) | **GET** /v1/customers/no_total | List customer profiles
[**get_customers_by_attributes**](ManagementApi.md#get_customers_by_attributes) | **POST** /v1/customer_search/no_total | List customer profiles matching the given attributes
[**get_event_types**](ManagementApi.md#get_event_types) | **GET** /v1/event_types | List event types
[**get_exports**](ManagementApi.md#get_exports) | **GET** /v1/exports | Get exports
[**get_loyalty_card**](ManagementApi.md#get_loyalty_card) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId} | Get loyalty card
[**get_loyalty_card_transaction_logs**](ManagementApi.md#get_loyalty_card_transaction_logs) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/logs | List card&#39;s transactions
[**get_loyalty_cards**](ManagementApi.md#get_loyalty_cards) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards | List loyalty cards
[**get_loyalty_points**](ManagementApi.md#get_loyalty_points) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId} | Get customer&#39;s full loyalty ledger
[**get_loyalty_program**](ManagementApi.md#get_loyalty_program) | **GET** /v1/loyalty_programs/{loyaltyProgramId} | Get loyalty program
[**get_loyalty_program_transactions**](ManagementApi.md#get_loyalty_program_transactions) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/transactions | List loyalty program transactions
[**get_loyalty_programs**](ManagementApi.md#get_loyalty_programs) | **GET** /v1/loyalty_programs | List loyalty programs
[**get_loyalty_statistics**](ManagementApi.md#get_loyalty_statistics) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/statistics | Get loyalty program statistics
[**get_notification_webhook**](ManagementApi.md#get_notification_webhook) | **GET** /v1/applications/{applicationId}/notification_webhooks/{notificationWebhookId} | Get notification about campaign-related changes
[**get_notification_webhooks**](ManagementApi.md#get_notification_webhooks) | **GET** /v1/applications/{applicationId}/notification_webhooks | List notifications about campaign-related changes
[**get_referrals_without_total_count**](ManagementApi.md#get_referrals_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/no_total | List referrals
[**get_role**](ManagementApi.md#get_role) | **GET** /v1/roles/{roleId} | Get role
[**get_ruleset**](ManagementApi.md#get_ruleset) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Get ruleset
[**get_rulesets**](ManagementApi.md#get_rulesets) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets | List campaign rulesets
[**get_user**](ManagementApi.md#get_user) | **GET** /v1/users/{userId} | Get user
[**get_users**](ManagementApi.md#get_users) | **GET** /v1/users | List users in account
[**get_webhook**](ManagementApi.md#get_webhook) | **GET** /v1/webhooks/{webhookId} | Get webhook
[**get_webhook_activation_logs**](ManagementApi.md#get_webhook_activation_logs) | **GET** /v1/webhook_activation_logs | List webhook activation log entries
[**get_webhook_logs**](ManagementApi.md#get_webhook_logs) | **GET** /v1/webhook_logs | List webhook log entries
[**get_webhooks**](ManagementApi.md#get_webhooks) | **GET** /v1/webhooks | List webhooks
[**import_account_collection**](ManagementApi.md#import_account_collection) | **POST** /v1/collections/{collectionId}/import | Import data in existing account-level collection
[**import_allowed_list**](ManagementApi.md#import_allowed_list) | **POST** /v1/attributes/{attributeId}/allowed_list/import | Import allowed values for attribute
[**import_collection**](ManagementApi.md#import_collection) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId}/import | Import data in existing collection
[**import_coupons**](ManagementApi.md#import_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_coupons | Import coupons
[**import_loyalty_cards**](ManagementApi.md#import_loyalty_cards) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/import_cards | Import loyalty cards
[**import_loyalty_points**](ManagementApi.md#import_loyalty_points) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/import_points | Import loyalty points
[**import_pool_giveaways**](ManagementApi.md#import_pool_giveaways) | **POST** /v1/giveaways/pools/{poolId}/import | Import giveaway codes into a giveaway pool
[**import_referrals**](ManagementApi.md#import_referrals) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_referrals | Import referrals
[**list_account_collections**](ManagementApi.md#list_account_collections) | **GET** /v1/collections | List collections in account
[**list_collections**](ManagementApi.md#list_collections) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections | List collections
[**list_collections_in_application**](ManagementApi.md#list_collections_in_application) | **GET** /v1/applications/{applicationId}/collections | List collections in application
[**post_added_deducted_points_notification**](ManagementApi.md#post_added_deducted_points_notification) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/notifications/added_deducted_points | Create notification about added or deducted loyalty points
[**post_catalogs_strikethrough_notification**](ManagementApi.md#post_catalogs_strikethrough_notification) | **POST** /v1/catalogs/{applicationId}/notifications/strikethrough | Create strikethrough notification
[**remove_loyalty_points**](ManagementApi.md#remove_loyalty_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/deduct_points | Deduct points from customer profile
[**reset_password**](ManagementApi.md#reset_password) | **POST** /v1/reset_password | Reset password
[**search_coupons_advanced_application_wide_without_total_count**](ManagementApi.md#search_coupons_advanced_application_wide_without_total_count) | **POST** /v1/applications/{applicationId}/coupons_search_advanced/no_total | List coupons that match the given attributes (without total count)
[**search_coupons_advanced_without_total_count**](ManagementApi.md#search_coupons_advanced_without_total_count) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced/no_total | List coupons that match the given attributes in campaign (without total count)
[**transfer_loyalty_card**](ManagementApi.md#transfer_loyalty_card) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/transfer | Transfer card data
[**update_account_collection**](ManagementApi.md#update_account_collection) | **PUT** /v1/collections/{collectionId} | Update account-level collection
[**update_additional_cost**](ManagementApi.md#update_additional_cost) | **PUT** /v1/additional_costs/{additionalCostId} | Update additional cost
[**update_attribute**](ManagementApi.md#update_attribute) | **PUT** /v1/attributes/{attributeId} | Update custom attribute
[**update_campaign**](ManagementApi.md#update_campaign) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId} | Update campaign
[**update_collection**](ManagementApi.md#update_collection) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Update collection description
[**update_coupon**](ManagementApi.md#update_coupon) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Update coupon
[**update_coupon_batch**](ManagementApi.md#update_coupon_batch) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Update coupons
[**update_loyalty_card**](ManagementApi.md#update_loyalty_card) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId} | Update loyalty card status
[**update_notification_webhook**](ManagementApi.md#update_notification_webhook) | **PUT** /v1/applications/{applicationId}/notification_webhooks/{notificationWebhookId} | Update notification about campaign-related changes
[**update_referral**](ManagementApi.md#update_referral) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Update referral


# **add_loyalty_card_points**
> add_loyalty_card_points(loyalty_program_id, loyalty_card_id, body)

Add points to card

Add points to the given loyalty card in the specified card-based loyalty program. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.AddLoyaltyPoints() # AddLoyaltyPoints | body

    try:
        # Add points to card
        api_instance.add_loyalty_card_points(loyalty_program_id, loyalty_card_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->add_loyalty_card_points: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.AddLoyaltyPoints() # AddLoyaltyPoints | body

    try:
        # Add points to card
        api_instance.add_loyalty_card_points(loyalty_program_id, loyalty_card_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->add_loyalty_card_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 
 **body** | [**AddLoyaltyPoints**](AddLoyaltyPoints.md)| body | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_loyalty_points**
> add_loyalty_points(loyalty_program_id, integration_id, body)

Add points to customer profile

Add points in the specified loyalty program for the given customer.  To get the `integrationId` of the profile from a `sessionId`, use the [Update customer session](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
body = talon_one.AddLoyaltyPoints() # AddLoyaltyPoints | body

    try:
        # Add points to customer profile
        api_instance.add_loyalty_points(loyalty_program_id, integration_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->add_loyalty_points: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
body = talon_one.AddLoyaltyPoints() # AddLoyaltyPoints | body

    try:
        # Add points to customer profile
        api_instance.add_loyalty_points(loyalty_program_id, integration_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->add_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 
 **body** | [**AddLoyaltyPoints**](AddLoyaltyPoints.md)| body | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_campaign_to_applications**
> InlineResponse2004 copy_campaign_to_applications(application_id, campaign_id, body)

Copy the campaign into the specified Application

Copy the campaign into all specified Applications.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.CampaignCopy() # CampaignCopy | body

    try:
        # Copy the campaign into the specified Application
        api_response = api_instance.copy_campaign_to_applications(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->copy_campaign_to_applications: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.CampaignCopy() # CampaignCopy | body

    try:
        # Copy the campaign into the specified Application
        api_response = api_instance.copy_campaign_to_applications(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->copy_campaign_to_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**CampaignCopy**](CampaignCopy.md)| body | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_collection**
> Collection create_account_collection(body)

Create account-level collection

Create account-level collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewCollection() # NewCollection | body

    try:
        # Create account-level collection
        api_response = api_instance.create_account_collection(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_account_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewCollection() # NewCollection | body

    try:
        # Create account-level collection
        api_response = api_instance.create_account_collection(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_account_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewCollection**](NewCollection.md)| body | 

### Return type

[**Collection**](Collection.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**409** | Conflict. A Collection with this name already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_additional_cost**
> AccountAdditionalCost create_additional_cost(body)

Create additional cost

Create an [additional cost](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).  These additional costs are shared across all applications in your account, and are never required. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewAdditionalCost() # NewAdditionalCost | body

    try:
        # Create additional cost
        api_response = api_instance.create_additional_cost(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_additional_cost: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewAdditionalCost() # NewAdditionalCost | body

    try:
        # Create additional cost
        api_response = api_instance.create_additional_cost(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_additional_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewAdditionalCost**](NewAdditionalCost.md)| body | 

### Return type

[**AccountAdditionalCost**](AccountAdditionalCost.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute**
> Attribute create_attribute(body)

Create custom attribute

Create a _custom attribute_ in this account. [Custom attributes](https://docs.talon.one/docs/dev/concepts/attributes) allow you to add data to Talon.One domain entities like campaigns, coupons, customers and so on.  These attributes can then be given values when creating/updating these entities, and these values can be used in your campaign rules.  For example, you could define a `zipCode` field for customer sessions, and add a rule to your campaign that only allows certain ZIP codes.  These attributes are shared across all Applications in your account and are never required. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewAttribute() # NewAttribute | body

    try:
        # Create custom attribute
        api_response = api_instance.create_attribute(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_attribute: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewAttribute() # NewAttribute | body

    try:
        # Create custom attribute
        api_response = api_instance.create_attribute(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewAttribute**](NewAttribute.md)| body | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_from_template**
> CreateTemplateCampaignResponse create_campaign_from_template(application_id, body)

Create campaign from campaign template

Use the campaign template referenced in the request body to create a new campaign in one of the connected Applications.  If the template was created from a campaign with rules referencing [campaign collections](https://docs.talon.one/docs/product/campaigns/managing-collections), the corresponding collections for the new campaign are created automatically. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.CreateTemplateCampaign() # CreateTemplateCampaign | body

    try:
        # Create campaign from campaign template
        api_response = api_instance.create_campaign_from_template(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_campaign_from_template: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.CreateTemplateCampaign() # CreateTemplateCampaign | body

    try:
        # Create campaign from campaign template
        api_response = api_instance.create_campaign_from_template(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_campaign_from_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | [**CreateTemplateCampaign**](CreateTemplateCampaign.md)| body | 

### Return type

[**CreateTemplateCampaignResponse**](CreateTemplateCampaignResponse.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> Collection create_collection(application_id, campaign_id, body)

Create collection

Create a collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCampaignCollection() # NewCampaignCollection | body

    try:
        # Create collection
        api_response = api_instance.create_collection(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCampaignCollection() # NewCampaignCollection | body

    try:
        # Create collection
        api_response = api_instance.create_collection(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewCampaignCollection**](NewCampaignCollection.md)| body | 

### Return type

[**Collection**](Collection.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons**
> InlineResponse2007 create_coupons(application_id, campaign_id, body, silent=silent)

Create coupons

Create coupons according to some pattern. Up to 20.000 coupons can be created without a unique prefix. When a unique prefix is provided, up to 200.000 coupons can be created.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCoupons() # NewCoupons | body
silent = 'yes' # str | Possible values: `yes` or `no`. - `yes`: Increases the perfomance of the API call by returning a 204 response. - `no`: Returns a 200 response that contains the updated customer profiles.  (optional) (default to 'yes')

    try:
        # Create coupons
        api_response = api_instance.create_coupons(application_id, campaign_id, body, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCoupons() # NewCoupons | body
silent = 'yes' # str | Possible values: `yes` or `no`. - `yes`: Increases the perfomance of the API call by returning a 204 response. - `no`: Returns a 200 response that contains the updated customer profiles.  (optional) (default to 'yes')

    try:
        # Create coupons
        api_response = api_instance.create_coupons(application_id, campaign_id, body, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewCoupons**](NewCoupons.md)| body | 
 **silent** | **str**| Possible values: &#x60;yes&#x60; or &#x60;no&#x60;. - &#x60;yes&#x60;: Increases the perfomance of the API call by returning a 204 response. - &#x60;no&#x60;: Returns a 200 response that contains the updated customer profiles.  | [optional] [default to &#39;yes&#39;]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons_async**
> AsyncCouponCreationResponse create_coupons_async(application_id, campaign_id, body)

Create coupons asynchronously

Create up to 5,000,000 coupons asynchronously. You should typically use this enpdoint when you create at least 20,001 coupons. You receive an email when the creation is complete.  If you want to create less than 20,001 coupons, you can use the [Create coupons](https://docs.talon.one/management-api#tag/Coupons/operation/createCoupons) endpoint. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCouponCreationJob() # NewCouponCreationJob | body

    try:
        # Create coupons asynchronously
        api_response = api_instance.create_coupons_async(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons_async: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCouponCreationJob() # NewCouponCreationJob | body

    try:
        # Create coupons asynchronously
        api_response = api_instance.create_coupons_async(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewCouponCreationJob**](NewCouponCreationJob.md)| body | 

### Return type

[**AsyncCouponCreationResponse**](AsyncCouponCreationResponse.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons_for_multiple_recipients**
> InlineResponse2007 create_coupons_for_multiple_recipients(application_id, campaign_id, body, silent=silent)

Create coupons for multiple recipients

Create coupons according to some pattern for up to 1000 recipients.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCouponsForMultipleRecipients() # NewCouponsForMultipleRecipients | body
silent = 'yes' # str | Possible values: `yes` or `no`. - `yes`: Increases the perfomance of the API call by returning a 204 response. - `no`: Returns a 200 response that contains the updated customer profiles.  (optional) (default to 'yes')

    try:
        # Create coupons for multiple recipients
        api_response = api_instance.create_coupons_for_multiple_recipients(application_id, campaign_id, body, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons_for_multiple_recipients: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.NewCouponsForMultipleRecipients() # NewCouponsForMultipleRecipients | body
silent = 'yes' # str | Possible values: `yes` or `no`. - `yes`: Increases the perfomance of the API call by returning a 204 response. - `no`: Returns a 200 response that contains the updated customer profiles.  (optional) (default to 'yes')

    try:
        # Create coupons for multiple recipients
        api_response = api_instance.create_coupons_for_multiple_recipients(application_id, campaign_id, body, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons_for_multiple_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewCouponsForMultipleRecipients**](NewCouponsForMultipleRecipients.md)| body | 
 **silent** | **str**| Possible values: &#x60;yes&#x60; or &#x60;no&#x60;. - &#x60;yes&#x60;: Increases the perfomance of the API call by returning a 204 response. - &#x60;no&#x60;: Returns a 200 response that contains the updated customer profiles.  | [optional] [default to &#39;yes&#39;]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_notification_webhook**
> NotificationWebhook create_notification_webhook(application_id, body)

Create notification about campaign-related changes

Create a [notification about campaign-related changes](https://docs.talon.one/docs/product/applications/outbound-notifications).  A notification about campaign-related changes is different from regular webhooks in that it is Application-scoped and has a predefined payload. [Regular webhooks](https://docs.talon.one/docs/dev/getting-started/webhooks) have user-definable payloads.  **Tip:**  - You can create these notifications using the Campaign Manager. See [Managing notifications](https://docs.talon.one/docs/product/applications/outbound-notifications). - You can review the payload you will receive in the [specs](https://docs.talon.one/outbound-notifications#/paths/campaign_created/post). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.NewNotificationWebhook() # NewNotificationWebhook | body

    try:
        # Create notification about campaign-related changes
        api_response = api_instance.create_notification_webhook(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_notification_webhook: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.NewNotificationWebhook() # NewNotificationWebhook | body

    try:
        # Create notification about campaign-related changes
        api_response = api_instance.create_notification_webhook(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewNotificationWebhook**](NewNotificationWebhook.md)| body | 

### Return type

[**NotificationWebhook**](NotificationWebhook.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_recovery_email**
> NewPasswordEmail create_password_recovery_email(body)

Request a password reset

Send an email with a password recovery link to the email address of an existing account.  **Note:** The password recovery link expires 30 minutes after this endpoint is triggered. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewPasswordEmail() # NewPasswordEmail | body

    try:
        # Request a password reset
        api_response = api_instance.create_password_recovery_email(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_password_recovery_email: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewPasswordEmail() # NewPasswordEmail | body

    try:
        # Request a password reset
        api_response = api_instance.create_password_recovery_email(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_password_recovery_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewPasswordEmail**](NewPasswordEmail.md)| body | 

### Return type

[**NewPasswordEmail**](NewPasswordEmail.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> Session create_session(body)

Create session

Create a session to use the Management API endpoints. Use the value of the `token` property provided in the response as bearer token in other API calls.  A token is valid for 3 months. In accordance with best pratices, use your generated token for all your API requests. Do **not** regenerate a token for each request.  This endpoint has a rate limit of 3 to 6 requests per second per account, depending on your setup.  <div class=\"redoc-section\">   <p class=\"title\">Granular API key</p>   Instead of using a session, you can also use the <a href=\"https://docs.talon.one/docs/product/account/dev-tools/managing-mapi-keys\">Management API key feature</a>   in the Campaign Manager to decide which endpoints can be used with a given key. </div> 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.LoginParams() # LoginParams | body

    try:
        # Create session
        api_response = api_instance.create_session(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_session: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.LoginParams() # LoginParams | body

    try:
        # Create session
        api_response = api_instance.create_session(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginParams**](LoginParams.md)| body | 

### Return type

[**Session**](Session.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deduct_loyalty_card_points**
> deduct_loyalty_card_points(loyalty_program_id, loyalty_card_id, body)

Deduct points from card

Deduct points from the given loyalty card in the specified card-based loyalty program. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.DeductLoyaltyPoints() # DeductLoyaltyPoints | body

    try:
        # Deduct points from card
        api_instance.deduct_loyalty_card_points(loyalty_program_id, loyalty_card_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->deduct_loyalty_card_points: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.DeductLoyaltyPoints() # DeductLoyaltyPoints | body

    try:
        # Deduct points from card
        api_instance.deduct_loyalty_card_points(loyalty_program_id, loyalty_card_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->deduct_loyalty_card_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 
 **body** | [**DeductLoyaltyPoints**](DeductLoyaltyPoints.md)| body | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_collection**
> delete_account_collection(collection_id)

Delete account-level collection

Delete the given account-level collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Delete account-level collection
        api_instance.delete_account_collection(collection_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_account_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Delete account-level collection
        api_instance.delete_account_collection(collection_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_account_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign**
> delete_campaign(application_id, campaign_id)

Delete campaign

Delete the given campaign.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.

    try:
        # Delete campaign
        api_instance.delete_campaign(application_id, campaign_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_campaign: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.

    try:
        # Delete campaign
        api_instance.delete_campaign(application_id, campaign_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> delete_collection(application_id, campaign_id, collection_id)

Delete collection

Delete the given collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Delete collection
        api_instance.delete_collection(application_id, campaign_id, collection_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Delete collection
        api_instance.delete_collection(application_id, campaign_id, collection_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon**
> delete_coupon(application_id, campaign_id, coupon_id)

Delete coupon

Delete the specified coupon.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
coupon_id = 'coupon_id_example' # str | The internal ID of the coupon code. You can find this value in the `id` property from the [List coupons](https://docs.talon.one/management-api#tag/Coupons/operation/getCouponsWithoutTotalCount) endpoint response. 

    try:
        # Delete coupon
        api_instance.delete_coupon(application_id, campaign_id, coupon_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_coupon: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
coupon_id = 'coupon_id_example' # str | The internal ID of the coupon code. You can find this value in the `id` property from the [List coupons](https://docs.talon.one/management-api#tag/Coupons/operation/getCouponsWithoutTotalCount) endpoint response. 

    try:
        # Delete coupon
        api_instance.delete_coupon(application_id, campaign_id, coupon_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **coupon_id** | **str**| The internal ID of the coupon code. You can find this value in the &#x60;id&#x60; property from the [List coupons](https://docs.talon.one/management-api#tag/Coupons/operation/getCouponsWithoutTotalCount) endpoint response.  | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupons**
> delete_coupons(application_id, campaign_id, value=value, created_before=created_before, created_after=created_after, starts_after=starts_after, starts_before=starts_before, expires_after=expires_after, expires_before=expires_before, valid=valid, batch_id=batch_id, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match)

Delete coupons

Deletes all the coupons matching the specified criteria.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | - `expired`: Matches coupons in which the expiration date is set and in the past. - `validNow`: Matches coupons in which start date is null or in the past and expiration date is null or in the future. - `validFuture`: Matches coupons in which start date is set and in the future.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
usable = 'usable_example' # str | - `true`: only coupons where `usageCounter < usageLimit` will be returned. - `false`: only coupons where `usageCounter >= usageLimit` will be returned.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's `RecipientIntegrationId` field.  (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)

    try:
        # Delete coupons
        api_instance.delete_coupons(application_id, campaign_id, value=value, created_before=created_before, created_after=created_after, starts_after=starts_after, starts_before=starts_before, expires_after=expires_after, expires_before=expires_before, valid=valid, batch_id=batch_id, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_coupons: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | - `expired`: Matches coupons in which the expiration date is set and in the past. - `validNow`: Matches coupons in which start date is null or in the past and expiration date is null or in the future. - `validFuture`: Matches coupons in which start date is set and in the future.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
usable = 'usable_example' # str | - `true`: only coupons where `usageCounter < usageLimit` will be returned. - `false`: only coupons where `usageCounter >= usageLimit` will be returned.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's `RecipientIntegrationId` field.  (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)

    try:
        # Delete coupons
        api_instance.delete_coupons(application_id, campaign_id, value=value, created_before=created_before, created_after=created_after, starts_after=starts_after, starts_before=starts_before, expires_after=expires_after, expires_before=expires_before, valid=valid, batch_id=batch_id, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **starts_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **starts_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **expires_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **expires_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| - &#x60;expired&#x60;: Matches coupons in which the expiration date is set and in the past. - &#x60;validNow&#x60;: Matches coupons in which start date is null or in the past and expiration date is null or in the future. - &#x60;validFuture&#x60;: Matches coupons in which start date is set and in the future.  | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **usable** | **str**| - &#x60;true&#x60;: only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned. - &#x60;false&#x60;: only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60; will be returned.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s &#x60;RecipientIntegrationId&#x60; field.  | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loyalty_card**
> delete_loyalty_card(loyalty_program_id, loyalty_card_id)

Delete loyalty card

Delete the given loyalty card.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 

    try:
        # Delete loyalty card
        api_instance.delete_loyalty_card(loyalty_program_id, loyalty_card_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_loyalty_card: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 

    try:
        # Delete loyalty card
        api_instance.delete_loyalty_card(loyalty_program_id, loyalty_card_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_loyalty_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_webhook**
> delete_notification_webhook(application_id, notification_webhook_id)

Delete notification about campaign-related changes

Remove the given existing [notification about campaign-related changes](https://docs.talon.one/docs/product/applications/outbound-notifications). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
notification_webhook_id = 56 # int | The ID of the webhook. Get it with the appropriate _List notifications_ endpoint.

    try:
        # Delete notification about campaign-related changes
        api_instance.delete_notification_webhook(application_id, notification_webhook_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_notification_webhook: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
notification_webhook_id = 56 # int | The ID of the webhook. Get it with the appropriate _List notifications_ endpoint.

    try:
        # Delete notification about campaign-related changes
        api_instance.delete_notification_webhook(application_id, notification_webhook_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **notification_webhook_id** | **int**| The ID of the webhook. Get it with the appropriate _List notifications_ endpoint. | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_referral**
> delete_referral(application_id, campaign_id, referral_id)

Delete referral

Delete the specified referral.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
referral_id = 'referral_id_example' # str | The ID of the referral code.

    try:
        # Delete referral
        api_instance.delete_referral(application_id, campaign_id, referral_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_referral: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
referral_id = 'referral_id_example' # str | The ID of the referral code.

    try:
        # Delete referral
        api_instance.delete_referral(application_id, campaign_id, referral_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_referral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **referral_id** | **str**| The ID of the referral code. | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_session**
> destroy_session()

Destroy session

Destroys the session.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    
    try:
        # Destroy session
        api_instance.destroy_session()
    except ApiException as e:
        print("Exception when calling ManagementApi->destroy_session: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    
    try:
        # Destroy session
        api_instance.destroy_session()
    except ApiException as e:
        print("Exception when calling ManagementApi->destroy_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_account_collection_items**
> str export_account_collection_items(collection_id)

Export account-level collection's items

Download a CSV file containing items from an account-level collection.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Export account-level collection's items
        api_response = api_instance.export_account_collection_items(collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_account_collection_items: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Export account-level collection's items
        api_response = api_instance.export_account_collection_items(collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_account_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_collection_items**
> str export_collection_items(application_id, campaign_id, collection_id)

Export a collection's items

Download a CSV file containing a collection's items.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Export a collection's items
        api_response = api_instance.export_collection_items(application_id, campaign_id, collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_collection_items: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Export a collection's items
        api_response = api_instance.export_collection_items(application_id, campaign_id, collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_coupons**
> str export_coupons(application_id, campaign_id=campaign_id, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, date_format=date_format, campaign_state=campaign_state)

Export coupons

Download a CSV file containing the coupons that match the given properties.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  The CSV file contains the following columns:  - `accountid`: The ID of your deployment. - `applicationid`: The ID of the Application this coupon is related to. - `attributes`: A json object describing _custom_ referral attribute names and their values. - `batchid`: The ID of the batch this coupon is part of. - `campaignid`: The ID of the campaign this coupon is related to. - `counter`: The number of times this coupon has been redeemed. - `created`: The creation date of the coupon code. - `deleted`: Whether the coupon code is deleted. - `deleted_changelogid`: The ID of the delete event in the logs. - `discount_counter`: The amount of discount given by this coupon. - `discount_limitval`: The maximum discount amount that can be given be this coupon. - `expirydate`: The end date in RFC3339 of the code redemption period. - `id`: The internal ID of the coupon code. - `importid`: The ID of the import job that created this coupon. - `is_reservation_mandatory`: Whether this coupon requires a reservation to be redeemed. - `limits`: The limits set on this coupon. - `limitval`: The maximum number of redemptions of this code. - `recipientintegrationid`: The integration ID of the customer considered as recipient of the coupon.   Only the customer with this integration ID can redeem the corresponding coupon code.   Learn about [coupon reservation](https://docs.talon.one/docs/product/rules/effects/using-effects#reserving-a-coupon-code). - `referralid`: The ID of the referral code that triggered the creation of this coupon (create coupon effect). - `reservation`: Whether the coupon is reserved. - `reservation_counter`: How many times this coupon has been reserved. - `reservation_limitval`: The maximum of number of reservations this coupon can have. - `startdate`: The start date in RFC3339 of the code redemption period. - `value`: The coupon code. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 3.4 # float | Filter results by campaign. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)

    try:
        # Export coupons
        api_response = api_instance.export_coupons(application_id, campaign_id=campaign_id, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, date_format=date_format, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_coupons: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 3.4 # float | Filter results by campaign. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)

    try:
        # Export coupons
        api_response = api_instance.export_coupons(application_id, campaign_id=campaign_id, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, date_format=date_format, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_customer_sessions**
> str export_customer_sessions(application_id, created_before=created_before, created_after=created_after, profile_integration_id=profile_integration_id, date_format=date_format, customer_session_state=customer_session_state)

Export customer sessions

Download a CSV file containing the customer sessions that match the request.  **Important:** Archived sessions cannot be exported. See the [retention policy](https://docs.talon.one/docs/product/server-infrastructure-and-data-retention#data-retention-policy).  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  - `id`: The internal ID of the session. - `firstsession`: Whether this is a first session. - `integrationid`: The integration ID of the session. - `applicationid`: The ID of the Application. - `profileid`: The internal ID of the customer profile. - `profileintegrationid`: The integration ID of the customer profile. - `created`: The timestamp when the session was created. - `state`: The [state](https://docs.talon.one/docs/dev/concepts/entities#customer-session-states) of the session. - `cartitems`: The cart items in the session. - `discounts`: The discounts in the session. - `total`: The total value of the session. - `attributes`: The attributes set in the session. - `closedat`: Timestamp when the session was closed. - `cancelledat`: Timestamp when the session was cancelled. - `referral`: The referral code in the session. - `identifiers`: The identifiers in the session. - `additional_costs`: The [additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs) in the session. - `updated`: Timestamp of the last session update. - `coupons`: Coupon codes in the session. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. (optional)
profile_integration_id = 'profile_integration_id_example' # str | Only return sessions for the customer that matches this customer integration ID. (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)
customer_session_state = 'customer_session_state_example' # str | Filter results by state. (optional)

    try:
        # Export customer sessions
        api_response = api_instance.export_customer_sessions(application_id, created_before=created_before, created_after=created_after, profile_integration_id=profile_integration_id, date_format=date_format, customer_session_state=customer_session_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_customer_sessions: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. (optional)
profile_integration_id = 'profile_integration_id_example' # str | Only return sessions for the customer that matches this customer integration ID. (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)
customer_session_state = 'customer_session_state_example' # str | Filter results by state. (optional)

    try:
        # Export customer sessions
        api_response = api_instance.export_customer_sessions(application_id, created_before=created_before, created_after=created_after, profile_integration_id=profile_integration_id, date_format=date_format, customer_session_state=customer_session_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_customer_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. | [optional] 
 **profile_integration_id** | **str**| Only return sessions for the customer that matches this customer integration ID. | [optional] 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 
 **customer_session_state** | **str**| Filter results by state. | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_effects**
> str export_effects(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, date_format=date_format)

Export triggered effects

Download a CSV file containing the triggered effects that match the given attributes.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  The generated file can contain the following columns:  - `applicationid`: The ID of the Application. - `campaignid`: The ID of the campaign. - `couponid`: The ID of the coupon, when applicable to the effect. - `created`: The timestamp of the effect. - `event_type`: The name of the event. See the [docs](https://docs.talon.one/docs/dev/concepts/events). - `eventid`: The internal ID of the effect. - `name`: The effect name. See the [docs](https://docs.talon.one/docs/dev/integration-api/api-effects). - `profileintegrationid`: The ID of the customer profile, when applicable. - `props`: The [properties](https://docs.talon.one/docs/dev/integration-api/api-effects) of the effect. - `ruleindex`: The index of the rule. - `rulesetid`: The ID of the rule set. - `sessionid`: The internal ID of the session that triggered the effect. - `profileid`: The internal ID of the customer profile. - `sessionintegrationid`: The integration ID of the session. - `total_revenue`: The total revenue. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export triggered effects
        api_response = api_instance.export_effects(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_effects: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export triggered effects
        api_response = api_instance.export_effects(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_effects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_balance**
> str export_loyalty_balance(loyalty_program_id, end_date=end_date)

Export customer loyalty balance to CSV

⚠️ Deprecation notice: Support for requests to this endpoint will end soon. To export customer loyalty balances to CSV, use the [Export customer loyalty balances to CSV](/management-api#tag/Loyalty/operation/exportLoyaltyBalances) endpoint.  Download a CSV file containing the balance of each customer in the loyalty program.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  (optional)

    try:
        # Export customer loyalty balance to CSV
        api_response = api_instance.export_loyalty_balance(loyalty_program_id, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_balance: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  (optional)

    try:
        # Export customer loyalty balance to CSV
        api_response = api_instance.export_loyalty_balance(loyalty_program_id, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **end_date** | **datetime**| Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_balances**
> str export_loyalty_balances(loyalty_program_id, end_date=end_date)

Export customer loyalty balances

Download a CSV file containing the balance of each customer in the loyalty program.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  The generated file can contain the following columns:  - `loyaltyProgramID`: The ID of the loyalty program. - `loyaltySubledger`: The name of the subdleger, when applicatble. - `profileIntegrationID`: The integration ID of the customer profile. - `currentBalance`: The current point balance. - `pendingBalance`: The number of pending points. - `expiredBalance`: The number of expired points. - `spentBalance`: The number of spent points. - `currentTier`: The tier that the customer is in at the time of the export. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  (optional)

    try:
        # Export customer loyalty balances
        api_response = api_instance.export_loyalty_balances(loyalty_program_id, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_balances: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  (optional)

    try:
        # Export customer loyalty balances
        api_response = api_instance.export_loyalty_balances(loyalty_program_id, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **end_date** | **datetime**| Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_card_balances**
> str export_loyalty_card_balances(loyalty_program_id, end_date=end_date)

Export all card transaction logs

Download a CSV file containing the balances of all cards in the loyalty program.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  The CSV file contains the following columns: - `loyaltyProgramID`: The ID of the loyalty program. - `loyaltySubledger`: The name of the subdleger, when applicatble. - `cardIdentifier`: The alphanumeric identifier of the loyalty card. - `cardState`:The state of the loyalty card. It can be `active` or `inactive`. - `currentBalance`: The current point balance. - `pendingBalance`: The number of pending points. - `expiredBalance`: The number of expired points. - `spentBalance`: The number of spent points. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  (optional)

    try:
        # Export all card transaction logs
        api_response = api_instance.export_loyalty_card_balances(loyalty_program_id, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_card_balances: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
end_date = '2013-10-20T19:20:30+01:00' # datetime | Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  (optional)

    try:
        # Export all card transaction logs
        api_response = api_instance.export_loyalty_card_balances(loyalty_program_id, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_card_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **end_date** | **datetime**| Used to return balances only for entries older than this timestamp. The expired, active, and pending points are relative to this timestamp.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_card_ledger**
> str export_loyalty_card_ledger(loyalty_program_id, loyalty_card_id, range_start, range_end, date_format=date_format)

Export card's ledger log

Download a CSV file containing a loyalty card ledger log of the loyalty program.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export card's ledger log
        api_response = api_instance.export_loyalty_card_ledger(loyalty_program_id, loyalty_card_id, range_start, range_end, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_card_ledger: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export card's ledger log
        api_response = api_instance.export_loyalty_card_ledger(loyalty_program_id, loyalty_card_id, range_start, range_end, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_card_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_ledger**
> str export_loyalty_ledger(range_start, range_end, loyalty_program_id, integration_id, date_format=date_format)

Export customer's transaction logs

Download a CSV file containing a customer's transaction logs in the loyalty program.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  The generated file can contain the following columns:  - `customerprofileid`: The ID of the profile. - `customersessionid`: The ID of the customer session. - `rulesetid`: The ID of the rule set. - `rulename`: The name of the rule. - `programid`: The ID of the loyalty program. - `type`: The type of the loyalty program. - `name`: The name of the loyalty program. - `subledgerid`: The ID of the subledger, when applicable. - `startdate`: The start date of the program. - `expirydate`: The expiration date of the program. - `id`: The ID of the transaction. - `created`: The timestamp of the creation of the loyalty program. - `amount`: The number of points in that transaction. - `archived`: Whether the session related to the transaction is archived. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export customer's transaction logs
        api_response = api_instance.export_loyalty_ledger(range_start, range_end, loyalty_program_id, integration_id, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_ledger: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export customer's transaction logs
        api_response = api_instance.export_loyalty_ledger(range_start, range_end, loyalty_program_id, integration_id, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_referrals**
> str export_referrals(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, valid=valid, usable=usable, batch_id=batch_id, date_format=date_format)

Export referrals

Download a CSV file containing the referrals that match the given parameters.  **Tip:** If the exported CSV file is too large to view, you can [split it into multiple files](https://www.makeuseof.com/tag/how-to-split-a-huge-csv-excel-workbook-into-seperate-files/).  The CSV file contains the following columns:  - `code`: The referral code. - `advocateprofileintegrationid`: The profile ID of the advocate. - `startdate`: The start date in RFC3339 of the code redemption period. - `expirydate`: The end date in RFC3339 of the code redemption period. - `limitval`: The maximum number of redemptions of this code. Defaults to `1` when left blank. - `attributes`: A json object describing _custom_ referral attribute names and their values. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | - `expired`: Matches referrals in which the expiration date is set and in the past. - `validNow`: Matches referrals in which start date is null or in the past and expiration date is null or in the future. - `validFuture`: Matches referrals in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | - `true`, only referrals where `usageCounter < usageLimit` will be returned. - `false`, only referrals where `usageCounter >= usageLimit` will be returned.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of referrals (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export referrals
        api_response = api_instance.export_referrals(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, valid=valid, usable=usable, batch_id=batch_id, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_referrals: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | - `expired`: Matches referrals in which the expiration date is set and in the past. - `validNow`: Matches referrals in which start date is null or in the past and expiration date is null or in the future. - `validFuture`: Matches referrals in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | - `true`, only referrals where `usageCounter < usageLimit` will be returned. - `false`, only referrals where `usageCounter >= usageLimit` will be returned.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of referrals (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export referrals
        api_response = api_instance.export_referrals(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, valid=valid, usable=usable, batch_id=batch_id, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_referrals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| - &#x60;expired&#x60;: Matches referrals in which the expiration date is set and in the past. - &#x60;validNow&#x60;: Matches referrals in which start date is null or in the past and expiration date is null or in the future. - &#x60;validFuture&#x60;: Matches referrals in which start date is set and in the future.  | [optional] 
 **usable** | **str**| - &#x60;true&#x60;, only referrals where &#x60;usageCounter &lt; usageLimit&#x60; will be returned. - &#x60;false&#x60;, only referrals where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60; will be returned.  | [optional] 
 **batch_id** | **str**| Filter results by batches of referrals | [optional] 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_logs_without_total_count**
> InlineResponse20018 get_access_logs_without_total_count(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

Get access logs for Application

Retrieve the list of API calls sent to the specified Application. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # Get access logs for Application
        api_response = api_instance.get_access_logs_without_total_count(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_access_logs_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # Get access logs for Application
        api_response = api_instance.get_access_logs_without_total_count(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_access_logs_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(account_id)

Get account details

Return the details of your companies Talon.One account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    account_id = 56 # int | The identifier of the account. Retrieve it via the [List users in account](https://docs.talon.one/management-api#operation/getUsers) endpoint in the `accountId` property. 

    try:
        # Get account details
        api_response = api_instance.get_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    account_id = 56 # int | The identifier of the account. Retrieve it via the [List users in account](https://docs.talon.one/management-api#operation/getUsers) endpoint in the `accountId` property. 

    try:
        # Get account details
        api_response = api_instance.get_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The identifier of the account. Retrieve it via the [List users in account](https://docs.talon.one/management-api#operation/getUsers) endpoint in the &#x60;accountId&#x60; property.  | 

### Return type

[**Account**](Account.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_analytics**
> AccountAnalytics get_account_analytics(account_id)

Get account analytics

Return the analytics of your Talon.One account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    account_id = 56 # int | The identifier of the account. Retrieve it via the [List users in account](https://docs.talon.one/management-api#operation/getUsers) endpoint in the `accountId` property. 

    try:
        # Get account analytics
        api_response = api_instance.get_account_analytics(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account_analytics: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    account_id = 56 # int | The identifier of the account. Retrieve it via the [List users in account](https://docs.talon.one/management-api#operation/getUsers) endpoint in the `accountId` property. 

    try:
        # Get account analytics
        api_response = api_instance.get_account_analytics(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The identifier of the account. Retrieve it via the [List users in account](https://docs.talon.one/management-api#operation/getUsers) endpoint in the &#x60;accountId&#x60; property.  | 

### Return type

[**AccountAnalytics**](AccountAnalytics.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_collection**
> Collection get_account_collection(collection_id)

Get account-level collection

Retrieve a given account-level collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Get account-level collection
        api_response = api_instance.get_account_collection(collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Get account-level collection
        api_response = api_instance.get_account_collection(collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 

### Return type

[**Collection**](Collection.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_cost**
> AccountAdditionalCost get_additional_cost(additional_cost_id)

Get additional cost

Returns the additional cost. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    additional_cost_id = 56 # int | The ID of the additional cost. You can find the ID the the Campaign Manager's URL when you display the details of the cost in **Account** > **Tools** > **Additional costs**. 

    try:
        # Get additional cost
        api_response = api_instance.get_additional_cost(additional_cost_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_additional_cost: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    additional_cost_id = 56 # int | The ID of the additional cost. You can find the ID the the Campaign Manager's URL when you display the details of the cost in **Account** > **Tools** > **Additional costs**. 

    try:
        # Get additional cost
        api_response = api_instance.get_additional_cost(additional_cost_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_additional_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_cost_id** | **int**| The ID of the additional cost. You can find the ID the the Campaign Manager&#39;s URL when you display the details of the cost in **Account** &gt; **Tools** &gt; **Additional costs**.  | 

### Return type

[**AccountAdditionalCost**](AccountAdditionalCost.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_costs**
> InlineResponse20032 get_additional_costs(page_size=page_size, skip=skip, sort=sort)

List additional costs

Returns all the defined additional costs for the account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List additional costs
        api_response = api_instance.get_additional_costs(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_additional_costs: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List additional costs
        api_response = api_instance.get_additional_costs(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_additional_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_logs**
> InlineResponse20019 get_all_access_logs(range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

List access logs

Fetches the access logs for the entire account. Sensitive requests (logins) are _always_ filtered from the logs. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List access logs
        api_response = api_instance.get_all_access_logs(range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_all_access_logs: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List access logs
        api_response = api_instance.get_all_access_logs(range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_all_access_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> InlineResponse20040 get_all_roles()

List roles

List all roles.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    
    try:
        # List roles
        api_response = api_instance.get_all_roles()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_all_roles: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    
    try:
        # List roles
        api_response = api_instance.get_all_roles()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_all_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> Application get_application(application_id)

Get Application

Get the application specified by the ID.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.

    try:
        # Get Application
        api_response = api_instance.get_application(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.

    try:
        # Get Application
        api_response = api_instance.get_application(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 

### Return type

[**Application**](Application.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_api_health**
> ApplicationApiHealth get_application_api_health(application_id)

Get Application health

Display the health of the Application and show the last time the Application was used.  You can also display this information from the **Settings** of an Application, in the **Developer Settings** menu. See the [docs](https://docs.talon.one/docs/dev/tutorials/monitoring-integration-status). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.

    try:
        # Get Application health
        api_response = api_instance.get_application_api_health(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_api_health: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.

    try:
        # Get Application health
        api_response = api_instance.get_application_api_health(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_api_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 

### Return type

[**ApplicationApiHealth**](ApplicationApiHealth.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customer**
> ApplicationCustomer get_application_customer(application_id, customer_id)

Get application's customer

Retrieve the customers of the specified application. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 

    try:
        # Get application's customer
        api_response = api_instance.get_application_customer(application_id, customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customer: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 

    try:
        # Get application's customer
        api_response = api_instance.get_application_customer(application_id, customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint.  | 

### Return type

[**ApplicationCustomer**](ApplicationCustomer.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customer_friends**
> InlineResponse20030 get_application_customer_friends(application_id, integration_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)

List friends referred by customer profile

List the friends referred by the specified customer profile in this Application. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
integration_id = 'integration_id_example' # str | The Integration ID of the Advocate's Profile.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List friends referred by customer profile
        api_response = api_instance.get_application_customer_friends(application_id, integration_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customer_friends: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
integration_id = 'integration_id_example' # str | The Integration ID of the Advocate's Profile.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List friends referred by customer profile
        api_response = api_instance.get_application_customer_friends(application_id, integration_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customer_friends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **integration_id** | **str**| The Integration ID of the Advocate&#39;s Profile. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customers**
> InlineResponse20021 get_application_customers(application_id, integration_id=integration_id, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)

List application's customers

List all the customers of the specified application.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
integration_id = 'integration_id_example' # str | Filter results performing an exact matching against the profile integration identifier. (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List application's customers
        api_response = api_instance.get_application_customers(application_id, integration_id=integration_id, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customers: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
integration_id = 'integration_id_example' # str | Filter results performing an exact matching against the profile integration identifier. (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List application's customers
        api_response = api_instance.get_application_customers(application_id, integration_id=integration_id, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **integration_id** | **str**| Filter results performing an exact matching against the profile integration identifier. | [optional] 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customers_by_attributes**
> InlineResponse20022 get_application_customers_by_attributes(application_id, body, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)

List application customers matching the given attributes

Get a list of the application customers matching the provided criteria.  The match is successful if all the attributes of the request are found in a profile, even if the profile has more attributes that are not present on the request. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.CustomerProfileSearchQuery() # CustomerProfileSearchQuery | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List application customers matching the given attributes
        api_response = api_instance.get_application_customers_by_attributes(application_id, body, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customers_by_attributes: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.CustomerProfileSearchQuery() # CustomerProfileSearchQuery | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List application customers matching the given attributes
        api_response = api_instance.get_application_customers_by_attributes(application_id, body, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customers_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | [**CustomerProfileSearchQuery**](CustomerProfileSearchQuery.md)| body | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_event_types**
> InlineResponse20028 get_application_event_types(application_id, page_size=page_size, skip=skip, sort=sort)

List Applications event types

Get all of the distinct values of the Event `type` property for events recorded in the application.  See also: [Track an event](https://docs.talon.one/integration-api#operation/trackEvent) 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List Applications event types
        api_response = api_instance.get_application_event_types(application_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_event_types: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List Applications event types
        api_response = api_instance.get_application_event_types(application_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_event_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_events_without_total_count**
> InlineResponse20027 get_application_events_without_total_count(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)

List Applications events

Lists all events recorded for an application. Instead of having the total number of results in the response, this endpoint only mentions whether there are more results. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
type = 'type_example' # str | Comma-separated list of types by which to filter events. Must be exact match(es). (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
session = 'session_example' # str | Session integration ID filter for events. Must be exact match. (optional)
profile = 'profile_example' # str | Profile integration ID filter for events. Must be exact match. (optional)
customer_name = 'customer_name_example' # str | Customer name filter for events. Will match substrings case-insensitively. (optional)
customer_email = 'customer_email_example' # str | Customer e-mail address filter for events. Will match substrings case-insensitively. (optional)
coupon_code = 'coupon_code_example' # str | Coupon code (optional)
referral_code = 'referral_code_example' # str | Referral code (optional)
rule_query = 'rule_query_example' # str | Rule name filter for events (optional)
campaign_query = 'campaign_query_example' # str | Campaign name filter for events (optional)

    try:
        # List Applications events
        api_response = api_instance.get_application_events_without_total_count(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_events_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
type = 'type_example' # str | Comma-separated list of types by which to filter events. Must be exact match(es). (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
session = 'session_example' # str | Session integration ID filter for events. Must be exact match. (optional)
profile = 'profile_example' # str | Profile integration ID filter for events. Must be exact match. (optional)
customer_name = 'customer_name_example' # str | Customer name filter for events. Will match substrings case-insensitively. (optional)
customer_email = 'customer_email_example' # str | Customer e-mail address filter for events. Will match substrings case-insensitively. (optional)
coupon_code = 'coupon_code_example' # str | Coupon code (optional)
referral_code = 'referral_code_example' # str | Referral code (optional)
rule_query = 'rule_query_example' # str | Rule name filter for events (optional)
campaign_query = 'campaign_query_example' # str | Campaign name filter for events (optional)

    try:
        # List Applications events
        api_response = api_instance.get_application_events_without_total_count(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_events_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **type** | **str**| Comma-separated list of types by which to filter events. Must be exact match(es). | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **session** | **str**| Session integration ID filter for events. Must be exact match. | [optional] 
 **profile** | **str**| Profile integration ID filter for events. Must be exact match. | [optional] 
 **customer_name** | **str**| Customer name filter for events. Will match substrings case-insensitively. | [optional] 
 **customer_email** | **str**| Customer e-mail address filter for events. Will match substrings case-insensitively. | [optional] 
 **coupon_code** | **str**| Coupon code | [optional] 
 **referral_code** | **str**| Referral code | [optional] 
 **rule_query** | **str**| Rule name filter for events | [optional] 
 **campaign_query** | **str**| Campaign name filter for events | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_session**
> ApplicationSession get_application_session(application_id, session_id)

Get Application session

Get the details of the given session. You can list the sessions with the [List Application sessions](https://docs.talon.one/management-api#tag/Customer-data/operation/getApplicationSessions) endpoint. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
session_id = 56 # int | The **internal** ID of the session. You can get the ID with the [List Application sessions](https://docs.talon.one/management-api#tag/Customer-data/operation/getApplicationSessions) endpoint. 

    try:
        # Get Application session
        api_response = api_instance.get_application_session(application_id, session_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_session: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
session_id = 56 # int | The **internal** ID of the session. You can get the ID with the [List Application sessions](https://docs.talon.one/management-api#tag/Customer-data/operation/getApplicationSessions) endpoint. 

    try:
        # Get Application session
        api_response = api_instance.get_application_session(application_id, session_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **session_id** | **int**| The **internal** ID of the session. You can get the ID with the [List Application sessions](https://docs.talon.one/management-api#tag/Customer-data/operation/getApplicationSessions) endpoint.  | 

### Return type

[**ApplicationSession**](ApplicationSession.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_sessions**
> InlineResponse20026 get_application_sessions(application_id, page_size=page_size, skip=skip, sort=sort, profile=profile, state=state, created_before=created_before, created_after=created_after, coupon=coupon, referral=referral, integration_id=integration_id)

List Application sessions

List all the sessions of the specified Application. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
profile = 'profile_example' # str | Profile integration ID filter for sessions. Must be exact match. (optional)
state = 'state_example' # str | Filter by sessions with this state. Must be exact match. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
coupon = 'coupon_example' # str | Filter by sessions with this coupon. Must be exact match. (optional)
referral = 'referral_example' # str | Filter by sessions with this referral. Must be exact match. (optional)
integration_id = 'integration_id_example' # str | Filter by sessions with this integrationId. Must be exact match. (optional)

    try:
        # List Application sessions
        api_response = api_instance.get_application_sessions(application_id, page_size=page_size, skip=skip, sort=sort, profile=profile, state=state, created_before=created_before, created_after=created_after, coupon=coupon, referral=referral, integration_id=integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_sessions: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
profile = 'profile_example' # str | Profile integration ID filter for sessions. Must be exact match. (optional)
state = 'state_example' # str | Filter by sessions with this state. Must be exact match. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
coupon = 'coupon_example' # str | Filter by sessions with this coupon. Must be exact match. (optional)
referral = 'referral_example' # str | Filter by sessions with this referral. Must be exact match. (optional)
integration_id = 'integration_id_example' # str | Filter by sessions with this integrationId. Must be exact match. (optional)

    try:
        # List Application sessions
        api_response = api_instance.get_application_sessions(application_id, page_size=page_size, skip=skip, sort=sort, profile=profile, state=state, created_before=created_before, created_after=created_after, coupon=coupon, referral=referral, integration_id=integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **profile** | **str**| Profile integration ID filter for sessions. Must be exact match. | [optional] 
 **state** | **str**| Filter by sessions with this state. Must be exact match. | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **coupon** | **str**| Filter by sessions with this coupon. Must be exact match. | [optional] 
 **referral** | **str**| Filter by sessions with this referral. Must be exact match. | [optional] 
 **integration_id** | **str**| Filter by sessions with this integrationId. Must be exact match. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> InlineResponse2003 get_applications(page_size=page_size, skip=skip, sort=sort)

List Applications

List all applications in the current account.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List Applications
        api_response = api_instance.get_applications(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_applications: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List Applications
        api_response = api_instance.get_applications(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> Attribute get_attribute(attribute_id)

Get custom attribute

Retrieve the specified custom attribute. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | The ID of the attribute. You can find the ID in the Campaign Manager's URL when you display the details of an attribute in **Account** > **Tools** > **Attributes**.

    try:
        # Get custom attribute
        api_response = api_instance.get_attribute(attribute_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_attribute: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | The ID of the attribute. You can find the ID in the Campaign Manager's URL when you display the details of an attribute in **Account** > **Tools** > **Attributes**.

    try:
        # Get custom attribute
        api_response = api_instance.get_attribute(attribute_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **int**| The ID of the attribute. You can find the ID in the Campaign Manager&#39;s URL when you display the details of an attribute in **Account** &gt; **Tools** &gt; **Attributes**. | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> InlineResponse20031 get_attributes(page_size=page_size, skip=skip, sort=sort, entity=entity)

List custom attributes

Return all the custom attributes for the account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
entity = 'entity_example' # str | Returned attributes will be filtered by supplied entity. (optional)

    try:
        # List custom attributes
        api_response = api_instance.get_attributes(page_size=page_size, skip=skip, sort=sort, entity=entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_attributes: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
entity = 'entity_example' # str | Returned attributes will be filtered by supplied entity. (optional)

    try:
        # List custom attributes
        api_response = api_instance.get_attributes(page_size=page_size, skip=skip, sort=sort, entity=entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **entity** | **str**| Returned attributes will be filtered by supplied entity. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences**
> InlineResponse20029 get_audiences(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)

List audiences

Get all audiences created in the account. To create an audience, use [Create audience](https://docs.talon.one/integration-api#tag/Audiences/operation/createAudienceV2). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List audiences
        api_response = api_instance.get_audiences(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_audiences: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)

    try:
        # List audiences
        api_response = api_instance.get_audiences(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> Campaign get_campaign(application_id, campaign_id)

Get campaign

Retrieve the given campaign.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.

    try:
        # Get campaign
        api_response = api_instance.get_campaign(application_id, campaign_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.

    try:
        # Get campaign
        api_response = api_instance.get_campaign(application_id, campaign_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_analytics**
> InlineResponse20020 get_campaign_analytics(application_id, campaign_id, range_start, range_end, granularity=granularity)

Get analytics of campaigns

Retrieve statistical data about the performance of the given campaign.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
granularity = 'granularity_example' # str | The time interval between the results in the returned time-series. (optional)

    try:
        # Get analytics of campaigns
        api_response = api_instance.get_campaign_analytics(application_id, campaign_id, range_start, range_end, granularity=granularity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_analytics: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
granularity = 'granularity_example' # str | The time interval between the results in the returned time-series. (optional)

    try:
        # Get analytics of campaigns
        api_response = api_instance.get_campaign_analytics(application_id, campaign_id, range_start, range_end, granularity=granularity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **granularity** | **str**| The time interval between the results in the returned time-series. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_by_attributes**
> InlineResponse2004 get_campaign_by_attributes(application_id, body, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state)

List campaigns that match the given attributes

Get a list of all the campaigns that match a set of attributes. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.CampaignSearch() # CampaignSearch | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)

    try:
        # List campaigns that match the given attributes
        api_response = api_instance.get_campaign_by_attributes(application_id, body, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_by_attributes: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.CampaignSearch() # CampaignSearch | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)

    try:
        # List campaigns that match the given attributes
        api_response = api_instance.get_campaign_by_attributes(application_id, body, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | [**CampaignSearch**](CampaignSearch.md)| body | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_templates**
> InlineResponse20010 get_campaign_templates(page_size=page_size, skip=skip, sort=sort, state=state, name=name, tags=tags, user_id=user_id)

List campaign templates

Retrieve a list of campaign templates.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
state = 'state_example' # str | Filter results by the state of the campaign template. (optional)
name = 'name_example' # str | Filter results performing case-insensitive matching against the name of the campaign template. (optional)
tags = 'tags_example' # str | Filter results performing case-insensitive matching against the tags of the campaign template. When used in conjunction with the \"name\" query parameter, a logical OR will be performed to search both tags and name for the provided values.  (optional)
user_id = 56 # int | Filter results by user ID. (optional)

    try:
        # List campaign templates
        api_response = api_instance.get_campaign_templates(page_size=page_size, skip=skip, sort=sort, state=state, name=name, tags=tags, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_templates: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
state = 'state_example' # str | Filter results by the state of the campaign template. (optional)
name = 'name_example' # str | Filter results performing case-insensitive matching against the name of the campaign template. (optional)
tags = 'tags_example' # str | Filter results performing case-insensitive matching against the tags of the campaign template. When used in conjunction with the \"name\" query parameter, a logical OR will be performed to search both tags and name for the provided values.  (optional)
user_id = 56 # int | Filter results by user ID. (optional)

    try:
        # List campaign templates
        api_response = api_instance.get_campaign_templates(page_size=page_size, skip=skip, sort=sort, state=state, name=name, tags=tags, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **state** | **str**| Filter results by the state of the campaign template. | [optional] 
 **name** | **str**| Filter results performing case-insensitive matching against the name of the campaign template. | [optional] 
 **tags** | **str**| Filter results performing case-insensitive matching against the tags of the campaign template. When used in conjunction with the \&quot;name\&quot; query parameter, a logical OR will be performed to search both tags and name for the provided values.  | [optional] 
 **user_id** | **int**| Filter results by user ID. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns**
> InlineResponse2004 get_campaigns(application_id, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state, name=name, tags=tags, created_before=created_before, created_after=created_after, campaign_group_id=campaign_group_id, template_id=template_id)

List campaigns

List the campaigns of the specified application that match your filter criteria. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)
name = 'name_example' # str | Filter results performing case-insensitive matching against the name of the campaign. (optional)
tags = 'tags_example' # str | Filter results performing case-insensitive matching against the tags of the campaign. When used in conjunction with the \"name\" query parameter, a logical OR will be performed to search both tags and name for the provided values  (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
campaign_group_id = 56 # int | Filter results to campaigns owned by the specified campaign group ID. (optional)
template_id = 56 # int | The ID of the Campaign Template this Campaign was created from. (optional)

    try:
        # List campaigns
        api_response = api_instance.get_campaigns(application_id, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state, name=name, tags=tags, created_before=created_before, created_after=created_after, campaign_group_id=campaign_group_id, template_id=template_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaigns: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)
name = 'name_example' # str | Filter results performing case-insensitive matching against the name of the campaign. (optional)
tags = 'tags_example' # str | Filter results performing case-insensitive matching against the tags of the campaign. When used in conjunction with the \"name\" query parameter, a logical OR will be performed to search both tags and name for the provided values  (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
campaign_group_id = 56 # int | Filter results to campaigns owned by the specified campaign group ID. (optional)
template_id = 56 # int | The ID of the Campaign Template this Campaign was created from. (optional)

    try:
        # List campaigns
        api_response = api_instance.get_campaigns(application_id, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state, name=name, tags=tags, created_before=created_before, created_after=created_after, campaign_group_id=campaign_group_id, template_id=template_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 
 **name** | **str**| Filter results performing case-insensitive matching against the name of the campaign. | [optional] 
 **tags** | **str**| Filter results performing case-insensitive matching against the tags of the campaign. When used in conjunction with the \&quot;name\&quot; query parameter, a logical OR will be performed to search both tags and name for the provided values  | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **campaign_group_id** | **int**| Filter results to campaigns owned by the specified campaign group ID. | [optional] 
 **template_id** | **int**| The ID of the Campaign Template this Campaign was created from. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changes**
> InlineResponse20038 get_changes(page_size=page_size, skip=skip, sort=sort, application_id=application_id, entity_path=entity_path, user_id=user_id, created_before=created_before, created_after=created_after, with_total_result_size=with_total_result_size, management_key_id=management_key_id, include_old=include_old)

Get audit logs for an account

Retrieve the audit logs displayed in **Accounts > Audit logs**. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
entity_path = 'entity_path_example' # str | Filter results on a case insensitive matching of the url path of the entity (optional)
user_id = 56 # int | Filter results by user ID. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
management_key_id = 56 # int | Filter results that match the given management key ID. (optional)
include_old = True # bool | When this flag is set to false, the state without the change will not be returned. The default value is true. (optional)

    try:
        # Get audit logs for an account
        api_response = api_instance.get_changes(page_size=page_size, skip=skip, sort=sort, application_id=application_id, entity_path=entity_path, user_id=user_id, created_before=created_before, created_after=created_after, with_total_result_size=with_total_result_size, management_key_id=management_key_id, include_old=include_old)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_changes: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
entity_path = 'entity_path_example' # str | Filter results on a case insensitive matching of the url path of the entity (optional)
user_id = 56 # int | Filter results by user ID. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
management_key_id = 56 # int | Filter results that match the given management key ID. (optional)
include_old = True # bool | When this flag is set to false, the state without the change will not be returned. The default value is true. (optional)

    try:
        # Get audit logs for an account
        api_response = api_instance.get_changes(page_size=page_size, skip=skip, sort=sort, application_id=application_id, entity_path=entity_path, user_id=user_id, created_before=created_before, created_after=created_after, with_total_result_size=with_total_result_size, management_key_id=management_key_id, include_old=include_old)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **entity_path** | **str**| Filter results on a case insensitive matching of the url path of the entity | [optional] 
 **user_id** | **int**| Filter results by user ID. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **management_key_id** | **int**| Filter results that match the given management key ID. | [optional] 
 **include_old** | **bool**| When this flag is set to false, the state without the change will not be returned. The default value is true. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> Collection get_collection(application_id, campaign_id, collection_id)

Get collection

Retrieve a given collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Get collection
        api_response = api_instance.get_collection(application_id, campaign_id, collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.

    try:
        # Get collection
        api_response = api_instance.get_collection(application_id, campaign_id, collection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 

### Return type

[**Collection**](Collection.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_items**
> InlineResponse20016 get_collection_items(collection_id, page_size=page_size, skip=skip)

Get collection items

Retrieve the items from the given collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # Get collection items
        api_response = api_instance.get_collection_items(collection_id, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_collection_items: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # Get collection items
        api_response = api_instance.get_collection_items(collection_id, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons_without_total_count**
> InlineResponse2008 get_coupons_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match)

List coupons

List all the coupons matching the specified criteria. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)

    try:
        # List coupons
        api_response = api_instance.get_coupons_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_coupons_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)

    try:
        # List coupons
        api_response = api_instance.get_coupons_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_coupons_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_activity_report**
> CustomerActivityReport get_customer_activity_report(range_start, range_end, application_id, customer_id, page_size=page_size, skip=skip)

Get customer's activity report

Fetch the summary report of a given customer in the given application, in a time range.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # Get customer's activity report
        api_response = api_instance.get_customer_activity_report(range_start, range_end, application_id, customer_id, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_activity_report: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # Get customer's activity report
        api_response = api_instance.get_customer_activity_report(range_start, range_end, application_id, customer_id, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_activity_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint.  | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**CustomerActivityReport**](CustomerActivityReport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_activity_reports_without_total_count**
> InlineResponse20025 get_customer_activity_reports_without_total_count(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)

Get Activity Reports for Application Customers

Fetch summary reports for all application customers based on a time range. Instead of having the total number of results in the response, this endpoint only mentions whether there are more results. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
name = 'name_example' # str | Only return reports matching the customer name (optional)
integration_id = 'integration_id_example' # str | Filter results performing an exact matching against the profile integration identifier. (optional)
campaign_name = 'campaign_name_example' # str | Only return reports matching the campaignName (optional)
advocate_name = 'advocate_name_example' # str | Only return reports matching the current customer referrer name (optional)

    try:
        # Get Activity Reports for Application Customers
        api_response = api_instance.get_customer_activity_reports_without_total_count(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_activity_reports_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp. This must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp. This must be an RFC3339 timestamp string.
application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
name = 'name_example' # str | Only return reports matching the customer name (optional)
integration_id = 'integration_id_example' # str | Filter results performing an exact matching against the profile integration identifier. (optional)
campaign_name = 'campaign_name_example' # str | Only return reports matching the campaignName (optional)
advocate_name = 'advocate_name_example' # str | Only return reports matching the current customer referrer name (optional)

    try:
        # Get Activity Reports for Application Customers
        api_response = api_instance.get_customer_activity_reports_without_total_count(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_activity_reports_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp. This must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp. This must be an RFC3339 timestamp string. | 
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **name** | **str**| Only return reports matching the customer name | [optional] 
 **integration_id** | **str**| Filter results performing an exact matching against the profile integration identifier. | [optional] 
 **campaign_name** | **str**| Only return reports matching the campaignName | [optional] 
 **advocate_name** | **str**| Only return reports matching the current customer referrer name | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_analytics**
> CustomerAnalytics get_customer_analytics(application_id, customer_id, page_size=page_size, skip=skip, sort=sort)

Get customer's analytics report

Fetch analytics for a given customer in the given application.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # Get customer's analytics report
        api_response = api_instance.get_customer_analytics(application_id, customer_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_analytics: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # Get customer's analytics report
        api_response = api_instance.get_customer_analytics(application_id, customer_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint.  | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**CustomerAnalytics**](CustomerAnalytics.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_profile**
> CustomerProfile get_customer_profile(customer_id)

Get customer profile

Return the details of the specified customer profile.  <div class=\"redoc-section\">   <p class=\"title\">Performance tips</p>    You can retrieve the same information via the Integration API, which can save you extra API requests. consider these options:    - Request the customer profile to be part of the response content using     [Update Customer Session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/updateCustomerSessionV2).   - Send an empty update with the [Update Customer Profile](https://docs.talon.one/integration-api#tag/Customer-profiles/operation/updateCustomerProfileV2) endpoint with `runRuleEngine=false`. </div> 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 

    try:
        # Get customer profile
        api_response = api_instance.get_customer_profile(customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_profile: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint. 

    try:
        # Get customer profile
        api_response = api_instance.get_customer_profile(customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](https://docs.talon.one/management-api#operation/getApplicationCustomers) endpoint.  | 

### Return type

[**CustomerProfile**](CustomerProfile.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_profiles**
> InlineResponse20024 get_customer_profiles(page_size=page_size, skip=skip, sandbox=sandbox)

List customer profiles

List all customer profiles.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sandbox = False # bool | Indicates whether you are pointing to a sandbox or Live customer. (optional) (default to False)

    try:
        # List customer profiles
        api_response = api_instance.get_customer_profiles(page_size=page_size, skip=skip, sandbox=sandbox)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_profiles: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sandbox = False # bool | Indicates whether you are pointing to a sandbox or Live customer. (optional) (default to False)

    try:
        # List customer profiles
        api_response = api_instance.get_customer_profiles(page_size=page_size, skip=skip, sandbox=sandbox)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sandbox** | **bool**| Indicates whether you are pointing to a sandbox or Live customer. | [optional] [default to False]

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_by_attributes**
> InlineResponse20023 get_customers_by_attributes(body, page_size=page_size, skip=skip, sandbox=sandbox)

List customer profiles matching the given attributes

Get a list of the customer profiles matching the provided criteria.  The match is successful if all the attributes of the request are found in a profile, even if the profile has more attributes that are not present on the request. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.CustomerProfileSearchQuery() # CustomerProfileSearchQuery | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sandbox = False # bool | Indicates whether you are pointing to a sandbox or Live customer. (optional) (default to False)

    try:
        # List customer profiles matching the given attributes
        api_response = api_instance.get_customers_by_attributes(body, page_size=page_size, skip=skip, sandbox=sandbox)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customers_by_attributes: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.CustomerProfileSearchQuery() # CustomerProfileSearchQuery | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sandbox = False # bool | Indicates whether you are pointing to a sandbox or Live customer. (optional) (default to False)

    try:
        # List customer profiles matching the given attributes
        api_response = api_instance.get_customers_by_attributes(body, page_size=page_size, skip=skip, sandbox=sandbox)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customers_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerProfileSearchQuery**](CustomerProfileSearchQuery.md)| body | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sandbox** | **bool**| Indicates whether you are pointing to a sandbox or Live customer. | [optional] [default to False]

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_types**
> InlineResponse20036 get_event_types(name=name, include_old_versions=include_old_versions, page_size=page_size, skip=skip, sort=sort)

List event types

Fetch all event type definitions for your account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    name = 'name_example' # str | Filter results to event types with the given name. This parameter implies `includeOldVersions`. (optional)
include_old_versions = False # bool | Include all versions of every event type. (optional) (default to False)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List event types
        api_response = api_instance.get_event_types(name=name, include_old_versions=include_old_versions, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_event_types: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    name = 'name_example' # str | Filter results to event types with the given name. This parameter implies `includeOldVersions`. (optional)
include_old_versions = False # bool | Include all versions of every event type. (optional) (default to False)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List event types
        api_response = api_instance.get_event_types(name=name, include_old_versions=include_old_versions, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_event_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter results to event types with the given name. This parameter implies &#x60;includeOldVersions&#x60;. | [optional] 
 **include_old_versions** | **bool**| Include all versions of every event type. | [optional] [default to False]
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exports**
> InlineResponse20039 get_exports(page_size=page_size, skip=skip, application_id=application_id, campaign_id=campaign_id, entity=entity)

Get exports

List all past exports 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
campaign_id = 56 # int | Filter by the campaign ID on which the limit counters are used. (optional)
entity = 'entity_example' # str | The name of the entity type that was exported. (optional)

    try:
        # Get exports
        api_response = api_instance.get_exports(page_size=page_size, skip=skip, application_id=application_id, campaign_id=campaign_id, entity=entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_exports: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
campaign_id = 56 # int | Filter by the campaign ID on which the limit counters are used. (optional)
entity = 'entity_example' # str | The name of the entity type that was exported. (optional)

    try:
        # Get exports
        api_response = api_instance.get_exports(page_size=page_size, skip=skip, application_id=application_id, campaign_id=campaign_id, entity=entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **campaign_id** | **int**| Filter by the campaign ID on which the limit counters are used. | [optional] 
 **entity** | **str**| The name of the entity type that was exported. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_card**
> LoyaltyCard get_loyalty_card(loyalty_program_id, loyalty_card_id)

Get loyalty card

Get the given loyalty card.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 

    try:
        # Get loyalty card
        api_response = api_instance.get_loyalty_card(loyalty_program_id, loyalty_card_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_card: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 

    try:
        # Get loyalty card
        api_response = api_instance.get_loyalty_card(loyalty_program_id, loyalty_card_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 

### Return type

[**LoyaltyCard**](LoyaltyCard.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_card_transaction_logs**
> InlineResponse20014 get_loyalty_card_transaction_logs(loyalty_program_id, loyalty_card_id, start_date=start_date, end_date=end_date, page_size=page_size, skip=skip, subledger_id=subledger_id)

List card's transactions

Retrieve the transaction logs for the given [loyalty card](https://docs.talon.one/docs/product/loyalty-programs/loyalty-cards/loyalty-card-overview) within the specified [card-based loyalty program](https://docs.talon.one/docs/product/loyalty-programs/overview#loyalty-program-types) with filtering options applied. If no filtering options are applied, the last 50 loyalty transactions for the given loyalty card are returned. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time from which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time by which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
subledger_id = 'subledger_id_example' # str | The ID of the subledger by which we filter the data. (optional)

    try:
        # List card's transactions
        api_response = api_instance.get_loyalty_card_transaction_logs(loyalty_program_id, loyalty_card_id, start_date=start_date, end_date=end_date, page_size=page_size, skip=skip, subledger_id=subledger_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_card_transaction_logs: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time from which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time by which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
subledger_id = 'subledger_id_example' # str | The ID of the subledger by which we filter the data. (optional)

    try:
        # List card's transactions
        api_response = api_instance.get_loyalty_card_transaction_logs(loyalty_program_id, loyalty_card_id, start_date=start_date, end_date=end_date, page_size=page_size, skip=skip, subledger_id=subledger_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_card_transaction_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 
 **start_date** | **datetime**| Date and time from which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 
 **end_date** | **datetime**| Date and time by which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **subledger_id** | **str**| The ID of the subledger by which we filter the data. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_cards**
> InlineResponse20013 get_loyalty_cards(loyalty_program_id, page_size=page_size, skip=skip, sort=sort, identifier=identifier, profile_id=profile_id)

List loyalty cards

For the given card-based loyalty program, list the loyalty cards that match your filter criteria. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
identifier = 'identifier_example' # str | Optional query parameter to search cards by identifier. (optional)
profile_id = 56 # int | Filter by the profile ID. (optional)

    try:
        # List loyalty cards
        api_response = api_instance.get_loyalty_cards(loyalty_program_id, page_size=page_size, skip=skip, sort=sort, identifier=identifier, profile_id=profile_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_cards: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
identifier = 'identifier_example' # str | Optional query parameter to search cards by identifier. (optional)
profile_id = 56 # int | Filter by the profile ID. (optional)

    try:
        # List loyalty cards
        api_response = api_instance.get_loyalty_cards(loyalty_program_id, page_size=page_size, skip=skip, sort=sort, identifier=identifier, profile_id=profile_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **identifier** | **str**| Optional query parameter to search cards by identifier. | [optional] 
 **profile_id** | **int**| Filter by the profile ID. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_points**
> LoyaltyLedger get_loyalty_points(loyalty_program_id, integration_id)

Get customer's full loyalty ledger

Get the loyalty ledger for this profile integration ID.  To get the `integrationId` of the profile from a `sessionId`, use the [Update customer session](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint.  **Important:** To get loyalty transaction logs for a given Integration ID in a loyalty program, we recommend using the Integration API's [Get customer's loyalty logs](https://docs.talon.one/integration-api#tag/Loyalty/operation/getLoyaltyProgramProfileTransactions). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.

    try:
        # Get customer's full loyalty ledger
        api_response = api_instance.get_loyalty_points(loyalty_program_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_points: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.

    try:
        # Get customer's full loyalty ledger
        api_response = api_instance.get_loyalty_points(loyalty_program_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 

### Return type

[**LoyaltyLedger**](LoyaltyLedger.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_program**
> LoyaltyProgram get_loyalty_program(loyalty_program_id)

Get loyalty program

Get the specified [loyalty program](https://docs.talon.one/docs/product/loyalty-programs/overview). To list all loyalty programs in your Application, use [List loyalty programs](#operation/getLoyaltyPrograms).  To list the loyalty programs that a customer profile is part of, use the [List customer data](https://docs.talon.one/integration-api#tag/Customer-profiles/operation/getCustomerInventory) 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 

    try:
        # Get loyalty program
        api_response = api_instance.get_loyalty_program(loyalty_program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_program: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 

    try:
        # Get loyalty program
        api_response = api_instance.get_loyalty_program(loyalty_program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 

### Return type

[**LoyaltyProgram**](LoyaltyProgram.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_program_transactions**
> InlineResponse20012 get_loyalty_program_transactions(loyalty_program_id, loyalty_transaction_type=loyalty_transaction_type, subledger_id=subledger_id, start_date=start_date, end_date=end_date, page_size=page_size, skip=skip)

List loyalty program transactions

Retrieve all loyalty program transaction logs in a given loyalty program with filtering options applied. Manual and imported transactions are also included. If no filters are applied, the last 50 loyalty transactions for the given loyalty program are returned.  **Important:** To get loyalty transaction logs for a given Integration ID in a loyalty program, we recommend using the Integration API's [Get customer's loyalty logs](https://docs.talon.one/integration-api#tag/Loyalty/operation/getLoyaltyProgramProfileTransactions). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_transaction_type = 'loyalty_transaction_type_example' # str | Filter results by loyalty transaction type: - `manual`: Loyalty transaction that was done manually. - `session`: Loyalty transaction that resulted from a customer session. - `import`: Loyalty transaction that was imported from a CSV file.  (optional)
subledger_id = 'subledger_id_example' # str | The ID of the subledger by which we filter the data. (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time from which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time by which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
page_size = 50 # int | The number of items in this response. (optional) (default to 50)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List loyalty program transactions
        api_response = api_instance.get_loyalty_program_transactions(loyalty_program_id, loyalty_transaction_type=loyalty_transaction_type, subledger_id=subledger_id, start_date=start_date, end_date=end_date, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_program_transactions: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_transaction_type = 'loyalty_transaction_type_example' # str | Filter results by loyalty transaction type: - `manual`: Loyalty transaction that was done manually. - `session`: Loyalty transaction that resulted from a customer session. - `import`: Loyalty transaction that was imported from a CSV file.  (optional)
subledger_id = 'subledger_id_example' # str | The ID of the subledger by which we filter the data. (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time from which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date and time by which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  (optional)
page_size = 50 # int | The number of items in this response. (optional) (default to 50)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List loyalty program transactions
        api_response = api_instance.get_loyalty_program_transactions(loyalty_program_id, loyalty_transaction_type=loyalty_transaction_type, subledger_id=subledger_id, start_date=start_date, end_date=end_date, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_program_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_transaction_type** | **str**| Filter results by loyalty transaction type: - &#x60;manual&#x60;: Loyalty transaction that was done manually. - &#x60;session&#x60;: Loyalty transaction that resulted from a customer session. - &#x60;import&#x60;: Loyalty transaction that was imported from a CSV file.  | [optional] 
 **subledger_id** | **str**| The ID of the subledger by which we filter the data. | [optional] 
 **start_date** | **datetime**| Date and time from which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 
 **end_date** | **datetime**| Date and time by which results are returned. Results are filtered by transaction creation date.  **Note:** It must be an RFC3339 timestamp string.  | [optional] 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 50]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_programs**
> InlineResponse20011 get_loyalty_programs()

List loyalty programs

List the loyalty programs of the account.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    
    try:
        # List loyalty programs
        api_response = api_instance.get_loyalty_programs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_programs: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    
    try:
        # List loyalty programs
        api_response = api_instance.get_loyalty_programs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_programs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_statistics**
> LoyaltyStatistics get_loyalty_statistics(loyalty_program_id)

Get loyalty program statistics

Retrieve the statistics of the specified loyalty program such as the total active points, pending points, spent points, and expired points.  **Important:** The returned data does not include the current day. All statistics are updated daily at 11:59 PM in the loyalty program time zone. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 

    try:
        # Get loyalty program statistics
        api_response = api_instance.get_loyalty_statistics(loyalty_program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_statistics: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 

    try:
        # Get loyalty program statistics
        api_response = api_instance.get_loyalty_statistics(loyalty_program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 

### Return type

[**LoyaltyStatistics**](LoyaltyStatistics.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_webhook**
> NotificationWebhook get_notification_webhook(application_id, notification_webhook_id)

Get notification about campaign-related changes

Return the given [notification about campaign-related changes](https://docs.talon.one/docs/product/applications/outbound-notifications). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
notification_webhook_id = 56 # int | The ID of the webhook. Get it with the appropriate _List notifications_ endpoint.

    try:
        # Get notification about campaign-related changes
        api_response = api_instance.get_notification_webhook(application_id, notification_webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_notification_webhook: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
notification_webhook_id = 56 # int | The ID of the webhook. Get it with the appropriate _List notifications_ endpoint.

    try:
        # Get notification about campaign-related changes
        api_response = api_instance.get_notification_webhook(application_id, notification_webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **notification_webhook_id** | **int**| The ID of the webhook. Get it with the appropriate _List notifications_ endpoint. | 

### Return type

[**NotificationWebhook**](NotificationWebhook.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_webhooks**
> InlineResponse2005 get_notification_webhooks(application_id)

List notifications about campaign-related changes

List all [notifications about campaign-related changes](https://docs.talon.one/docs/product/applications/outbound-notifications) for the given Application. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.

    try:
        # List notifications about campaign-related changes
        api_response = api_instance.get_notification_webhooks(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_notification_webhooks: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.

    try:
        # List notifications about campaign-related changes
        api_response = api_instance.get_notification_webhooks(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_notification_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_referrals_without_total_count**
> InlineResponse2009 get_referrals_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)

List referrals

List all referrals of the specified campaign.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
code = 'code_example' # str | Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches referrals in which the expiration date is set and in the past. The second matches referrals in which start date is null or in the past and expiration date is null or in the future, the third matches referrals in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only referrals where `usageCounter < usageLimit` will be returned, \"false\" will return only referrals where `usageCounter >= usageLimit`.  (optional)
advocate = 'advocate_example' # str | Filter results by match with a profile id specified in the referral's AdvocateProfileIntegrationId field (optional)

    try:
        # List referrals
        api_response = api_instance.get_referrals_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_referrals_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
code = 'code_example' # str | Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches referrals in which the expiration date is set and in the past. The second matches referrals in which start date is null or in the past and expiration date is null or in the future, the third matches referrals in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only referrals where `usageCounter < usageLimit` will be returned, \"false\" will return only referrals where `usageCounter >= usageLimit`.  (optional)
advocate = 'advocate_example' # str | Filter results by match with a profile id specified in the referral's AdvocateProfileIntegrationId field (optional)

    try:
        # List referrals
        api_response = api_instance.get_referrals_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_referrals_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **code** | **str**| Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches referrals in which the expiration date is set and in the past. The second matches referrals in which start date is null or in the past and expiration date is null or in the future, the third matches referrals in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only referrals where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only referrals where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **advocate** | **str**| Filter results by match with a profile id specified in the referral&#39;s AdvocateProfileIntegrationId field | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(role_id)

Get role

Get the details of the specified role. To see all the roles, use [List roles](#operation/getAllRoles). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    role_id = 56 # int | The Id of role. 

    try:
        # Get role
        api_response = api_instance.get_role(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_role: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    role_id = 56 # int | The Id of role. 

    try:
        # Get role
        api_response = api_instance.get_role(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| The Id of role.  | 

### Return type

[**Role**](Role.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ruleset**
> Ruleset get_ruleset(application_id, campaign_id, ruleset_id)

Get ruleset

Retrieve the specified ruleset.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
ruleset_id = 56 # int | The ID of the ruleset.

    try:
        # Get ruleset
        api_response = api_instance.get_ruleset(application_id, campaign_id, ruleset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_ruleset: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
ruleset_id = 56 # int | The ID of the ruleset.

    try:
        # Get ruleset
        api_response = api_instance.get_ruleset(application_id, campaign_id, ruleset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rulesets**
> InlineResponse2006 get_rulesets(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort)

List campaign rulesets

List all rulesets of this campaign. A ruleset is a revision of the rules of a campaign. **Important:** The response also includes deleted rules. You should only consider the latest revision of the returned rulesets. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List campaign rulesets
        api_response = api_instance.get_rulesets(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_rulesets: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List campaign rulesets
        api_response = api_instance.get_rulesets(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Get user

Retrieve the data (including an invitation code) for a user. Non-admin users can only get their own profile. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    user_id = 56 # int | The ID of the user.

    try:
        # Get user
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_user: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    user_id = 56 # int | The ID of the user.

    try:
        # Get user
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user. | 

### Return type

[**User**](User.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> InlineResponse20037 get_users(page_size=page_size, skip=skip, sort=sort)

List users in account

Retrieve all users in your account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List users in account
        api_response = api_instance.get_users(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_users: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)

    try:
        # List users in account
        api_response = api_instance.get_users(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Get webhook

Returns a webhook by its id.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    webhook_id = 56 # int | The ID of the webhook. You can find the ID in the Campaign Manager's URL when you display the details of the webhook in **Account** > **Webhooks**. 

    try:
        # Get webhook
        api_response = api_instance.get_webhook(webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhook: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    webhook_id = 56 # int | The ID of the webhook. You can find the ID in the Campaign Manager's URL when you display the details of the webhook in **Account** > **Webhooks**. 

    try:
        # Get webhook
        api_response = api_instance.get_webhook(webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**| The ID of the webhook. You can find the ID in the Campaign Manager&#39;s URL when you display the details of the webhook in **Account** &gt; **Webhooks**.  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_activation_logs**
> InlineResponse20034 get_webhook_activation_logs(page_size=page_size, skip=skip, sort=sort, integration_request_uuid=integration_request_uuid, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after)

List webhook activation log entries

Webhook activation log entries are created as soon as an integration request triggers a webhook effect. See the [docs](https://docs.talon.one/docs/dev/getting-started/webhooks). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
integration_request_uuid = 'integration_request_uuid_example' # str | Filter results by integration request UUID. (optional)
webhook_id = 3.4 # float | Filter results by Webhook. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)

    try:
        # List webhook activation log entries
        api_response = api_instance.get_webhook_activation_logs(page_size=page_size, skip=skip, sort=sort, integration_request_uuid=integration_request_uuid, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhook_activation_logs: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
integration_request_uuid = 'integration_request_uuid_example' # str | Filter results by integration request UUID. (optional)
webhook_id = 3.4 # float | Filter results by Webhook. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)

    try:
        # List webhook activation log entries
        api_response = api_instance.get_webhook_activation_logs(page_size=page_size, skip=skip, sort=sort, integration_request_uuid=integration_request_uuid, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhook_activation_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **integration_request_uuid** | **str**| Filter results by integration request UUID. | [optional] 
 **webhook_id** | **float**| Filter results by Webhook. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_logs**
> InlineResponse20035 get_webhook_logs(page_size=page_size, skip=skip, sort=sort, status=status, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, request_uuid=request_uuid, created_before=created_before, created_after=created_after)

List webhook log entries

Retrieve all webhook log entries.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
webhook_id = 3.4 # float | Filter results by Webhook. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
campaign_id = 3.4 # float | Filter results by campaign. (optional)
request_uuid = 'request_uuid_example' # str | Filter results by request UUID. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries before parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)

    try:
        # List webhook log entries
        api_response = api_instance.get_webhook_logs(page_size=page_size, skip=skip, sort=sort, status=status, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, request_uuid=request_uuid, created_before=created_before, created_after=created_after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhook_logs: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
webhook_id = 3.4 # float | Filter results by Webhook. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
campaign_id = 3.4 # float | Filter results by campaign. (optional)
request_uuid = 'request_uuid_example' # str | Filter results by request UUID. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries before parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)

    try:
        # List webhook log entries
        api_response = api_instance.get_webhook_logs(page_size=page_size, skip=skip, sort=sort, status=status, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, request_uuid=request_uuid, created_before=created_before, created_after=created_after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhook_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **webhook_id** | **float**| Filter results by Webhook. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **request_uuid** | **str**| Filter results by request UUID. | [optional] 
 **created_before** | **datetime**| Filter results where request and response times to return entries before parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> InlineResponse20033 get_webhooks(application_ids=application_ids, sort=sort, page_size=page_size, skip=skip)

List webhooks

List all webhooks.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_ids = 'application_ids_example' # str | Filter by one or more application IDs separated by a comma. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List webhooks
        api_response = api_instance.get_webhooks(application_ids=application_ids, sort=sort, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhooks: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_ids = 'application_ids_example' # str | Filter by one or more application IDs separated by a comma. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List webhooks
        api_response = api_instance.get_webhooks(application_ids=application_ids, sort=sort, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_ids** | **str**| Filter by one or more application IDs separated by a comma. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_account_collection**
> ModelImport import_account_collection(collection_id, up_file=up_file)

Import data in existing account-level collection

Upload a CSV file containing the collection of string values that should be attached as payload for collection. The file should be sent as multipart data.  The import **replaces** the initial content of the collection.  The CSV file **must** only contain the following column:  - `item`: the values in your collection.  A collection is limited to 500,000 items.  Example:  ``` item Addidas Nike Asics ```  **Note:** Before sending a request to this endpoint, ensure the data in the CSV to import is different from the data currently stored in the collection. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import data in existing account-level collection
        api_response = api_instance.import_account_collection(collection_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_account_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import data in existing account-level collection
        api_response = api_instance.import_account_collection(collection_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_account_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_allowed_list**
> ModelImport import_allowed_list(attribute_id, up_file=up_file)

Import allowed values for attribute

Upload a CSV file containing a list of [picklist values](https://docs.talon.one/docs/product/account/dev-tools/managing-attributes#picklist-values) for the specified attribute.  The file should be sent as multipart data.  The import **replaces** the previous list of allowed values for this attribute, if any.  The CSV file **must** only contain the following column: - `item` (required): the values in your allowed list, for example a list of SKU's.  An allowed list is limited to 500,000 items.  Example:  ```text item CS-VG-04032021-UP-50D-10 CS-DV-04042021-UP-49D-12 CS-DG-02082021-UP-50G-07 ``` 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | The ID of the attribute. You can find the ID in the Campaign Manager's URL when you display the details of an attribute in **Account** > **Tools** > **Attributes**.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import allowed values for attribute
        api_response = api_instance.import_allowed_list(attribute_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_allowed_list: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | The ID of the attribute. You can find the ID in the Campaign Manager's URL when you display the details of an attribute in **Account** > **Tools** > **Attributes**.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import allowed values for attribute
        api_response = api_instance.import_allowed_list(attribute_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_allowed_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **int**| The ID of the attribute. You can find the ID in the Campaign Manager&#39;s URL when you display the details of an attribute in **Account** &gt; **Tools** &gt; **Attributes**. | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_collection**
> ModelImport import_collection(application_id, campaign_id, collection_id, up_file=up_file)

Import data in existing collection

Upload a CSV file containing the collection of string values that should be attached as payload for collection. The file should be sent as multipart data.  The import **replaces** the initial content of the collection.  The CSV file **must** only contain the following column:  - `item`: the values in your collection.  A collection is limited to 500,000 items.  Example:  ``` item Addidas Nike Asics ```  **Note:** Before sending a request to this endpoint, ensure the data in the CSV to import is different from the data currently stored in the collection. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import data in existing collection
        api_response = api_instance.import_collection(application_id, campaign_id, collection_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import data in existing collection
        api_response = api_instance.import_collection(application_id, campaign_id, collection_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_coupons**
> ModelImport import_coupons(application_id, campaign_id, up_file=up_file)

Import coupons

Upload a CSV file containing the coupons that should be created. The file should be sent as multipart data.  The CSV file contains the following columns:  - `value` (required): The coupon code. - `expirydate`: The end date in RFC3339 of the code redemption period. - `startdate`: The start date in RFC3339 of the code redemption period. - `recipientintegrationid`: The integration ID of the customer who receives the coupon.   Only the customer with this integration ID can redeem the corresponding coupon code.   Learn about [coupon reservation](https://docs.talon.one/docs/product/rules/effects/using-effects#reserving-a-coupon-code). - `limitval`: The maximum number of redemptions of this code. For unlimited redemptions, use `0`. Defaults to `1` when not provided. - `discountlimit`: The total discount value that the code can give. This is typically used to represent a gift card value. - `attributes`: A json object describing _custom_ referral attribute names and their values. Double the double-quotes in the object.   For example, if you created a [custom attribute](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes)   called `category` associated to the coupon entity, set it with `\"{\"\"category\"\": \"\"10_off\"\"}\"`.  You can use the time zone of your choice. It is converted to UTC internally by Talon.One.  **Note:** We recommend limiting your file size to 500MB.  **Example:**  ```text \"value\",\"expirydate\",\"startdate\",\"recipientintegrationid\",\"limitval\",\"attributes\",\"discountlimit\" COUP1,2018-07-01T04:00:00Z,2018-05-01T04:00:00Z,cust123,1,\"{\"\"Category\"\": \"\"10_off\"\"}\",2.4 ```  Once imported, you can find the `batchId` in the Campaign Manager or by using [List coupons](#tag/Coupons/operation/getCouponsWithoutTotalCount). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import coupons
        api_response = api_instance.import_coupons(application_id, campaign_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_coupons: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import coupons
        api_response = api_instance.import_coupons(application_id, campaign_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_loyalty_cards**
> ModelImport import_loyalty_cards(loyalty_program_id, up_file=up_file)

Import loyalty cards

Upload a CSV file containing the loyalty cards that you want to use in your card-based loyalty program. Send the file as multipart data.  It contains the following columns for each card:  - `identifier` (required): The alphanumeric identifier of the loyalty card. - `state` (required): The state of the loyalty card. It can be `active` or `inactive`. - `customerprofileids` (optional): An array of strings representing the identifiers of the customer profiles linked to the loyalty card.  **Note:** We recommend limiting your file size to 500MB.  **Example:**  ```csv identifier,state,customerprofileids 123-456-789AT,active,Alexa001;UserA ``` 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import loyalty cards
        api_response = api_instance.import_loyalty_cards(loyalty_program_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_loyalty_cards: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import loyalty cards
        api_response = api_instance.import_loyalty_cards(loyalty_program_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_loyalty_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_loyalty_points**
> ModelImport import_loyalty_points(loyalty_program_id, up_file=up_file)

Import loyalty points

Upload a CSV file containing the loyalty points you want to import into a given loyalty program. Send the file as multipart data.  Depending on the loyalty program type, you can import the points into a given customer profile or into a given _active_ loyalty card.  The CSV file contains the following columns:  - `customerprofileid` (optional): For profile-based loyalty programs, the integration ID of the customer profile where the loyalty points are imported. - `identifier` (optional): For card-based loyalty programs, the identifier of the loyalty card where the loyalty points are imported. - `amount`: The amount of points to award to the customer profile. - `startdate`: The earliest date when the points can be redeemed. On this date and until the expiration date, the points are `active`. - `expirydate`: The latest date when the points can be redeemed. After this date, the points are `expired`. - `subledgerid` (optional): The ID of the subledger that should received the points. - `reason` (optional): The reason why these points are awarded.  You can use the time zone of your choice. It is converted to UTC internally by Talon.One.  **Note:** For existing customer profiles and loyalty cards, the imported points are added to any previous active or pending points, depending on the value provided for `startdate`. If `startdate` matches the current date, the imported points are _active_. If it is later, the points are _pending_ until the date provided for `startdate` is reached.  **Note:** We recommend limiting your file size to 500MB.  **Example for profile-based programs:**  ```text customerprofileid,amount,startdate,expirydate,subledgerid,reason URNGV8294NV,100,2009-11-10T23:00:00Z,2009-11-11T23:00:00Z,subledger1,appeasement ```  **Example for card-based programs:**  ```text identifier,amount,startdate,expirydate,subledgerid,reason summer-loyalty-card-0543,100,2009-11-10T23:00:00Z,2009-11-11T23:00:00Z,subledger1,appeasement ``` 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import loyalty points
        api_response = api_instance.import_loyalty_points(loyalty_program_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_loyalty_points: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import loyalty points
        api_response = api_instance.import_loyalty_points(loyalty_program_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_pool_giveaways**
> ModelImport import_pool_giveaways(pool_id, up_file=up_file)

Import giveaway codes into a giveaway pool

Upload a CSV file containing the giveaway codes that should be created. Send the file as multipart data.  The CSV file contains the following columns: - `code` (required): the code of your giveaway, for instance, a gift card redemption code. - `startdate`:  the start date in RFC3339 of the code redemption period. - `enddate`: the last date in RFC3339 of the code redemption period. - `attributes`: A json object describing _custom_ giveaway attribute names and their values. Double the double-quotes in the object.   For example, if you [created a custom attribute](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes)   called `provider` associated to the giveaway entity, set it with `\"{\"\"provider\"\": \"\"myPartnerCompany\"\"}\"`.  The `startdate` and `enddate` have nothing to do with the _validity_ of the codes. They are only used by the Rule Engine to award the codes or not. You can use the time zone of your choice. It is converted to UTC internally by Talon.One.  **Note:** We recommend limiting your file size to 500MB.  **Example:**  ```text code,startdate,enddate,attributes GIVEAWAY1,2020-11-10T23:00:00Z,2022-11-11T23:00:00Z,\"{\"\"provider\"\": \"\"Amazon\"\"}\" GIVEAWAY2,2020-11-10T23:00:00Z,2022-11-11T23:00:00Z,\"{\"\"provider\"\": \"\"Amazon\"\"}\" GIVEAWAY3,2021-01-10T23:00:00Z,2022-11-11T23:00:00Z,\"{\"\"provider\"\": \"\"Aliexpress\"\"}\" ``` 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    pool_id = 56 # int | The ID of the pool. You can find it in the Campaign Manager, in the **Giveaways** section.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import giveaway codes into a giveaway pool
        api_response = api_instance.import_pool_giveaways(pool_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_pool_giveaways: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    pool_id = 56 # int | The ID of the pool. You can find it in the Campaign Manager, in the **Giveaways** section.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import giveaway codes into a giveaway pool
        api_response = api_instance.import_pool_giveaways(pool_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_pool_giveaways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| The ID of the pool. You can find it in the Campaign Manager, in the **Giveaways** section. | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_referrals**
> ModelImport import_referrals(application_id, campaign_id, up_file=up_file)

Import referrals

Upload a CSV file containing the referrals that should be created. The file should be sent as multipart data.  The CSV file contains the following columns:  - `code` (required): The referral code. - `advocateprofileintegrationid` (required): The profile ID of the advocate. - `startdate`: The start date in RFC3339 of the code redemption period. - `expirydate`: The end date in RFC3339 of the code redemption period. - `limitval`: The maximum number of redemptions of this code. Defaults to `1` when left blank. - `attributes`: A json object describing _custom_ referral attribute names and their values. Double the double-quotes in the object.    For example, if you [created a custom attribute](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes)   called `category` associated to the referral entity, set it with `\"{\"\"category\"\": \"\"10_off\"\"}\"`.  You can use the time zone of your choice. It is converted to UTC internally by Talon.One.  **Note:** We recommend limiting your file size to 500MB.  **Example:**  ```text code,startdate,expirydate,advocateprofileintegrationid,limitval,attributes REFERRAL_CODE1,2020-11-10T23:00:00Z,2021-11-11T23:00:00Z,integid_4,1,\"{\"\"my_attribute\"\": \"\"10_off\"\"}\" REFERRAL_CODE2,2020-11-10T23:00:00Z,2021-11-11T23:00:00Z,integid1,1,\"{\"\"my_attribute\"\": \"\"20_off\"\"}\" ``` 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import referrals
        api_response = api_instance.import_referrals(application_id, campaign_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_referrals: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
up_file = 'up_file_example' # str | The file with the information about the data that should be imported. (optional)

    try:
        # Import referrals
        api_response = api_instance.import_referrals(application_id, campaign_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_referrals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_collections**
> InlineResponse20015 list_account_collections(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)

List collections in account

List collections in account.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
name = 'name_example' # str | Filter by the name of the Collection. (optional)

    try:
        # List collections in account
        api_response = api_instance.list_account_collections(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->list_account_collections: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
name = 'name_example' # str | Filter by the name of the Collection. (optional)

    try:
        # List collections in account
        api_response = api_instance.list_account_collections(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->list_account_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **name** | **str**| Filter by the name of the Collection. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> InlineResponse20017 list_collections(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)

List collections

List collections in the campaign.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
name = 'name_example' # str | Filter by the name of the Collection. (optional)

    try:
        # List collections
        api_response = api_instance.list_collections(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->list_collections: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
name = 'name_example' # str | Filter by the name of the Collection. (optional)

    try:
        # List collections
        api_response = api_instance.list_collections(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->list_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **name** | **str**| Filter by the name of the Collection. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections_in_application**
> InlineResponse20017 list_collections_in_application(application_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)

List collections in application

List collections from all campaigns in the Application.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
name = 'name_example' # str | Filter by the name of the Collection. (optional)

    try:
        # List collections in application
        api_response = api_instance.list_collections_in_application(application_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->list_collections_in_application: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
name = 'name_example' # str | Filter by the name of the Collection. (optional)

    try:
        # List collections in application
        api_response = api_instance.list_collections_in_application(application_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->list_collections_in_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **name** | **str**| Filter by the name of the Collection. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_added_deducted_points_notification**
> BaseNotification post_added_deducted_points_notification(loyalty_program_id, body)

Create notification about added or deducted loyalty points

Create a notification about added or deducted loyalty points in a given profile-based loyalty program. A notification for added or deducted loyalty points is different from regular webhooks in that it is loyalty program-scoped and has a predefined payload.  For more information, see [Managing notifications](https://docs.talon.one/docs/product/loyalty-programs/managing-notifications). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
body = talon_one.NewBaseNotification() # NewBaseNotification | body

    try:
        # Create notification about added or deducted loyalty points
        api_response = api_instance.post_added_deducted_points_notification(loyalty_program_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->post_added_deducted_points_notification: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
body = talon_one.NewBaseNotification() # NewBaseNotification | body

    try:
        # Create notification about added or deducted loyalty points
        api_response = api_instance.post_added_deducted_points_notification(loyalty_program_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->post_added_deducted_points_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **body** | [**NewBaseNotification**](NewBaseNotification.md)| body | 

### Return type

[**BaseNotification**](BaseNotification.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_catalogs_strikethrough_notification**
> BaseNotification post_catalogs_strikethrough_notification(application_id, body)

Create strikethrough notification

Create a notification for the in the given Application. For more information, see [Managing notifications](https://docs.talon.one/docs/product/applications/outbound-notifications).  See the [payload](https://docs.talon.one/outbound-notifications) you will receive. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.NewBaseNotification() # NewBaseNotification | body

    try:
        # Create strikethrough notification
        api_response = api_instance.post_catalogs_strikethrough_notification(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->post_catalogs_strikethrough_notification: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = talon_one.NewBaseNotification() # NewBaseNotification | body

    try:
        # Create strikethrough notification
        api_response = api_instance.post_catalogs_strikethrough_notification(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->post_catalogs_strikethrough_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewBaseNotification**](NewBaseNotification.md)| body | 

### Return type

[**BaseNotification**](BaseNotification.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_loyalty_points**
> remove_loyalty_points(loyalty_program_id, integration_id, body)

Deduct points from customer profile

Deduct points from the specified loyalty program and specified customer profile.  To get the `integrationId` of the profile from a `sessionId`, use the [Update customer session](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
body = talon_one.DeductLoyaltyPoints() # DeductLoyaltyPoints | body

    try:
        # Deduct points from customer profile
        api_instance.remove_loyalty_points(loyalty_program_id, integration_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->remove_loyalty_points: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
body = talon_one.DeductLoyaltyPoints() # DeductLoyaltyPoints | body

    try:
        # Deduct points from customer profile
        api_instance.remove_loyalty_points(loyalty_program_id, integration_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->remove_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 
 **body** | [**DeductLoyaltyPoints**](DeductLoyaltyPoints.md)| body | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> NewPassword reset_password(body)

Reset password

Consumes the supplied password reset token and updates the password for the associated account. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewPassword() # NewPassword | body

    try:
        # Reset password
        api_response = api_instance.reset_password(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->reset_password: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    body = talon_one.NewPassword() # NewPassword | body

    try:
        # Reset password
        api_response = api_instance.reset_password(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewPassword**](NewPassword.md)| body | 

### Return type

[**NewPassword**](NewPassword.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_coupons_advanced_application_wide_without_total_count**
> InlineResponse2008 search_coupons_advanced_application_wide_without_total_count(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)

List coupons that match the given attributes (without total count)

List the coupons whose attributes match the query criteria in all **active** campaigns of the given Application.  The match is successful if all the attributes of the request are found in a coupon, even if the coupon has more attributes that are not present on the request.  **Note:** The total count is not included in the response. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = None # object | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)

    try:
        # List coupons that match the given attributes (without total count)
        api_response = api_instance.search_coupons_advanced_application_wide_without_total_count(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_application_wide_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
body = None # object | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign.  - `enabled`: Campaigns that are scheduled, running (activated), or expired. - `running`: Campaigns that are running (activated). - `disabled`: Campaigns that are disabled. - `expired`: Campaigns that are expired. - `archived`: Campaigns that are archived. - `draft`: Campaigns that are drafts.  (optional)

    try:
        # List coupons that match the given attributes (without total count)
        api_response = api_instance.search_coupons_advanced_application_wide_without_total_count(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_application_wide_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | **object**| body | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_coupons_advanced_without_total_count**
> InlineResponse2008 search_coupons_advanced_without_total_count(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)

List coupons that match the given attributes in campaign (without total count)

List the coupons whose attributes match the query criteria in the given campaign.  The match is successful if all the attributes of the request are found in a coupon, even if the coupon has more attributes that are not present on the request.  **Note:** The total count is not included in the response. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = None # object | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)

    try:
        # List coupons that match the given attributes in campaign (without total count)
        api_response = api_instance.search_coupons_advanced_without_total_count(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_without_total_count: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = None # object | body
page_size = 1000 # int | The number of items in this response. (optional) (default to 1000)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with `-`.  **Note:** This parameter works only with numeric fields.  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)

    try:
        # List coupons that match the given attributes in campaign (without total count)
        api_response = api_instance.search_coupons_advanced_without_total_count(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | **object**| body | 
 **page_size** | **int**| The number of items in this response. | [optional] [default to 1000]
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. By default, results are sorted in ascending order. To sort them in descending order, prefix the field name with &#x60;-&#x60;.  **Note:** This parameter works only with numeric fields.  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiration date is set and in the past. The second matches coupons in which start date is null or in the past and expiration date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the ID of a referral. This filter shows the coupons created by redeeming a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_loyalty_card**
> transfer_loyalty_card(loyalty_program_id, loyalty_card_id, body)

Transfer card data

Transfer loyalty card data, such as linked customers, loyalty balances and transactions, from a given loyalty card to a new, automatically created loyalty card.  **Important:**  - The original card is automatically blocked once the new card is created, and it cannot be activated again. - The default status of the new card is _active_. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.TransferLoyaltyCard() # TransferLoyaltyCard | body

    try:
        # Transfer card data
        api_instance.transfer_loyalty_card(loyalty_program_id, loyalty_card_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->transfer_loyalty_card: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.TransferLoyaltyCard() # TransferLoyaltyCard | body

    try:
        # Transfer card data
        api_instance.transfer_loyalty_card(loyalty_program_id, loyalty_card_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->transfer_loyalty_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 
 **body** | [**TransferLoyaltyCard**](TransferLoyaltyCard.md)| body | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_collection**
> Collection update_account_collection(collection_id, body)

Update account-level collection

Edit the description of the account-level collection and enable or disable the collection in the specified Applications.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
body = talon_one.UpdateCollection() # UpdateCollection | body

    try:
        # Update account-level collection
        api_response = api_instance.update_account_collection(collection_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_account_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
body = talon_one.UpdateCollection() # UpdateCollection | body

    try:
        # Update account-level collection
        api_response = api_instance.update_account_collection(collection_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_account_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 
 **body** | [**UpdateCollection**](UpdateCollection.md)| body | 

### Return type

[**Collection**](Collection.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**409** | Conflict. A Collection with this name already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_additional_cost**
> AccountAdditionalCost update_additional_cost(additional_cost_id, body)

Update additional cost

Updates an existing additional cost. Once created, the only property of an additional cost that can be changed is the title (human readable description). This restriction is in place to prevent accidentally breaking live integrations. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    additional_cost_id = 56 # int | The ID of the additional cost. You can find the ID the the Campaign Manager's URL when you display the details of the cost in **Account** > **Tools** > **Additional costs**. 
body = talon_one.NewAdditionalCost() # NewAdditionalCost | body

    try:
        # Update additional cost
        api_response = api_instance.update_additional_cost(additional_cost_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_additional_cost: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    additional_cost_id = 56 # int | The ID of the additional cost. You can find the ID the the Campaign Manager's URL when you display the details of the cost in **Account** > **Tools** > **Additional costs**. 
body = talon_one.NewAdditionalCost() # NewAdditionalCost | body

    try:
        # Update additional cost
        api_response = api_instance.update_additional_cost(additional_cost_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_additional_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_cost_id** | **int**| The ID of the additional cost. You can find the ID the the Campaign Manager&#39;s URL when you display the details of the cost in **Account** &gt; **Tools** &gt; **Additional costs**.  | 
 **body** | [**NewAdditionalCost**](NewAdditionalCost.md)| body | 

### Return type

[**AccountAdditionalCost**](AccountAdditionalCost.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute**
> Attribute update_attribute(attribute_id, body)

Update custom attribute

Update an existing custom attribute. Once created, the only property of a custom attribute that can be changed is the description.  To change the `type` or `name` property of a custom attribute, create a new attribute and update any relevant integrations and rules to use the new attribute. 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | The ID of the attribute. You can find the ID in the Campaign Manager's URL when you display the details of an attribute in **Account** > **Tools** > **Attributes**.
body = talon_one.NewAttribute() # NewAttribute | body

    try:
        # Update custom attribute
        api_response = api_instance.update_attribute(attribute_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_attribute: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | The ID of the attribute. You can find the ID in the Campaign Manager's URL when you display the details of an attribute in **Account** > **Tools** > **Attributes**.
body = talon_one.NewAttribute() # NewAttribute | body

    try:
        # Update custom attribute
        api_response = api_instance.update_attribute(attribute_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **int**| The ID of the attribute. You can find the ID in the Campaign Manager&#39;s URL when you display the details of an attribute in **Account** &gt; **Tools** &gt; **Attributes**. | 
 **body** | [**NewAttribute**](NewAttribute.md)| body | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign**
> Campaign update_campaign(application_id, campaign_id, body)

Update campaign

Update the given campaign.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.UpdateCampaign() # UpdateCampaign | body

    try:
        # Update campaign
        api_response = api_instance.update_campaign(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_campaign: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.UpdateCampaign() # UpdateCampaign | body

    try:
        # Update campaign
        api_response = api_instance.update_campaign(application_id, campaign_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**UpdateCampaign**](UpdateCampaign.md)| body | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> Collection update_collection(application_id, campaign_id, collection_id, body)

Update collection description

Edit the description of the collection.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
body = talon_one.UpdateCampaignCollection() # UpdateCampaignCollection | body

    try:
        # Update collection description
        api_response = api_instance.update_collection(application_id, campaign_id, collection_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_collection: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint.
body = talon_one.UpdateCampaignCollection() # UpdateCampaignCollection | body

    try:
        # Update collection description
        api_response = api_instance.update_collection(application_id, campaign_id, collection_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account](#operation/listCollectionsInApplication) endpoint. | 
 **body** | [**UpdateCampaignCollection**](UpdateCampaignCollection.md)| body | 

### Return type

[**Collection**](Collection.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon**
> Coupon update_coupon(application_id, campaign_id, coupon_id, body)

Update coupon

Update the specified coupon.  <div class=\"redoc-section\">   <p class=\"title\">Important</p>    <p>With this PUT endpoint only, any property you do not explicitly set in your request   will be set to <code>null</code>.</p>  </div> 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
coupon_id = 'coupon_id_example' # str | The internal ID of the coupon code. You can find this value in the `id` property from the [List coupons](https://docs.talon.one/management-api#tag/Coupons/operation/getCouponsWithoutTotalCount) endpoint response. 
body = talon_one.UpdateCoupon() # UpdateCoupon | body

    try:
        # Update coupon
        api_response = api_instance.update_coupon(application_id, campaign_id, coupon_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_coupon: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
coupon_id = 'coupon_id_example' # str | The internal ID of the coupon code. You can find this value in the `id` property from the [List coupons](https://docs.talon.one/management-api#tag/Coupons/operation/getCouponsWithoutTotalCount) endpoint response. 
body = talon_one.UpdateCoupon() # UpdateCoupon | body

    try:
        # Update coupon
        api_response = api_instance.update_coupon(application_id, campaign_id, coupon_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **coupon_id** | **str**| The internal ID of the coupon code. You can find this value in the &#x60;id&#x60; property from the [List coupons](https://docs.talon.one/management-api#tag/Coupons/operation/getCouponsWithoutTotalCount) endpoint response.  | 
 **body** | [**UpdateCoupon**](UpdateCoupon.md)| body | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_batch**
> update_coupon_batch(application_id, campaign_id, body)

Update coupons

Update all coupons, or a specific batch of coupons, in a campaign. You can find the `batchId` in the **Coupons** view of your Application in the Campaign Manager, or you can use [List coupons](#operation/getCouponsWithoutTotalCount).  <div class=\"redoc-section\">   <p class=\"title\">Important</p>    <ul>     <li>Only send sequential requests to this endpoint.</li>     <li>Requests to this endpoint timeout after 30 minutes. If you hit a timeout, reach out to our support team.</li>   </ul>  </div>  To update a specific coupon, use [Update coupon](#operation/updateCoupon). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.UpdateCouponBatch() # UpdateCouponBatch | body

    try:
        # Update coupons
        api_instance.update_coupon_batch(application_id, campaign_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_coupon_batch: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
body = talon_one.UpdateCouponBatch() # UpdateCouponBatch | body

    try:
        # Update coupons
        api_instance.update_coupon_batch(application_id, campaign_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_coupon_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **body** | [**UpdateCouponBatch**](UpdateCouponBatch.md)| body | 

### Return type

void (empty response body)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_card**
> LoyaltyCard update_loyalty_card(loyalty_program_id, loyalty_card_id, body)

Update loyalty card status

Update the status of the given loyalty card. A card can be _active_ or _inactive_.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.UpdateLoyaltyCard() # UpdateLoyaltyCard | body

    try:
        # Update loyalty card status
        api_response = api_instance.update_loyalty_card(loyalty_program_id, loyalty_card_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_loyalty_card: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    loyalty_program_id = 56 # int | Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint. 
loyalty_card_id = 'loyalty_card_id_example' # str | Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint. 
body = talon_one.UpdateLoyaltyCard() # UpdateLoyaltyCard | body

    try:
        # Update loyalty card status
        api_response = api_instance.update_loyalty_card(loyalty_program_id, loyalty_card_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_loyalty_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the card-based loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs](https://docs.talon.one/management-api#tag/Loyalty/operation/getLoyaltyPrograms) endpoint.  | 
 **loyalty_card_id** | **str**| Identifier of the loyalty card. You can get the identifier with the [List loyalty cards](https://docs.talon.one/management-api#tag/Loyalty-cards/operation/getLoyaltyCards) endpoint.  | 
 **body** | [**UpdateLoyaltyCard**](UpdateLoyaltyCard.md)| body | 

### Return type

[**LoyaltyCard**](LoyaltyCard.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_webhook**
> NotificationWebhook update_notification_webhook(application_id, notification_webhook_id, body)

Update notification about campaign-related changes

Update the given [notification about campaign-related changes](https://docs.talon.one/docs/product/applications/outbound-notifications).  **Tip:** You can review the payload you will receive in the [specs](https://docs.talon.one/outbound-notifications#/paths/campaign_edited/post). 

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
notification_webhook_id = 56 # int | The ID of the webhook. Get it with the appropriate _List notifications_ endpoint.
body = talon_one.NewNotificationWebhook() # NewNotificationWebhook | body

    try:
        # Update notification about campaign-related changes
        api_response = api_instance.update_notification_webhook(application_id, notification_webhook_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_notification_webhook: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
notification_webhook_id = 56 # int | The ID of the webhook. Get it with the appropriate _List notifications_ endpoint.
body = talon_one.NewNotificationWebhook() # NewNotificationWebhook | body

    try:
        # Update notification about campaign-related changes
        api_response = api_instance.update_notification_webhook(application_id, notification_webhook_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **notification_webhook_id** | **int**| The ID of the webhook. Get it with the appropriate _List notifications_ endpoint. | 
 **body** | [**NewNotificationWebhook**](NewNotificationWebhook.md)| body | 

### Return type

[**NotificationWebhook**](NotificationWebhook.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_referral**
> Referral update_referral(application_id, campaign_id, referral_id, body)

Update referral

Update the specified referral.

### Example

* Api Key Authentication (management_key):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
referral_id = 'referral_id_example' # str | The ID of the referral code.
body = talon_one.UpdateReferral() # UpdateReferral | body

    try:
        # Update referral
        api_response = api_instance.update_referral(application_id, campaign_id, referral_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_referral: %s\n" % e)
```

* Api Key Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://yourbaseurl.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: manager_auth
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
campaign_id = 56 # int | The ID of the campaign. It is displayed in your Talon.One deployment URL.
referral_id = 'referral_id_example' # str | The ID of the referral code.
body = talon_one.UpdateReferral() # UpdateReferral | body

    try:
        # Update referral
        api_response = api_instance.update_referral(application_id, campaign_id, referral_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_referral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **campaign_id** | **int**| The ID of the campaign. It is displayed in your Talon.One deployment URL. | 
 **referral_id** | **str**| The ID of the referral code. | 
 **body** | [**UpdateReferral**](UpdateReferral.md)| body | 

### Return type

[**Referral**](Referral.md)

### Authorization

[management_key](../README.md#management_key), [manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

