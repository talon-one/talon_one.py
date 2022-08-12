# talon_one.ManagementApi

All URIs are relative to *https://yourbaseurl.talon.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_loyalty_points**](ManagementApi.md#add_loyalty_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/add_points | Add points in loyalty program for given customer
[**copy_campaign_to_applications**](ManagementApi.md#copy_campaign_to_applications) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/copy | Copy the campaign into the specified application
[**create_account_collection**](ManagementApi.md#create_account_collection) | **POST** /v1/collections | Create account-level collection
[**create_additional_cost**](ManagementApi.md#create_additional_cost) | **POST** /v1/additional_costs | Create additional cost
[**create_attribute**](ManagementApi.md#create_attribute) | **POST** /v1/attributes | Create custom attribute
[**create_campaign_from_template**](ManagementApi.md#create_campaign_from_template) | **POST** /v1/applications/{applicationId}/create_campaign_from_template | Create campaign from campaign template
[**create_collection**](ManagementApi.md#create_collection) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/collections | Create collection
[**create_coupons**](ManagementApi.md#create_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Create coupons
[**create_coupons_async**](ManagementApi.md#create_coupons_async) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_async | Create coupons asynchronously
[**create_coupons_for_multiple_recipients**](ManagementApi.md#create_coupons_for_multiple_recipients) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_with_recipients | Create coupons for multiple recipients
[**create_notification_webhook**](ManagementApi.md#create_notification_webhook) | **POST** /v1/applications/{applicationId}/notification_webhooks | Create notification webhook
[**create_password_recovery_email**](ManagementApi.md#create_password_recovery_email) | **POST** /v1/password_recovery_emails | Request a password reset
[**create_session**](ManagementApi.md#create_session) | **POST** /v1/sessions | Create session
[**delete_account_collection**](ManagementApi.md#delete_account_collection) | **DELETE** /v1/collections/{collectionId} | Delete account-level collection
[**delete_campaign**](ManagementApi.md#delete_campaign) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId} | Delete campaign
[**delete_collection**](ManagementApi.md#delete_collection) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Delete collection
[**delete_coupon**](ManagementApi.md#delete_coupon) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Delete coupon
[**delete_coupons**](ManagementApi.md#delete_coupons) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Delete coupons
[**delete_notification_webhook**](ManagementApi.md#delete_notification_webhook) | **DELETE** /v1/applications/{applicationId}/notification_webhooks/{notificationWebhookId} | Delete notification webhook
[**delete_referral**](ManagementApi.md#delete_referral) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Delete referral
[**destroy_session**](ManagementApi.md#destroy_session) | **DELETE** /v1/sessions | Destroy session
[**export_account_collection_items**](ManagementApi.md#export_account_collection_items) | **GET** /v1/collections/{collectionId}/export | Export account-level collection&#39;s items
[**export_collection_items**](ManagementApi.md#export_collection_items) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId}/export | Export a collection&#39;s items
[**export_coupons**](ManagementApi.md#export_coupons) | **GET** /v1/applications/{applicationId}/export_coupons | Export coupons
[**export_customer_sessions**](ManagementApi.md#export_customer_sessions) | **GET** /v1/applications/{applicationId}/export_customer_sessions | Export customer sessions
[**export_effects**](ManagementApi.md#export_effects) | **GET** /v1/applications/{applicationId}/export_effects | Export triggered effects
[**export_loyalty_balance**](ManagementApi.md#export_loyalty_balance) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_customer_balance | Export customer loyalty balance to a CSV file
[**export_loyalty_ledger**](ManagementApi.md#export_loyalty_ledger) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/export_log | Export a customer&#39;s loyalty ledger log
[**export_referrals**](ManagementApi.md#export_referrals) | **GET** /v1/applications/{applicationId}/export_referrals | Export referrals
[**get_access_logs_without_total_count**](ManagementApi.md#get_access_logs_without_total_count) | **GET** /v1/applications/{applicationId}/access_logs/no_total | Get access logs for Application
[**get_account**](ManagementApi.md#get_account) | **GET** /v1/accounts/{accountId} | Get account details
[**get_account_analytics**](ManagementApi.md#get_account_analytics) | **GET** /v1/accounts/{accountId}/analytics | Get account analytics
[**get_account_collection**](ManagementApi.md#get_account_collection) | **GET** /v1/collections/{collectionId} | Get account-level collection
[**get_additional_cost**](ManagementApi.md#get_additional_cost) | **GET** /v1/additional_costs/{additionalCostId} | Get additional cost
[**get_additional_costs**](ManagementApi.md#get_additional_costs) | **GET** /v1/additional_costs | List additional costs
[**get_all_access_logs**](ManagementApi.md#get_all_access_logs) | **GET** /v1/access_logs | List access logs
[**get_all_roles**](ManagementApi.md#get_all_roles) | **GET** /v1/roles | List roles
[**get_application**](ManagementApi.md#get_application) | **GET** /v1/applications/{applicationId} | Get application
[**get_application_api_health**](ManagementApi.md#get_application_api_health) | **GET** /v1/applications/{applicationId}/health_report | Get report of health of application API
[**get_application_customer**](ManagementApi.md#get_application_customer) | **GET** /v1/applications/{applicationId}/customers/{customerId} | Get application&#39;s customer
[**get_application_customer_friends**](ManagementApi.md#get_application_customer_friends) | **GET** /v1/applications/{applicationId}/profile/{integrationId}/friends | List friends referred by customer profile
[**get_application_customers**](ManagementApi.md#get_application_customers) | **GET** /v1/applications/{applicationId}/customers | List application&#39;s customers
[**get_application_customers_by_attributes**](ManagementApi.md#get_application_customers_by_attributes) | **POST** /v1/applications/{applicationId}/customer_search | List application customers matching the given attributes
[**get_application_event_types**](ManagementApi.md#get_application_event_types) | **GET** /v1/applications/{applicationId}/event_types | List Applications event types
[**get_application_events_without_total_count**](ManagementApi.md#get_application_events_without_total_count) | **GET** /v1/applications/{applicationId}/events/no_total | List Applications events
[**get_application_session**](ManagementApi.md#get_application_session) | **GET** /v1/applications/{applicationId}/sessions/{sessionId} | Get Application session
[**get_application_sessions**](ManagementApi.md#get_application_sessions) | **GET** /v1/applications/{applicationId}/sessions | List Application sessions
[**get_applications**](ManagementApi.md#get_applications) | **GET** /v1/applications | List applications
[**get_attribute**](ManagementApi.md#get_attribute) | **GET** /v1/attributes/{attributeId} | Get custom attribute
[**get_attributes**](ManagementApi.md#get_attributes) | **GET** /v1/attributes | List custom attributes
[**get_audiences**](ManagementApi.md#get_audiences) | **GET** /v1/audiences | List audiences
[**get_campaign**](ManagementApi.md#get_campaign) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId} | Get campaign
[**get_campaign_analytics**](ManagementApi.md#get_campaign_analytics) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/analytics | Get analytics of campaigns
[**get_campaign_by_attributes**](ManagementApi.md#get_campaign_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns_search | List campaigns that match the given attributes
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
[**get_loyalty_points**](ManagementApi.md#get_loyalty_points) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId} | Get the Loyalty Ledger for this integrationID
[**get_loyalty_program**](ManagementApi.md#get_loyalty_program) | **GET** /v1/loyalty_programs/{loyaltyProgramId} | Get loyalty program
[**get_loyalty_programs**](ManagementApi.md#get_loyalty_programs) | **GET** /v1/loyalty_programs | List loyalty programs
[**get_loyalty_statistics**](ManagementApi.md#get_loyalty_statistics) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/statistics | Get loyalty program statistics by loyalty program ID
[**get_notification_webhook**](ManagementApi.md#get_notification_webhook) | **GET** /v1/applications/{applicationId}/notification_webhooks/{notificationWebhookId} | Get notification webhook
[**get_notification_webhooks**](ManagementApi.md#get_notification_webhooks) | **GET** /v1/applications/{applicationId}/notification_webhooks | List notification webhooks
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
[**import_loyalty_points**](ManagementApi.md#import_loyalty_points) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/import_points | Import loyalty points
[**import_pool_giveaways**](ManagementApi.md#import_pool_giveaways) | **POST** /v1/giveaways/pools/{poolId}/import | Import giveaway codes into a giveaway pool
[**import_referrals**](ManagementApi.md#import_referrals) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_referrals | Import referrals
[**list_account_collections**](ManagementApi.md#list_account_collections) | **GET** /v1/collections | List collections in account
[**list_collections**](ManagementApi.md#list_collections) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections | List collections
[**list_collections_in_application**](ManagementApi.md#list_collections_in_application) | **GET** /v1/applications/{applicationId}/collections | List collections in application
[**remove_loyalty_points**](ManagementApi.md#remove_loyalty_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/deduct_points | Deduct points in loyalty program for given customer
[**reset_password**](ManagementApi.md#reset_password) | **POST** /v1/reset_password | Reset password
[**search_coupons_advanced_application_wide_without_total_count**](ManagementApi.md#search_coupons_advanced_application_wide_without_total_count) | **POST** /v1/applications/{applicationId}/coupons_search_advanced/no_total | List coupons that match the given attributes (without total count)
[**search_coupons_advanced_without_total_count**](ManagementApi.md#search_coupons_advanced_without_total_count) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced/no_total | List coupons that match the given attributes in campaign (without total count)
[**update_account_collection**](ManagementApi.md#update_account_collection) | **PUT** /v1/collections/{collectionId} | Update account-level collection
[**update_additional_cost**](ManagementApi.md#update_additional_cost) | **PUT** /v1/additional_costs/{additionalCostId} | Update additional cost
[**update_attribute**](ManagementApi.md#update_attribute) | **PUT** /v1/attributes/{attributeId} | Update custom attribute
[**update_campaign**](ManagementApi.md#update_campaign) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId} | Update campaign
[**update_collection**](ManagementApi.md#update_collection) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Update collection description
[**update_coupon**](ManagementApi.md#update_coupon) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Update coupon
[**update_coupon_batch**](ManagementApi.md#update_coupon_batch) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Update coupons
[**update_notification_webhook**](ManagementApi.md#update_notification_webhook) | **PUT** /v1/applications/{applicationId}/notification_webhooks/{notificationWebhookId} | Update notification webhook
[**update_referral**](ManagementApi.md#update_referral) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Update referral


# **add_loyalty_points**
> add_loyalty_points(loyalty_program_id, integration_id, body)

Add points in loyalty program for given customer

Add points in the specified loyalty program for the given customer.  To get the `integrationId` of the profile from a `sessionId`, use the [Update customer session](/integration-api/#operation/updateCustomerSessionV2). 

### Example

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
body = talon_one.LoyaltyPoints() # LoyaltyPoints | 

    try:
        # Add points in loyalty program for given customer
        api_instance.add_loyalty_points(loyalty_program_id, integration_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->add_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 
 **body** | [**LoyaltyPoints**](LoyaltyPoints.md)|  | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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
> InlineResponse2002 copy_campaign_to_applications(application_id, campaign_id, body)

Copy the campaign into the specified application

Copy the campaign into all specified application.

### Example

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
body = talon_one.CampaignCopy() # CampaignCopy | 

    try:
        # Copy the campaign into the specified application
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
 **body** | [**CampaignCopy**](CampaignCopy.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    body = talon_one.NewCollection() # NewCollection | 

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
 **body** | [**NewCollection**](NewCollection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Create an [additional cost](/docs/product/account/dev-tools/managing-additional-costs/).  These additional costs are shared across all applications in your account, and are never required. 

### Example

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
    body = talon_one.NewAdditionalCost() # NewAdditionalCost | 

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
 **body** | [**NewAdditionalCost**](NewAdditionalCost.md)|  | 

### Return type

[**AccountAdditionalCost**](AccountAdditionalCost.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Create a _custom attribute_ in this account. Custom attributes allow you to attach new fields to Talon.One domain objects like campaigns, coupons, customers and so on.  These attributes can then be given values when creating/updating these objects, and these values can be used in your campaign rules. For example, you could define a `zipCode` field for customer sessions, and add a rule to your campaign that only allows certain ZIP codes.  These attributes are shared across all applications in your account, and are never required. 

### Example

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
    body = talon_one.NewAttribute() # NewAttribute | 

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
 **body** | [**NewAttribute**](NewAttribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
body = talon_one.CreateTemplateCampaign() # CreateTemplateCampaign | 

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
 **body** | [**CreateTemplateCampaign**](CreateTemplateCampaign.md)|  | 

### Return type

[**CreateTemplateCampaignResponse**](CreateTemplateCampaignResponse.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
body = talon_one.NewCampaignCollection() # NewCampaignCollection | 

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
 **body** | [**NewCampaignCollection**](NewCampaignCollection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons**
> InlineResponse2005 create_coupons(application_id, campaign_id, body, silent=silent)

Create coupons

Create coupons according to some pattern. Up to 20.000 coupons can be created without a unique prefix. When a unique prefix is provided, up to 200.000 coupons can be created.

### Example

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
body = talon_one.NewCoupons() # NewCoupons | 
silent = 'yes' # str | Possible values: `yes` or `no`. - `yes`: Increases the perfomance of the API call by returning a 204 response. - `no`: Returns a 200 response that contains essential data such as the updated customer profiles and session-related information.  (optional) (default to 'yes')

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
 **body** | [**NewCoupons**](NewCoupons.md)|  | 
 **silent** | **str**| Possible values: &#x60;yes&#x60; or &#x60;no&#x60;. - &#x60;yes&#x60;: Increases the perfomance of the API call by returning a 204 response. - &#x60;no&#x60;: Returns a 200 response that contains essential data such as the updated customer profiles and session-related information.  | [optional] [default to &#39;yes&#39;]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Create any number of coupons from 20,001 to 5,000,000.

### Example

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
body = talon_one.NewCouponCreationJob() # NewCouponCreationJob | 

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
 **body** | [**NewCouponCreationJob**](NewCouponCreationJob.md)|  | 

### Return type

[**AsyncCouponCreationResponse**](AsyncCouponCreationResponse.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons_for_multiple_recipients**
> InlineResponse2005 create_coupons_for_multiple_recipients(application_id, campaign_id, body, silent=silent)

Create coupons for multiple recipients

Create coupons according to some pattern for up to 1000 recipients.

### Example

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
body = talon_one.NewCouponsForMultipleRecipients() # NewCouponsForMultipleRecipients | 
silent = 'yes' # str | Possible values: `yes` or `no`. - `yes`: Increases the perfomance of the API call by returning a 204 response. - `no`: Returns a 200 response that contains essential data such as the updated customer profiles and session-related information.  (optional) (default to 'yes')

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
 **body** | [**NewCouponsForMultipleRecipients**](NewCouponsForMultipleRecipients.md)|  | 
 **silent** | **str**| Possible values: &#x60;yes&#x60; or &#x60;no&#x60;. - &#x60;yes&#x60;: Increases the perfomance of the API call by returning a 204 response. - &#x60;no&#x60;: Returns a 200 response that contains essential data such as the updated customer profiles and session-related information.  | [optional] [default to &#39;yes&#39;]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Create notification webhook

Create an outbound notification webhook. An outbound notification webhook is different from regular webhooks in that it is application-scoped and has a predefined payload (regular webhooks have user-definable payloads). 

### Example

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
body = talon_one.NewNotificationWebhook() # NewNotificationWebhook | 

    try:
        # Create notification webhook
        api_response = api_instance.create_notification_webhook(application_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **body** | [**NewNotificationWebhook**](NewNotificationWebhook.md)|  | 

### Return type

[**NotificationWebhook**](NotificationWebhook.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Send an email with a password recovery link to the email address of an existing account. 

### Example

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
    body = talon_one.NewPasswordEmail() # NewPasswordEmail | 

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
 **body** | [**NewPasswordEmail**](NewPasswordEmail.md)|  | 

### Return type

[**NewPasswordEmail**](NewPasswordEmail.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Create a session to use the Management API endpoints. Use the value of the `token` property provided in the response as bearer token in other API calls.  A token is valid for 3 months. In accordance with best pratices, use your generated token for all your API requests. Do **not** regenerate a token for each request.  This endpoint has a rate limit of 3 to 6 requests per second per account, depending on your setup.  **Note:** You can also use your browser's developer's console when you log into the Campaign Manager. Keep in mind that logging out destroys the token displayed in the console. 

### Example

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
    body = talon_one.LoginParams() # LoginParams | 

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
 **body** | [**LoginParams**](LoginParams.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_collection**
> delete_account_collection(collection_id)

Delete account-level collection

Delete the given account-level collection.

### Example

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
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).

    try:
        # Delete account-level collection
        api_instance.delete_account_collection(collection_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_account_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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

[manager_auth](../README.md#manager_auth)

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
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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
coupon_id = 'coupon_id_example' # str | The ID of the coupon code to update

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
 **coupon_id** | **str**| The ID of the coupon code to update | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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
valid = 'valid_example' # str | - `expired`: Matches coupons in which the expiry date is set and in the past. - `validNow`: Matches coupons in which start date is null or in the past and expiry date is null or in the future. - `validFuture`: Matches coupons in which start date is set and in the future.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
usable = 'usable_example' # str | - `true`: only coupons where `usageCounter < usageLimit` will be returned. - `false`: only coupons where `usageCounter >= usageLimit` will be returned.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
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
 **valid** | **str**| - &#x60;expired&#x60;: Matches coupons in which the expiry date is set and in the past. - &#x60;validNow&#x60;: Matches coupons in which start date is null or in the past and expiry date is null or in the future. - &#x60;validFuture&#x60;: Matches coupons in which start date is set and in the future.  | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **usable** | **str**| - &#x60;true&#x60;: only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned. - &#x60;false&#x60;: only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60; will be returned.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s &#x60;RecipientIntegrationId&#x60; field.  | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_webhook**
> delete_notification_webhook(application_id, notification_webhook_id)

Delete notification webhook

Remove the given existing outbound notification webhook.

### Example

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
notification_webhook_id = 56 # int | 

    try:
        # Delete notification webhook
        api_instance.delete_notification_webhook(application_id, notification_webhook_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **notification_webhook_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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
referral_id = 'referral_id_example' # str | The ID of the referral code to delete

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
 **referral_id** | **str**| The ID of the referral code to delete | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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

[manager_auth](../README.md#manager_auth)

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

Download a CSV file containing items from an account-level collection.

### Example

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
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

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

Download a CSV file containing a collection's items.

### Example

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
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

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

Download a CSV file containing the coupons that match the given properties.

### Example

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
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
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
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

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

Download a CSV file containing the customer sessions that match the request.  **Important:** Archived sessions cannot be exported. See the [retention policy](https://docs.talon.one/docs/product/server-infrastructure-and-data-retention#data-retention-policy). 

### Example

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

[manager_auth](../README.md#manager_auth)

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

Download a CSV file containing the triggered effects that match the given attributes. 

### Example

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

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_balance**
> str export_loyalty_balance(loyalty_program_id)

Export customer loyalty balance to a CSV file

Download a CSV file containing the balance of each customer in the loyalty program.

### Example

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

    try:
        # Export customer loyalty balance to a CSV file
        api_response = api_instance.export_loyalty_balance(loyalty_program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

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

# **export_loyalty_ledger**
> str export_loyalty_ledger(range_start, range_end, loyalty_program_id, integration_id, date_format=date_format)

Export a customer's loyalty ledger log

Download a CSV file containing a customer's ledger log in the loyalty program

### Example

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
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string.
loyalty_program_id = 'loyalty_program_id_example' # str | The identifier for the loyalty program.
integration_id = 'integration_id_example' # str | The identifier of the profile.
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export a customer's loyalty ledger log
        api_response = api_instance.export_loyalty_ledger(range_start, range_end, loyalty_program_id, integration_id, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string. | 
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

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

Download a CSV file containing the referrals that match the given parameters.

### Example

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
valid = 'valid_example' # str | - `expired`: Matches referrals in which the expiry date is set and in the past. - `validNow`: Matches referrals in which start date is null or in the past and expiry date is null or in the future. - `validFuture`: Matches referrals in which start date is set and in the future.  (optional)
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
 **valid** | **str**| - &#x60;expired&#x60;: Matches referrals in which the expiry date is set and in the past. - &#x60;validNow&#x60;: Matches referrals in which start date is null or in the past and expiry date is null or in the future. - &#x60;validFuture&#x60;: Matches referrals in which start date is set and in the future.  | [optional] 
 **usable** | **str**| - &#x60;true&#x60;, only referrals where &#x60;usageCounter &lt; usageLimit&#x60; will be returned. - &#x60;false&#x60;, only referrals where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60; will be returned.  | [optional] 
 **batch_id** | **str**| Filter results by batches of referrals | [optional] 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_logs_without_total_count**
> InlineResponse20012 get_access_logs_without_total_count(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

Get access logs for Application

Retrieve the list of API calls to this Application matching the specified criteria. 

### Example

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
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string.
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string. | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    account_id = 56 # int | The identifier of the account. Retrieve it via the [List users in account endpoint](https://docs.talon.one/management-api#operation/getUsers), in the `accountId` property. 

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
 **account_id** | **int**| The identifier of the account. Retrieve it via the [List users in account endpoint](https://docs.talon.one/management-api#operation/getUsers), in the &#x60;accountId&#x60; property.  | 

### Return type

[**Account**](Account.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    account_id = 56 # int | The identifier of the account. Retrieve it via the [List users in account endpoint](https://docs.talon.one/management-api#operation/getUsers), in the `accountId` property. 

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
 **account_id** | **int**| The identifier of the account. Retrieve it via the [List users in account endpoint](https://docs.talon.one/management-api#operation/getUsers), in the &#x60;accountId&#x60; property.  | 

### Return type

[**AccountAnalytics**](AccountAnalytics.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 

### Return type

[**Collection**](Collection.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    additional_cost_id = 56 # int | 

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
 **additional_cost_id** | **int**|  | 

### Return type

[**AccountAdditionalCost**](AccountAdditionalCost.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_costs**
> InlineResponse20025 get_additional_costs(page_size=page_size, skip=skip, sort=sort)

List additional costs

Returns all the defined additional costs for the account. 

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_logs**
> InlineResponse20013 get_all_access_logs(range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

List access logs

Fetches the access logs for the entire account. Sensitive requests (logins) are _always_ filtered from the logs. 

### Example

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
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string.
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string. | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> InlineResponse20033 get_all_roles()

List roles

List all roles.

### Example

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

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Get application

Get the application specified by the ID.

### Example

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
        # Get application
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

[manager_auth](../README.md#manager_auth)

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

Get report of health of application API

Display the health of the application and show the last time the Application was used. 

### Example

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
        # Get report of health of application API
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

[manager_auth](../README.md#manager_auth)

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
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint. 

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
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint.  | 

### Return type

[**ApplicationCustomer**](ApplicationCustomer.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customer_friends**
> InlineResponse20023 get_application_customer_friends(application_id, integration_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)

List friends referred by customer profile

List the friends referred by the specified customer profile in this Application. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customers**
> InlineResponse20015 get_application_customers(application_id, integration_id=integration_id, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)

List application's customers

List all the customers of the specified application.

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customers_by_attributes**
> InlineResponse20016 get_application_customers_by_attributes(application_id, body, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)

List application customers matching the given attributes

Get a list of the application customers matching the provided criteria.  The match is successful if all the attributes of the request are found in a profile, even if the profile has more attributes that are not present on the request. 

### Example

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
body = talon_one.CustomerProfileSearchQuery() # CustomerProfileSearchQuery | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
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
 **body** | [**CustomerProfileSearchQuery**](CustomerProfileSearchQuery.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_event_types**
> InlineResponse20021 get_application_event_types(application_id, page_size=page_size, skip=skip, sort=sort)

List Applications event types

Get all of the distinct values of the Event `type` property for events recorded in the application.  See also: [Track an event](/integration-api/#operation/trackEvent) 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_events_without_total_count**
> InlineResponse20020 get_application_events_without_total_count(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)

List Applications events

Lists all events recorded for an application. Instead of having the total number of results in the response, this endpoint only mentions whether there are more results. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
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

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Get the details of the given session. You can list the sessions with the [List Application sessions](/#tag/Customer-data/operation/getApplicationSession) endpoint. 

### Example

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
session_id = 56 # int | The **internal** ID of the session. You can get the ID with the [List Application sessions endpoint](/#tag/Customer-data/operation/getApplicationSession). 

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
 **session_id** | **int**| The **internal** ID of the session. You can get the ID with the [List Application sessions endpoint](/#tag/Customer-data/operation/getApplicationSession).  | 

### Return type

[**ApplicationSession**](ApplicationSession.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_sessions**
> InlineResponse20019 get_application_sessions(application_id, page_size=page_size, skip=skip, sort=sort, profile=profile, state=state, created_before=created_before, created_after=created_after, coupon=coupon, referral=referral, integration_id=integration_id)

List Application sessions

List all the sessions of the specified Application. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **profile** | **str**| Profile integration ID filter for sessions. Must be exact match. | [optional] 
 **state** | **str**| Filter by sessions with this state. Must be exact match. | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **coupon** | **str**| Filter by sessions with this coupon. Must be exact match. | [optional] 
 **referral** | **str**| Filter by sessions with this referral. Must be exact match. | [optional] 
 **integration_id** | **str**| Filter by sessions with this integrationId. Must be exact match. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> InlineResponse2001 get_applications(page_size=page_size, skip=skip, sort=sort)

List applications

List all applications in the current account.

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

    try:
        # List applications
        api_response = api_instance.get_applications(page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Returns custom attribute for the account by its id. 

### Example

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
    attribute_id = 56 # int | 

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
 **attribute_id** | **int**|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> InlineResponse20024 get_attributes(page_size=page_size, skip=skip, sort=sort, entity=entity)

List custom attributes

Returns all the defined custom attributes for the account. 

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **entity** | **str**| Returned attributes will be filtered by supplied entity. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences**
> InlineResponse20022 get_audiences(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)

List audiences

Get all audiences created in the account. To create an audience, use [Create audience](https://docs.talon.one/integration-api#tag/Audiences/operation/createAudienceV2). 

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_analytics**
> InlineResponse20014 get_campaign_analytics(application_id, campaign_id, range_start, range_end, granularity=granularity)

Get analytics of campaigns

Retrieve statistical data about the performance of the given campaign.

### Example

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
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string.
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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string. | 
 **granularity** | **str**| The time interval between the results in the returned time-series. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_by_attributes**
> InlineResponse2002 get_campaign_by_attributes(application_id, body, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state)

List campaigns that match the given attributes

Get a list of all the campaigns that match a set of attributes. 

### Example

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
body = talon_one.CampaignSearch() # CampaignSearch | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **body** | [**CampaignSearch**](CampaignSearch.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns**
> InlineResponse2002 get_campaigns(application_id, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state, name=name, tags=tags, created_before=created_before, created_after=created_after, campaign_group_id=campaign_group_id, template_id=template_id)

List campaigns

List the campaigns of the specified application that match your filter criteria. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 
 **name** | **str**| Filter results performing case-insensitive matching against the name of the campaign. | [optional] 
 **tags** | **str**| Filter results performing case-insensitive matching against the tags of the campaign. When used in conjunction with the \&quot;name\&quot; query parameter, a logical OR will be performed to search both tags and name for the provided values  | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **campaign_group_id** | **int**| Filter results to campaigns owned by the specified campaign group ID. | [optional] 
 **template_id** | **int**| The ID of the Campaign Template this Campaign was created from. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
> InlineResponse20031 get_changes(page_size=page_size, skip=skip, sort=sort, application_id=application_id, entity_path=entity_path, user_id=user_id, created_before=created_before, created_after=created_after, with_total_result_size=with_total_result_size, include_old=include_old)

Get audit logs for an account

Export the audit logs displayed in **Accounts > Audit logs**. 

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
application_id = 3.4 # float | Filter results by Application ID. (optional)
entity_path = 'entity_path_example' # str | Filter results on a case insensitive matching of the url path of the entity (optional)
user_id = 56 # int | Filter results that match the given user ID. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
with_total_result_size = True # bool | When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When `true`: `hasMore` is true when there is a next page. `totalResultSize` is always zero. - When `false`: `hasMore` is always false. `totalResultSize` contains the total number of results for this query.  (optional)
include_old = True # bool | When this flag is set to false, the state without the change will not be returned. The default value is true. (optional)

    try:
        # Get audit logs for an account
        api_response = api_instance.get_changes(page_size=page_size, skip=skip, sort=sort, application_id=application_id, entity_path=entity_path, user_id=user_id, created_before=created_before, created_after=created_after, with_total_result_size=with_total_result_size, include_old=include_old)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **entity_path** | **str**| Filter results on a case insensitive matching of the url path of the entity | [optional] 
 **user_id** | **int**| Filter results that match the given user ID. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **include_old** | **bool**| When this flag is set to false, the state without the change will not be returned. The default value is true. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 

### Return type

[**Collection**](Collection.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
> InlineResponse20010 get_collection_items(collection_id, page_size=page_size, skip=skip)

Get collection items

Retrieve the items from the given collection.

### Example

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
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
> InlineResponse2006 get_coupons_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match)

List coupons

List all the coupons matching the specified criteria. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string.
application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint. 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string. | 
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint.  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**CustomerActivityReport**](CustomerActivityReport.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_activity_reports_without_total_count**
> InlineResponse20018 get_customer_activity_reports_without_total_count(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)

Get Activity Reports for Application Customers

Fetch summary reports for all application customers based on a time range. Instead of having the total number of results in the response, this endpoint only mentions whether there are more results. 

### Example

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
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string.
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string.
application_id = 56 # int | The ID of the Application. It is displayed in your Talon.One deployment URL.
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string. | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string. | 
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **name** | **str**| Only return reports matching the customer name | [optional] 
 **integration_id** | **str**| Filter results performing an exact matching against the profile integration identifier. | [optional] 
 **campaign_name** | **str**| Only return reports matching the campaignName | [optional] 
 **advocate_name** | **str**| Only return reports matching the current customer referrer name | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint. 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint.  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**CustomerAnalytics**](CustomerAnalytics.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    customer_id = 56 # int | The value of the `id` property of a customer profile. Get it with the [List Application's customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint. 

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
 **customer_id** | **int**| The value of the &#x60;id&#x60; property of a customer profile. Get it with the [List Application&#39;s customers](/#tag/Customer-data/operation/getApplicationCustomers) endpoint.  | 

### Return type

[**CustomerProfile**](CustomerProfile.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_profiles**
> InlineResponse20017 get_customer_profiles(page_size=page_size, skip=skip)

List customer profiles

List all customer profiles.

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List customer profiles
        api_response = api_instance.get_customer_profiles(page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_by_attributes**
> InlineResponse20017 get_customers_by_attributes(body, page_size=page_size, skip=skip)

List customer profiles matching the given attributes

Get a list of the customer profiles matching the provided criteria.  The match is successful if all the attributes of the request are found in a profile, even if the profile has more attributes that are not present on the request. 

### Example

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
    body = talon_one.CustomerProfileSearchQuery() # CustomerProfileSearchQuery | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List customer profiles matching the given attributes
        api_response = api_instance.get_customers_by_attributes(body, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customers_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerProfileSearchQuery**](CustomerProfileSearchQuery.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_types**
> InlineResponse20029 get_event_types(name=name, include_old_versions=include_old_versions, page_size=page_size, skip=skip, sort=sort)

List event types

Fetch all event type definitions for your account. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exports**
> InlineResponse20032 get_exports(page_size=page_size, skip=skip, application_id=application_id, campaign_id=campaign_id, entity=entity)

Get exports

List all past exports 

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **campaign_id** | **int**| Filter by the campaign ID on which the limit counters are used. | [optional] 
 **entity** | **str**| The name of the entity type that was exported. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_points**
> LoyaltyLedger get_loyalty_points(loyalty_program_id, integration_id)

Get the Loyalty Ledger for this integrationID

Get the loyalty ledger for this profile integration ID.  To get the `integrationId` of the profile from a `sessionId`, use the [Update customer session](/integration-api/#operation/updateCustomerSessionV2). 

### Example

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
        # Get the Loyalty Ledger for this integrationID
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

[manager_auth](../README.md#manager_auth)

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
    loyalty_program_id = 56 # int | Identifier of the loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs endpoint](https://docs.talon.one/management-api/#operation/getLoyaltyPrograms). 

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
 **loyalty_program_id** | **int**| Identifier of the loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs endpoint](https://docs.talon.one/management-api/#operation/getLoyaltyPrograms).  | 

### Return type

[**LoyaltyProgram**](LoyaltyProgram.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_programs**
> InlineResponse2008 get_loyalty_programs()

List loyalty programs

List the loyalty programs of the account.

### Example

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

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Get loyalty program statistics by loyalty program ID

Retrieve the statistics of the specified loyalty program such as the total active points, pending points, spent points and expired points. 

### Example

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
    loyalty_program_id = 56 # int | Identifier of the loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs endpoint](https://docs.talon.one/management-api/#operation/getLoyaltyPrograms). 

    try:
        # Get loyalty program statistics by loyalty program ID
        api_response = api_instance.get_loyalty_statistics(loyalty_program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **int**| Identifier of the loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs endpoint](https://docs.talon.one/management-api/#operation/getLoyaltyPrograms).  | 

### Return type

[**LoyaltyStatistics**](LoyaltyStatistics.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Get notification webhook

Return the given outbound notification webhook.

### Example

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
notification_webhook_id = 56 # int | 

    try:
        # Get notification webhook
        api_response = api_instance.get_notification_webhook(application_id, notification_webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **notification_webhook_id** | **int**|  | 

### Return type

[**NotificationWebhook**](NotificationWebhook.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_webhooks**
> InlineResponse2003 get_notification_webhooks(application_id)

List notification webhooks

List all outbound notification webhooks for this application.

### Example

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
        # List notification webhooks
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

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_referrals_without_total_count**
> InlineResponse2007 get_referrals_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)

List referrals

List all referrals of the specified campaign.

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
code = 'code_example' # str | Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches referrals in which the expiry date is set and in the past. The second matches referrals in which start date is null or in the past and expiry date is null or in the future, the third matches referrals in which start date is set and in the future.  (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **code** | **str**| Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches referrals in which the expiry date is set and in the past. The second matches referrals in which start date is null or in the past and expiry date is null or in the future, the third matches referrals in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only referrals where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only referrals where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **advocate** | **str**| Filter results by match with a profile id specified in the referral&#39;s AdvocateProfileIntegrationId field | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

[manager_auth](../README.md#manager_auth)

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
ruleset_id = 56 # int | 

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
 **ruleset_id** | **int**|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rulesets**
> InlineResponse2004 get_rulesets(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort)

List campaign rulesets

List all rulesets of this campaign. A ruleset is a revision of the rules of a campaign. **Important:** The response also includes deleted rules. You should only consider the latest revision of the returned rulesets. 

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> InlineResponse20030 get_users(page_size=page_size, skip=skip, sort=sort)

List users in account

Retrieve all users in your account. 

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)

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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    webhook_id = 56 # int | 

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
 **webhook_id** | **int**|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_activation_logs**
> InlineResponse20027 get_webhook_activation_logs(page_size=page_size, skip=skip, sort=sort, integration_request_uuid=integration_request_uuid, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after)

List webhook activation log entries

Webhook activation log entries would be created as soon as an integration request triggered an effect with a webhook.

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **integration_request_uuid** | **str**| Filter results by integration request UUID. | [optional] 
 **webhook_id** | **float**| Filter results by Webhook. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_logs**
> InlineResponse20028 get_webhook_logs(page_size=page_size, skip=skip, sort=sort, status=status, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, request_uuid=request_uuid, created_before=created_before, created_after=created_after)

List webhook log entries

Retrieve all webhook log entries.

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **webhook_id** | **float**| Filter results by Webhook. | [optional] 
 **application_id** | **float**| Filter results by Application ID. | [optional] 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **request_uuid** | **str**| Filter results by request UUID. | [optional] 
 **created_before** | **datetime**| Filter results where request and response times to return entries before parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> InlineResponse20026 get_webhooks(application_ids=application_ids, sort=sort, page_size=page_size, skip=skip)

List webhooks

List all webhooks.

### Example

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
    application_ids = 'application_ids_example' # str | Filter by one or more application ids separated by comma. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
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
 **application_ids** | **str**| Filter by one or more application ids separated by comma. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).
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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Upload a CSV file containing a list of allowed values for the specified attribute. These values are also called [picklist values](/docs/product/account/dev-tools/managing-attributes/#picklist-values).  The file should be sent as multipart data.  The import **replaces** the previous list of allowed values for this attribute, if any.  The CSV file **must** only contain the following column: - `item` (required): the values in your allowed list, for example a list of SKU's.  An allowed list is limited to 500,000 items.  Example:  ```text item CS-VG-04032021-UP-50D-10 CS-DV-04042021-UP-49D-12 CS-DG-02082021-UP-50G-07 ``` 

### Example

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
    attribute_id = 56 # int | 
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
 **attribute_id** | **int**|  | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).
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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Upload a CSV file containing the coupons that should be created. The file should be sent as multipart data.  The CSV file can contain the following columns:  - `value` (required): The coupon code. - `expirydate`: The end date in RFC3339 of the code redemption period. - `startdate`: The start date in RFC3339 of the code redemption period. - `limitval`: The maximum amount of redemptions of this code. For unlimited redemptions, use `0`. Defaults to `1` when not provided. - `attributes`: A json object describing _custom_ referral attribute names and their values. Double the double-quotes in the object. - `discountlimit`: The amount of discounts that can be given with this coupon code.   For example, if you created a [custom attribute](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes)   called `category` associated to the coupon entity, set it with `\"{\"\"category\"\": \"\"10_off\"\"}\"`.  **Important:** Do not leave empty columns in the file.  You can use the timezone of your choice. It is converted to UTC internally by Talon.One.  **Example:**  ```text \"value\",\"expirydate\",\"startdate\",\"recipientintegrationid\",\"limitval\",\"attributes\",\"discountlimit\" COUP1,2018-07-01T04:00:00Z,2018-05-01T04:00:00Z,cust123,1,\"{\"\"Category\"\": \"\"10_off\"\"}\",2.4 ```  Once imported, you can find the `batchId` in the Campaign Manager or by using [List coupons](#tag/Coupons/operation/getCouponsWithoutTotalCount). 

### Example

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

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_loyalty_points**
> ModelImport import_loyalty_points(loyalty_program_id, up_file=up_file)

Import loyalty points

Upload a CSV file containing the [loyalty](https://www.talon.one/pillar-pages/loyalty) points that should be created. The file should be sent as multipart data.  **Important**: For existing customer profiles, the imported points are _added_ to their active points. Learn more about [Loyalty programs](https://docs.talon.one/docs/product/loyalty-programs/overview).  The CSV file can contain the following columns:  - `customerprofileid`: The integration ID of the customer profile that should receive the loyalty points. - `amount`: The amount of points to award to the customer profile. - `startdate`: The earliest date when the points can be redeemed. On this date and until the expiry date, the points are `active`. - `expirydate`: The latest date when the points can be redeemed. After this date, the points are `expired`. - `subledgerid` (optional): The ID of the subledger that should received the points. - `reason` (optional): A reason why these points were awarded.  **Important:** Do not leave empty columns in the file.  You can use the timezone of your choice. It is converted to UTC internally by Talon.One.  **Example:**  ```text customerprofileid,amount,startdate,expirydate,subledgerid,reason URNGV8294NV,100,2009-11-10T23:00:00Z,2009-11-11T23:00:00Z,subledger1,appeasement ``` 

### Example

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
    loyalty_program_id = 56 # int | Identifier of the loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs endpoint](https://docs.talon.one/management-api/#operation/getLoyaltyPrograms). 
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
 **loyalty_program_id** | **int**| Identifier of the loyalty program containing the loyalty card. You can get the ID with the [List loyalty programs endpoint](https://docs.talon.one/management-api/#operation/getLoyaltyPrograms).  | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Upload a CSV file containing the giveaway codes that should be created. Send the file as multipart data.  The CSV file can contain the following columns: - `code` (required): the code of your giveaway, for instance, a gift card redemption code. - `startdate`:  the start date in RFC3339 of the code redemption period. - `enddate`: the last date in RFC3339 of the code redemption period. - `attributes`: A json object describing _custom_ giveaway attribute names and their values. Double the double-quotes in the object.   For example, if you [created a custom attribute](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes)   called `provider` associated to the giveaway entity, set it with `\"{\"\"provider\"\": \"\"myPartnerCompany\"\"}\"`.  **Important:** Do not leave empty columns in the file.  The `startdate` and `enddate` have nothing to do with the _validity_ of the codes. They are only used by the Rule Engine to award the codes or not. You can use the timezone of your choice. It is converted to UTC internally by Talon.One.  **Example:**  ```text code,startdate,enddate,attributes GIVEAWAY1,2020-11-10T23:00:00Z,2022-11-11T23:00:00Z,\"{\"\"provider\"\": \"\"Amazon\"\"}\" GIVEAWAY2,2020-11-10T23:00:00Z,2022-11-11T23:00:00Z,\"{\"\"provider\"\": \"\"Amazon\"\"}\" GIVEAWAY3,2021-01-10T23:00:00Z,2022-11-11T23:00:00Z,\"{\"\"provider\"\": \"\"Aliexpress\"\"}\" ``` 

### Example

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
    pool_id = 56 # int | 
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
 **pool_id** | **int**|  | 
 **up_file** | **str**| The file with the information about the data that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Upload a CSV file containing the referrals that should be created. The file should be sent as multipart data.  The CSV file can contain the following columns:  - `code` (required): The referral code. - `advocateprofileintegrationid` (required): The profile ID of the advocate. - `startdate`: The start date in RFC3339 of the code redemption period. - `expirydate`: The end date in RFC3339 of the code redemption period. - `limitval`: The maximum amount of redemptions of this code. Defaults to `1` when left blank. - `attributes`: A json object describing _custom_ referral attribute names and their values. Double the double-quotes in the object.    For example, if you [created a custom attribute](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes)   called `category` associated to the referral entity, set it with `\"{\"\"category\"\": \"\"10_off\"\"}\"`.  You can use the timezone of your choice. It is converted to UTC internally by Talon.One.  **Example:**  ```text code,startdate,expirydate,advocateprofileintegrationid,limitval,attributes REFERRAL_CODE1,2020-11-10T23:00:00Z,2021-11-11T23:00:00Z,integid_4,1,\"{\"\"my_attribute\"\": \"\"10_off\"\"}\" REFERRAL_CODE2,2020-11-10T23:00:00Z,2021-11-11T23:00:00Z,integid1,1,\"{\"\"my_attribute\"\": \"\"20_off\"\"}\" ``` 

### Example

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

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_collections**
> InlineResponse2009 list_account_collections(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)

List collections in account

List collections in account.

### Example

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
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **name** | **str**| Filter by the name of the Collection. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
> InlineResponse20011 list_collections(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)

List collections

List collections in the campaign.

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **name** | **str**| Filter by the name of the Collection. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
> InlineResponse20011 list_collections_in_application(application_id, page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size, name=name)

List collections in application

List collections from all campaigns in the Application.

### Example

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
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result includes the total size of the result, across all pages. This might decrease performance on large data sets.  - When &#x60;true&#x60;: &#x60;hasMore&#x60; is true when there is a next page. &#x60;totalResultSize&#x60; is always zero. - When &#x60;false&#x60;: &#x60;hasMore&#x60; is always false. &#x60;totalResultSize&#x60; contains the total number of results for this query.  | [optional] 
 **name** | **str**| Filter by the name of the Collection. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_loyalty_points**
> remove_loyalty_points(loyalty_program_id, integration_id, body)

Deduct points in loyalty program for given customer

Remove points from the specified loyalty program and specified customer profile.  To get the `integrationId` of the profile from a `sessionId`, use the [Update customer session](/integration-api/#operation/updateCustomerSessionV2). 

### Example

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
body = talon_one.LoyaltyPoints() # LoyaltyPoints | 

    try:
        # Deduct points in loyalty program for given customer
        api_instance.remove_loyalty_points(loyalty_program_id, integration_id, body)
    except ApiException as e:
        print("Exception when calling ManagementApi->remove_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalty_program_id** | **str**| The identifier for the loyalty program. | 
 **integration_id** | **str**| The identifier of the profile. | 
 **body** | [**LoyaltyPoints**](LoyaltyPoints.md)|  | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    body = talon_one.NewPassword() # NewPassword | 

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
 **body** | [**NewPassword**](NewPassword.md)|  | 

### Return type

[**NewPassword**](NewPassword.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_coupons_advanced_application_wide_without_total_count**
> InlineResponse2006 search_coupons_advanced_application_wide_without_total_count(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)

List coupons that match the given attributes (without total count)

List the coupons whose attributes match the query criteria in all **active** campaigns of the given Application.  The match is successful if all the attributes of the request are found in a coupon, even if the coupon has more attributes that are not present on the request.  **Note:** The total count is not included in the response. 

### Example

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
body = None # object | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
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
 **body** | **object**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **campaign_state** | **str**| Filter results by the state of the campaign.  - &#x60;enabled&#x60;: Campaigns that are scheduled, running (activated), or expired. - &#x60;running&#x60;: Campaigns that are running (activated). - &#x60;disabled&#x60;: Campaigns that are disabled. - &#x60;expired&#x60;: Campaigns that are expired. - &#x60;archived&#x60;: Campaigns that are archived. - &#x60;draft&#x60;: Campaigns that are drafts.  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_coupons_advanced_without_total_count**
> InlineResponse2006 search_coupons_advanced_without_total_count(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)

List coupons that match the given attributes in campaign (without total count)

List the coupons whose attributes match the query criteria in the given campaign.  The match is successful if all the attributes of the request are found in a coupon, even if the coupon has more attributes that are not present on the request.  **Note:** The total count is not included in the response. 

### Example

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
body = None # object | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str | The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with `-` to sort in descending order. (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
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
 **body** | **object**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**| The field by which results should be sorted. Sorting defaults to ascending order, prefix the field name with &#x60;-&#x60; to sort in descending order. | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_collection**
> Collection update_account_collection(collection_id, body)

Update account-level collection

Edit the description of the account-level collection and enable or disable the collection in the specified Applications.

### Example

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
    collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).
body = talon_one.UpdateCollection() # UpdateCollection | 

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 
 **body** | [**UpdateCollection**](UpdateCollection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
    additional_cost_id = 56 # int | 
body = talon_one.NewAdditionalCost() # NewAdditionalCost | 

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
 **additional_cost_id** | **int**|  | 
 **body** | [**NewAdditionalCost**](NewAdditionalCost.md)|  | 

### Return type

[**AccountAdditionalCost**](AccountAdditionalCost.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Updates an existing custom attribute. Once created, the only property of a custom attribute that can be changed is the title (human readable description). This restriction is in place to prevent accidentally breaking live integrations. E.g. if you have a customer profile attribute with the name `region`, and your integration is sending `attributes.region` with customer profile updates, changing the name to `locale` would cause the integration requests to begin failing.  If you **really** need to change the `type` or `name` property of a custom attribute, create a new attribute and update any relevant integrations and rules to use the new attribute. Then delete the old attribute when you are confident you have migrated any needed data from the old attribute to the new one. 

### Example

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
    attribute_id = 56 # int | 
body = talon_one.NewAttribute() # NewAttribute | 

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
 **attribute_id** | **int**|  | 
 **body** | [**NewAttribute**](NewAttribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
body = talon_one.UpdateCampaign() # UpdateCampaign | 

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
 **body** | [**UpdateCampaign**](UpdateCampaign.md)|  | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
collection_id = 56 # int | The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication).
body = talon_one.UpdateCampaignCollection() # UpdateCampaignCollection | 

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
 **collection_id** | **int**| The ID of the collection. You can get it with the [List collection in account endpoint](#operation/listCollectionsInApplication). | 
 **body** | [**UpdateCampaignCollection**](UpdateCampaignCollection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Update the specified coupon.

### Example

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
coupon_id = 'coupon_id_example' # str | The ID of the coupon code to update
body = talon_one.UpdateCoupon() # UpdateCoupon | 

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
 **coupon_id** | **str**| The ID of the coupon code to update | 
 **body** | [**UpdateCoupon**](UpdateCoupon.md)|  | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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

Update all coupons of an campaign, or a specific batch of coupons. You can find the `batchId` in the **Coupons** view of your Application in the Campaign Manager or by using [List coupons](#operation/getCouponsWithoutTotalCount).  **Important**: - Only send sequential requests to this endpoint. - Requests to this endpoint timeout after 30 minutes. If you hit a timeout, reach out to our support team.  To update a specific coupon, use [Update coupon](#operation/updateCoupon). 

### Example

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
body = talon_one.UpdateCouponBatch() # UpdateCouponBatch | 

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
 **body** | [**UpdateCouponBatch**](UpdateCouponBatch.md)|  | 

### Return type

void (empty response body)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_webhook**
> NotificationWebhook update_notification_webhook(application_id, notification_webhook_id, body)

Update notification webhook

Update the given outbound notification webhook.

### Example

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
notification_webhook_id = 56 # int | 
body = talon_one.NewNotificationWebhook() # NewNotificationWebhook | 

    try:
        # Update notification webhook
        api_response = api_instance.update_notification_webhook(application_id, notification_webhook_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The ID of the Application. It is displayed in your Talon.One deployment URL. | 
 **notification_webhook_id** | **int**|  | 
 **body** | [**NewNotificationWebhook**](NewNotificationWebhook.md)|  | 

### Return type

[**NotificationWebhook**](NotificationWebhook.md)

### Authorization

[manager_auth](../README.md#manager_auth)

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
referral_id = 'referral_id_example' # str | The ID of the referral code to delete
body = talon_one.UpdateReferral() # UpdateReferral | 

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
 **referral_id** | **str**| The ID of the referral code to delete | 
 **body** | [**UpdateReferral**](UpdateReferral.md)|  | 

### Return type

[**Referral**](Referral.md)

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

