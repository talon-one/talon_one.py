# talon_one.ManagementApi

All URIs are relative to *http://your_domain.your_region.talon.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_loyalty_points**](ManagementApi.md#add_loyalty_points) | **PUT** /v1/loyalty_programs/{programID}/profile/{integrationID}/add_points | Add points in a loyalty program for the specified customer
[**copy_campaign_to_applications**](ManagementApi.md#copy_campaign_to_applications) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/copy | Copy the campaign into every specified application
[**create_additional_cost**](ManagementApi.md#create_additional_cost) | **POST** /v1/additional_costs | Define a new additional cost
[**create_attribute**](ManagementApi.md#create_attribute) | **POST** /v1/attributes | Define a new custom attribute
[**create_campaign**](ManagementApi.md#create_campaign) | **POST** /v1/applications/{applicationId}/campaigns | Create campaign
[**create_coupons**](ManagementApi.md#create_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Create coupons
[**create_coupons_for_multiple_recipients**](ManagementApi.md#create_coupons_for_multiple_recipients) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_with_recipients | Create coupons for multiple recipients
[**create_password_recovery_email**](ManagementApi.md#create_password_recovery_email) | **POST** /v1/password_recovery_emails | Request a password reset
[**create_ruleset**](ManagementApi.md#create_ruleset) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets | Create ruleset
[**create_session**](ManagementApi.md#create_session) | **POST** /v1/sessions | Create session
[**delete_campaign**](ManagementApi.md#delete_campaign) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId} | Delete campaign
[**delete_coupon**](ManagementApi.md#delete_coupon) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Delete coupon
[**delete_coupons**](ManagementApi.md#delete_coupons) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Delete coupons
[**delete_referral**](ManagementApi.md#delete_referral) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Delete referral
[**delete_ruleset**](ManagementApi.md#delete_ruleset) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Delete ruleset
[**export_coupons**](ManagementApi.md#export_coupons) | **GET** /v1/applications/{applicationId}/export_coupons | Export coupons to a CSV file
[**export_customer_sessions**](ManagementApi.md#export_customer_sessions) | **GET** /v1/applications/{applicationId}/export_customer_sessions | Export Customer Sessions to a CSV file
[**export_effects**](ManagementApi.md#export_effects) | **GET** /v1/applications/{applicationId}/export_effects | Export triggered Effects to a CSV file
[**export_loyalty_balance**](ManagementApi.md#export_loyalty_balance) | **GET** /v1/loyalty_programs/{programID}/export_customer_balance | Export customer loyalty balance to a CSV file
[**export_loyalty_ledger**](ManagementApi.md#export_loyalty_ledger) | **GET** /v1/loyalty_programs/{programID}/profile/{integrationID}/export_log | Export a customer&#39;s loyalty ledger log to a CSV file
[**get_access_logs**](ManagementApi.md#get_access_logs) | **GET** /v1/applications/{applicationId}/access_logs | Get access logs for application (with total count)
[**get_access_logs_without_total_count**](ManagementApi.md#get_access_logs_without_total_count) | **GET** /v1/applications/{applicationId}/access_logs/no_total | Get access logs for application
[**get_account**](ManagementApi.md#get_account) | **GET** /v1/accounts/{accountId} | Get Account Details
[**get_account_analytics**](ManagementApi.md#get_account_analytics) | **GET** /v1/accounts/{accountId}/analytics | Get Account Analytics
[**get_additional_cost**](ManagementApi.md#get_additional_cost) | **GET** /v1/additional_costs/{additionalCostId} | Get an additional cost
[**get_additional_costs**](ManagementApi.md#get_additional_costs) | **GET** /v1/additional_costs | List additional costs
[**get_all_access_logs**](ManagementApi.md#get_all_access_logs) | **GET** /v1/access_logs | List access logs
[**get_all_roles**](ManagementApi.md#get_all_roles) | **GET** /v1/roles | List roles
[**get_application**](ManagementApi.md#get_application) | **GET** /v1/applications/{applicationId} | Get Application
[**get_application_api_health**](ManagementApi.md#get_application_api_health) | **GET** /v1/applications/{applicationId}/health_report | Get report of health of application API
[**get_application_customer**](ManagementApi.md#get_application_customer) | **GET** /v1/applications/{applicationId}/customers/{customerId} | Get Application Customer
[**get_application_customers**](ManagementApi.md#get_application_customers) | **GET** /v1/applications/{applicationId}/customers | List Application Customers
[**get_application_customers_by_attributes**](ManagementApi.md#get_application_customers_by_attributes) | **POST** /v1/application_customer_search | Get a list of the customer profiles that match the given attributes (with total count)
[**get_application_event_types**](ManagementApi.md#get_application_event_types) | **GET** /v1/applications/{applicationId}/event_types | List Applications Event Types
[**get_application_events**](ManagementApi.md#get_application_events) | **GET** /v1/applications/{applicationId}/events | List Applications Events (with total count)
[**get_application_events_without_total_count**](ManagementApi.md#get_application_events_without_total_count) | **GET** /v1/applications/{applicationId}/events/no_total | List Applications Events
[**get_application_session**](ManagementApi.md#get_application_session) | **GET** /v1/applications/{applicationId}/sessions/{sessionId} | Get Application Session
[**get_application_sessions**](ManagementApi.md#get_application_sessions) | **GET** /v1/applications/{applicationId}/sessions | List Application Sessions
[**get_applications**](ManagementApi.md#get_applications) | **GET** /v1/applications | List Applications
[**get_attribute**](ManagementApi.md#get_attribute) | **GET** /v1/attributes/{attributeId} | Get a custom attribute
[**get_attributes**](ManagementApi.md#get_attributes) | **GET** /v1/attributes | List custom attributes
[**get_audiences**](ManagementApi.md#get_audiences) | **GET** /v1/audiences | List audiences
[**get_campaign**](ManagementApi.md#get_campaign) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId} | Get campaign
[**get_campaign_analytics**](ManagementApi.md#get_campaign_analytics) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/analytics | Get analytics of campaigns
[**get_campaign_by_attributes**](ManagementApi.md#get_campaign_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns_search | List campaigns that match the given attributes
[**get_campaigns**](ManagementApi.md#get_campaigns) | **GET** /v1/applications/{applicationId}/campaigns | List campaigns
[**get_changes**](ManagementApi.md#get_changes) | **GET** /v1/changes | Get audit log for an account
[**get_coupons**](ManagementApi.md#get_coupons) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | List coupons (with total count)
[**get_coupons_by_attributes**](ManagementApi.md#get_coupons_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search | List coupons that match the given attributes
[**get_coupons_by_attributes_application_wide**](ManagementApi.md#get_coupons_by_attributes_application_wide) | **POST** /v1/applications/{applicationId}/coupons_search | List coupons that match the given attributes in all active campaigns of an application (with total count)
[**get_coupons_without_total_count**](ManagementApi.md#get_coupons_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/no_total | List coupons
[**get_customer_activity_report**](ManagementApi.md#get_customer_activity_report) | **GET** /v1/applications/{applicationId}/customer_activity_reports/{customerId} | Get Activity Report for Single Customer
[**get_customer_activity_reports**](ManagementApi.md#get_customer_activity_reports) | **GET** /v1/applications/{applicationId}/customer_activity_reports | Get Activity Reports for Application Customers (with total count)
[**get_customer_activity_reports_without_total_count**](ManagementApi.md#get_customer_activity_reports_without_total_count) | **GET** /v1/applications/{applicationId}/customer_activity_reports/no_total | Get Activity Reports for Application Customers
[**get_customer_analytics**](ManagementApi.md#get_customer_analytics) | **GET** /v1/applications/{applicationId}/customers/{customerId}/analytics | Get Analytics Report for a Customer
[**get_customer_profile**](ManagementApi.md#get_customer_profile) | **GET** /v1/customers/{customerId} | Get Customer Profile
[**get_customer_profiles**](ManagementApi.md#get_customer_profiles) | **GET** /v1/customers/no_total | List Customer Profiles
[**get_customers_by_attributes**](ManagementApi.md#get_customers_by_attributes) | **POST** /v1/customer_search/no_total | List customer profiles that match the given attributes
[**get_event_types**](ManagementApi.md#get_event_types) | **GET** /v1/event_types | List event types
[**get_exports**](ManagementApi.md#get_exports) | **GET** /v1/exports | Get exports
[**get_loyalty_points**](ManagementApi.md#get_loyalty_points) | **GET** /v1/loyalty_programs/{programID}/profile/{integrationID} | Get integration&#39;s Loyalty Ledger
[**get_loyalty_program**](ManagementApi.md#get_loyalty_program) | **GET** /v1/loyalty_programs/{programID} | Get a loyalty program
[**get_loyalty_programs**](ManagementApi.md#get_loyalty_programs) | **GET** /v1/loyalty_programs | List loyalty programs
[**get_loyalty_statistics**](ManagementApi.md#get_loyalty_statistics) | **GET** /v1/loyalty_programs/{programID}/statistics | Get loyalty program statistics by loyalty program ID
[**get_referrals**](ManagementApi.md#get_referrals) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals | List referrals (with total count)
[**get_referrals_without_total_count**](ManagementApi.md#get_referrals_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/no_total | List referrals
[**get_role**](ManagementApi.md#get_role) | **GET** /v1/roles/{roleId} | Get information for the specified role
[**get_ruleset**](ManagementApi.md#get_ruleset) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Get ruleset
[**get_rulesets**](ManagementApi.md#get_rulesets) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets | List rulesets
[**get_user**](ManagementApi.md#get_user) | **GET** /v1/users/{userId} | Get a single User
[**get_users**](ManagementApi.md#get_users) | **GET** /v1/users | List users
[**get_webhook**](ManagementApi.md#get_webhook) | **GET** /v1/webhooks/{webhookId} | Get Webhook
[**get_webhook_activation_logs**](ManagementApi.md#get_webhook_activation_logs) | **GET** /v1/webhook_activation_logs | List Webhook activation Log Entries
[**get_webhook_logs**](ManagementApi.md#get_webhook_logs) | **GET** /v1/webhook_logs | List Webhook Log Entries
[**get_webhooks**](ManagementApi.md#get_webhooks) | **GET** /v1/webhooks | List Webhooks
[**import_coupons**](ManagementApi.md#import_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_coupons | Import coupons via CSV file
[**import_loyalty_points**](ManagementApi.md#import_loyalty_points) | **POST** /v1/loyalty_programs/{programID}/import_points | Import loyalty points via CSV file
[**import_pool_giveaways**](ManagementApi.md#import_pool_giveaways) | **POST** /v1/giveaways/pools/{poolId}/import | Import giveaways codes into a giveaways pool
[**import_referrals**](ManagementApi.md#import_referrals) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_referrals | Import referrals via CSV file
[**remove_loyalty_points**](ManagementApi.md#remove_loyalty_points) | **PUT** /v1/loyalty_programs/{programID}/profile/{integrationID}/deduct_points | Deduct points in a loyalty program for the specified customer
[**reset_password**](ManagementApi.md#reset_password) | **POST** /v1/reset_password | Reset password
[**search_coupons_advanced**](ManagementApi.md#search_coupons_advanced) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced | List coupons that match the given attributes (with total count)
[**search_coupons_advanced_application_wide**](ManagementApi.md#search_coupons_advanced_application_wide) | **POST** /v1/applications/{applicationId}/coupons_search_advanced | List coupons that match the given attributes in all active campaigns of an application (with total count)
[**search_coupons_advanced_application_wide_without_total_count**](ManagementApi.md#search_coupons_advanced_application_wide_without_total_count) | **POST** /v1/applications/{applicationId}/coupons_search_advanced/no_total | List coupons that match the given attributes in all active campaigns of an application
[**search_coupons_advanced_without_total_count**](ManagementApi.md#search_coupons_advanced_without_total_count) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced/no_total | List coupons that match the given attributes
[**update_additional_cost**](ManagementApi.md#update_additional_cost) | **PUT** /v1/additional_costs/{additionalCostId} | Update an additional cost
[**update_attribute**](ManagementApi.md#update_attribute) | **PUT** /v1/attributes/{attributeId} | Update a custom attribute
[**update_campaign**](ManagementApi.md#update_campaign) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId} | Update campaign
[**update_coupon**](ManagementApi.md#update_coupon) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Update coupon
[**update_coupon_batch**](ManagementApi.md#update_coupon_batch) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Update a batch of coupons
[**update_referral**](ManagementApi.md#update_referral) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Update referral
[**update_ruleset**](ManagementApi.md#update_ruleset) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Update ruleset


# **add_loyalty_points**
> add_loyalty_points(program_id, integration_id, loyalty_points)

Add points in a loyalty program for the specified customer

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.
integration_id = 'integration_id_example' # str | 
loyalty_points = talon_one.LoyaltyPoints() # LoyaltyPoints | 

    try:
        # Add points in a loyalty program for the specified customer
        api_instance.add_loyalty_points(program_id, integration_id, loyalty_points)
    except ApiException as e:
        print("Exception when calling ManagementApi->add_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 
 **integration_id** | **str**|  | 
 **loyalty_points** | [**LoyaltyPoints**](LoyaltyPoints.md)|  | 

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

# **copy_campaign_to_applications**
> InlineResponse2002 copy_campaign_to_applications(application_id, campaign_id, campaign_copy)

Copy the campaign into every specified application

Copy the campaign into every specified application.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
campaign_copy = talon_one.CampaignCopy() # CampaignCopy | 

    try:
        # Copy the campaign into every specified application
        api_response = api_instance.copy_campaign_to_applications(application_id, campaign_id, campaign_copy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->copy_campaign_to_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **campaign_copy** | [**CampaignCopy**](CampaignCopy.md)|  | 

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

# **create_additional_cost**
> AccountAdditionalCost create_additional_cost(new_additional_cost)

Define a new additional cost

Defines a new _additional cost_ in this account.  These additional costs are shared across all applications in your account, and are never required. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    new_additional_cost = talon_one.NewAdditionalCost() # NewAdditionalCost | 

    try:
        # Define a new additional cost
        api_response = api_instance.create_additional_cost(new_additional_cost)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_additional_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_additional_cost** | [**NewAdditionalCost**](NewAdditionalCost.md)|  | 

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
> Attribute create_attribute(new_attribute)

Define a new custom attribute

Defines a new _custom attribute_ in this account. Custom attributes allow you to attach new fields to Talon.One domain objects like campaigns, coupons, customers and so on. These attributes can then be given values when creating / updating these objects, and these values can be used in your campaign rules. For example, you could define a `zipCode` field for customer sessions, and add a rule to your campaign that only allows certain ZIP codes.  These attributes are shared across all applications in your account, and are never required. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    new_attribute = talon_one.NewAttribute() # NewAttribute | 

    try:
        # Define a new custom attribute
        api_response = api_instance.create_attribute(new_attribute)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_attribute** | [**NewAttribute**](NewAttribute.md)|  | 

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

# **create_campaign**
> Campaign create_campaign(application_id, new_campaign)

Create campaign

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
new_campaign = talon_one.NewCampaign() # NewCampaign | 

    try:
        # Create campaign
        api_response = api_instance.create_campaign(application_id, new_campaign)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **new_campaign** | [**NewCampaign**](NewCampaign.md)|  | 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons**
> InlineResponse2004 create_coupons(application_id, campaign_id, new_coupons, silent=silent)

Create coupons

Create coupons according to some pattern. Up to 20.000 coupons can be created without a unique prefix. When a unique prefix is provided, up to 200.000 coupons can be created.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
new_coupons = talon_one.NewCoupons() # NewCoupons | 
silent = 'silent_example' # str | If set to `yes`, response will be an empty 204, otherwise a list of integration states will be generated (up to 1000). (optional)

    try:
        # Create coupons
        api_response = api_instance.create_coupons(application_id, campaign_id, new_coupons, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **new_coupons** | [**NewCoupons**](NewCoupons.md)|  | 
 **silent** | **str**| If set to &#x60;yes&#x60;, response will be an empty 204, otherwise a list of integration states will be generated (up to 1000). | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **create_coupons_for_multiple_recipients**
> InlineResponse2004 create_coupons_for_multiple_recipients(application_id, campaign_id, new_coupons_for_multiple_recipients, silent=silent)

Create coupons for multiple recipients

Create coupons according to the specified pattern for up to 1000 recipients.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
new_coupons_for_multiple_recipients = talon_one.NewCouponsForMultipleRecipients() # NewCouponsForMultipleRecipients | 
silent = 'silent_example' # str | If set to `yes`, response will be an empty 204, otherwise a list of integration states will be generated (up to 1000). (optional)

    try:
        # Create coupons for multiple recipients
        api_response = api_instance.create_coupons_for_multiple_recipients(application_id, campaign_id, new_coupons_for_multiple_recipients, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_coupons_for_multiple_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **new_coupons_for_multiple_recipients** | [**NewCouponsForMultipleRecipients**](NewCouponsForMultipleRecipients.md)|  | 
 **silent** | **str**| If set to &#x60;yes&#x60;, response will be an empty 204, otherwise a list of integration states will be generated (up to 1000). | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **create_password_recovery_email**
> NewPasswordEmail create_password_recovery_email(new_password_email)

Request a password reset

Sends an email with a password recovery link to the email of an existing account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    new_password_email = talon_one.NewPasswordEmail() # NewPasswordEmail | 

    try:
        # Request a password reset
        api_response = api_instance.create_password_recovery_email(new_password_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_password_recovery_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_password_email** | [**NewPasswordEmail**](NewPasswordEmail.md)|  | 

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

# **create_ruleset**
> Ruleset create_ruleset(application_id, campaign_id, new_ruleset)

Create ruleset

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
new_ruleset = talon_one.NewRuleset() # NewRuleset | 

    try:
        # Create ruleset
        api_response = api_instance.create_ruleset(application_id, campaign_id, new_ruleset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **new_ruleset** | [**NewRuleset**](NewRuleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

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

# **create_session**
> Session create_session(login_params)

Create session

Create a session to use the other Management API endpoints. Use the `token` property of the response as bearer token.

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    login_params = talon_one.LoginParams() # LoginParams | 

    try:
        # Create session
        api_response = api_instance.create_session(login_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->create_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_params** | [**LoginParams**](LoginParams.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign**
> delete_campaign(application_id, campaign_id)

Delete campaign

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 

    try:
        # Delete campaign
        api_instance.delete_campaign(application_id, campaign_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 

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

# **delete_coupon**
> delete_coupon(application_id, campaign_id, coupon_id)

Delete coupon

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
coupon_id = 'coupon_id_example' # str | The ID of the coupon code to delete

    try:
        # Delete coupon
        api_instance.delete_coupon(application_id, campaign_id, coupon_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **coupon_id** | **str**| The ID of the coupon code to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **starts_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **starts_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **expires_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **expires_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
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

# **delete_referral**
> delete_referral(application_id, campaign_id, referral_id)

Delete referral

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
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

# **delete_ruleset**
> delete_ruleset(application_id, campaign_id, ruleset_id)

Delete ruleset

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
ruleset_id = 56 # int | 

    try:
        # Delete ruleset
        api_instance.delete_ruleset(application_id, campaign_id, ruleset_id)
    except ApiException as e:
        print("Exception when calling ManagementApi->delete_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **ruleset_id** | **int**|  | 

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

# **export_coupons**
> str export_coupons(application_id, campaign_id=campaign_id, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, date_format=date_format, campaign_state=campaign_state)

Export coupons to a CSV file

Download a file with the coupons that match the given attributes.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 3.4 # float | Filter results by campaign. (optional)
sort = 'sort_example' # str |  (optional)
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
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign. (optional)

    try:
        # Export coupons to a CSV file
        api_response = api_instance.export_coupons(application_id, campaign_id=campaign_id, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, date_format=date_format, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **sort** | **str**|  | [optional] 
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
 **campaign_state** | **str**| Filter results by the state of the campaign. | [optional] 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_customer_sessions**
> str export_customer_sessions(application_id, created_before=created_before, created_after=created_after, profile_integration_id=profile_integration_id, date_format=date_format, customer_session_state=customer_session_state)

Export Customer Sessions to a CSV file

Download a file with the customer sessions that match the request.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string. (optional)
profile_integration_id = 'profile_integration_id_example' # str | Only return sessions for the customer that matches this customer integration ID. (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)
customer_session_state = 'customer_session_state_example' # str | Filter results by state. (optional)

    try:
        # Export Customer Sessions to a CSV file
        api_response = api_instance.export_customer_sessions(application_id, created_before=created_before, created_after=created_after, profile_integration_id=profile_integration_id, date_format=date_format, customer_session_state=customer_session_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_customer_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
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
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_effects**
> str export_effects(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, date_format=date_format)

Export triggered Effects to a CSV file

Download a file with the triggered effects that match the given attributes.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export triggered Effects to a CSV file
        api_response = api_instance.export_effects(application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_effects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
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
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_balance**
> str export_loyalty_balance(program_id)

Export customer loyalty balance to a CSV file

Download a file with the balance of each customer in the loyalty program

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.

    try:
        # Export customer loyalty balance to a CSV file
        api_response = api_instance.export_loyalty_balance(program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_ledger**
> str export_loyalty_ledger(program_id, integration_id, range_start, range_end, date_format=date_format)

Export a customer's loyalty ledger log to a CSV file

Download a file with a customer's ledger log in the loyalty program

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.
integration_id = 'integration_id_example' # str | 
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
date_format = 'date_format_example' # str | Determines the format of dates in the export document. (optional)

    try:
        # Export a customer's loyalty ledger log to a CSV file
        api_response = api_instance.export_loyalty_ledger(program_id, integration_id, range_start, range_end, date_format=date_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->export_loyalty_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 
 **integration_id** | **str**|  | 
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **date_format** | **str**| Determines the format of dates in the export document. | [optional] 

### Return type

**str**

### Authorization

[manager_auth](../README.md#manager_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_logs**
> InlineResponse2008 get_access_logs(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

Get access logs for application (with total count)

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # Get access logs for application (with total count)
        api_response = api_instance.get_access_logs(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_access_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

# **get_access_logs_without_total_count**
> InlineResponse2009 get_access_logs_without_total_count(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

Get access logs for application

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # Get access logs for application
        api_response = api_instance.get_access_logs_without_total_count(application_id, range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_access_logs_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(account_id)

Get Account Details

Return the details of your companies Talon.One account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    account_id = 56 # int | 

    try:
        # Get Account Details
        api_response = api_instance.get_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

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

Get Account Analytics

Return the analytics of your companies Talon.One account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    account_id = 56 # int | 

    try:
        # Get Account Analytics
        api_response = api_instance.get_account_analytics(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_account_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

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

# **get_additional_cost**
> AccountAdditionalCost get_additional_cost(additional_cost_id)

Get an additional cost

Returns additional cost for the account by its id. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    additional_cost_id = 56 # int | 

    try:
        # Get an additional cost
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
> InlineResponse20021 get_additional_costs(page_size=page_size, skip=skip, sort=sort)

List additional costs

Returns all the defined additional costs for the account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

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
 **sort** | **str**|  | [optional] 

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

# **get_all_access_logs**
> InlineResponse2008 get_all_access_logs(range_start, range_end, path=path, method=method, status=status, page_size=page_size, skip=skip, sort=sort)

List access logs

Fetches the access logs for the entire account. Sensitive requests (logins) are _always_ filtered from the logs. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
path = 'path_example' # str | Only return results where the request path matches the given regular expression. (optional)
method = 'method_example' # str | Only return results where the request method matches the given regular expression. (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **path** | **str**| Only return results where the request path matches the given regular expression. | [optional] 
 **method** | **str**| Only return results where the request method matches the given regular expression. | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

# **get_all_roles**
> InlineResponse20029 get_all_roles()

List roles

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
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

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

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

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 

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
 **application_id** | **int**|  | 

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

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 

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
 **application_id** | **int**|  | 

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

Get Application Customer

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
customer_id = 56 # int | 

    try:
        # Get Application Customer
        api_response = api_instance.get_application_customer(application_id, customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **customer_id** | **int**|  | 

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

# **get_application_customers**
> InlineResponse20011 get_application_customers(application_id, integration_id=integration_id, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)

List Application Customers

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
integration_id = 'integration_id_example' # str | Filter results performing an exact matching against the profile integration identifier. (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
with_total_result_size = True # bool | When this flag is set, the result will include the total size of the result, across all pages. This might decrease performance on large data sets. With this flag set to true, hasMore will be be true whenever there is a next page. totalResultSize will always be zero. With this flag set to false, hasMore will always be set to false. totalResultSize will contain the total number of results for this query.  (optional)

    try:
        # List Application Customers
        api_response = api_instance.get_application_customers(application_id, integration_id=integration_id, page_size=page_size, skip=skip, with_total_result_size=with_total_result_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **integration_id** | **str**| Filter results performing an exact matching against the profile integration identifier. | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result will include the total size of the result, across all pages. This might decrease performance on large data sets. With this flag set to true, hasMore will be be true whenever there is a next page. totalResultSize will always be zero. With this flag set to false, hasMore will always be set to false. totalResultSize will contain the total number of results for this query.  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_customers_by_attributes**
> InlineResponse20012 get_application_customers_by_attributes(application_customer_search)

Get a list of the customer profiles that match the given attributes (with total count)

Gets a list of all the customer profiles for the account that exactly match a set of attributes.  The match is successful if all the attributes of the request are found in a profile, even if the profile has more attributes that are not present on the request.  [Customer Profile]: https://help.talon.one/hc/en-us/articles/360005130739-Data-Model#/customerProfile 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_customer_search = talon_one.ApplicationCustomerSearch() # ApplicationCustomerSearch | 

    try:
        # Get a list of the customer profiles that match the given attributes (with total count)
        api_response = api_instance.get_application_customers_by_attributes(application_customer_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_customers_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_customer_search** | [**ApplicationCustomerSearch**](ApplicationCustomerSearch.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

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
> InlineResponse20018 get_application_event_types(application_id, page_size=page_size, skip=skip, sort=sort)

List Applications Event Types

Get all of the distinct values of the Event `type` property for events recorded in the application.  See also: [Track an event](/integration-api/reference/#trackEvent) 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # List Applications Event Types
        api_response = api_instance.get_application_event_types(application_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_event_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

# **get_application_events**
> InlineResponse20016 get_application_events(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)

List Applications Events (with total count)

Lists all events recorded for an application. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
        # List Applications Events (with total count)
        api_response = api_instance.get_application_events(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
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

[**InlineResponse20016**](InlineResponse20016.md)

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
> InlineResponse20017 get_application_events_without_total_count(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)

List Applications Events

Lists all events recorded for an application. Instead of having the total number of results in the response, this endpoint only if there are more results. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
        # List Applications Events
        api_response = api_instance.get_application_events_without_total_count(application_id, page_size=page_size, skip=skip, sort=sort, type=type, created_before=created_before, created_after=created_after, session=session, profile=profile, customer_name=customer_name, customer_email=customer_email, coupon_code=coupon_code, referral_code=referral_code, rule_query=rule_query, campaign_query=campaign_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_events_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
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

# **get_application_session**
> ApplicationSession get_application_session(application_id, session_id)

Get Application Session

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
session_id = 56 # int | 

    try:
        # Get Application Session
        api_response = api_instance.get_application_session(application_id, session_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **session_id** | **int**|  | 

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
> InlineResponse20015 get_application_sessions(application_id, page_size=page_size, skip=skip, sort=sort, profile=profile, state=state, created_before=created_before, created_after=created_after, coupon=coupon, referral=referral, integration_id=integration_id)

List Application Sessions

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
profile = 'profile_example' # str | Profile integration ID filter for sessions. Must be exact match. (optional)
state = 'state_example' # str | Filter by sessions with this state. Must be exact match. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
coupon = 'coupon_example' # str | Filter by sessions with this coupon. Must be exact match. (optional)
referral = 'referral_example' # str | Filter by sessions with this referral. Must be exact match. (optional)
integration_id = 'integration_id_example' # str | Filter by sessions with this integrationId. Must be exact match. (optional)

    try:
        # List Application Sessions
        api_response = api_instance.get_application_sessions(application_id, page_size=page_size, skip=skip, sort=sort, profile=profile, state=state, created_before=created_before, created_after=created_after, coupon=coupon, referral=referral, integration_id=integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_application_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **profile** | **str**| Profile integration ID filter for sessions. Must be exact match. | [optional] 
 **state** | **str**| Filter by sessions with this state. Must be exact match. | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Only return events created after this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **coupon** | **str**| Filter by sessions with this coupon. Must be exact match. | [optional] 
 **referral** | **str**| Filter by sessions with this referral. Must be exact match. | [optional] 
 **integration_id** | **str**| Filter by sessions with this integrationId. Must be exact match. | [optional] 

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

# **get_applications**
> InlineResponse2001 get_applications(page_size=page_size, skip=skip, sort=sort)

List Applications

List all application in the current account.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

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
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

Get a custom attribute

Returns custom attribute for the account by its id. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | 

    try:
        # Get a custom attribute
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
> InlineResponse20020 get_attributes(page_size=page_size, skip=skip, sort=sort, entity=entity)

List custom attributes

Returns all the defined custom attributes for the account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
entity = 'entity_example' # str |  (optional)

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
 **sort** | **str**|  | [optional] 
 **entity** | **str**|  | [optional] 

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

# **get_audiences**
> InlineResponse20019 get_audiences(page_size=page_size, skip=skip, sort=sort, with_total_result_size=with_total_result_size)

List audiences

Get All audiences created in the account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
with_total_result_size = True # bool | When this flag is set, the result will include the total size of the result, across all pages. This might decrease performance on large data sets. With this flag set to true, hasMore will be be true whenever there is a next page. totalResultSize will always be zero. With this flag set to false, hasMore will always be set to false. totalResultSize will contain the total number of results for this query.  (optional)

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
 **sort** | **str**|  | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result will include the total size of the result, across all pages. This might decrease performance on large data sets. With this flag set to true, hasMore will be be true whenever there is a next page. totalResultSize will always be zero. With this flag set to false, hasMore will always be set to false. totalResultSize will contain the total number of results for this query.  | [optional] 

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

# **get_campaign**
> Campaign get_campaign(application_id, campaign_id)

Get campaign

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 

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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 

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
> InlineResponse20010 get_campaign_analytics(application_id, campaign_id, range_start, range_end, granularity=granularity)

Get analytics of campaigns

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **granularity** | **str**| The time interval between the results in the returned time-series. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_by_attributes**
> InlineResponse2002 get_campaign_by_attributes(application_id, campaign_search, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state)

List campaigns that match the given attributes

Gets a list of all the campaigns that exactly match a set of attributes. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_search = talon_one.CampaignSearch() # CampaignSearch | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign. (optional)

    try:
        # List campaigns that match the given attributes
        api_response = api_instance.get_campaign_by_attributes(application_id, campaign_search, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaign_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_search** | [**CampaignSearch**](CampaignSearch.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign. | [optional] 

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
> InlineResponse2002 get_campaigns(application_id, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state, name=name, tags=tags, created_before=created_before, created_after=created_after, campaign_group_id=campaign_group_id)

List campaigns

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign. (optional)
name = 'name_example' # str | Filter results performing case-insensitive matching against the name of the campaign. (optional)
tags = 'tags_example' # str | Filter results performing case-insensitive matching against the tags of the campaign. When used in conjunction with the \"name\" query parameter, a logical OR will be performed to search both tags and name for the provided values  (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
campaign_group_id = 56 # int | Filter results to campaigns owned by the specified campaign group ID. (optional)

    try:
        # List campaigns
        api_response = api_instance.get_campaigns(application_id, page_size=page_size, skip=skip, sort=sort, campaign_state=campaign_state, name=name, tags=tags, created_before=created_before, created_after=created_after, campaign_group_id=campaign_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **campaign_state** | **str**| Filter results by the state of the campaign. | [optional] 
 **name** | **str**| Filter results performing case-insensitive matching against the name of the campaign. | [optional] 
 **tags** | **str**| Filter results performing case-insensitive matching against the tags of the campaign. When used in conjunction with the \&quot;name\&quot; query parameter, a logical OR will be performed to search both tags and name for the provided values  | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the campaign creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **campaign_group_id** | **int**| Filter results to campaigns owned by the specified campaign group ID. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changes**
> InlineResponse20027 get_changes(page_size=page_size, skip=skip, sort=sort, application_id=application_id, entity_path=entity_path, user_id=user_id, created_before=created_before, created_after=created_after, with_total_result_size=with_total_result_size, include_old=include_old)

Get audit log for an account

Get list of changes caused by API calls for an account. Only accessible for admins.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
application_id = 56 # int |  (optional)
entity_path = 'entity_path_example' # str | Filter results on a case insensitive matching of the url path of the entity (optional)
user_id = 56 # int |  (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
with_total_result_size = True # bool | When this flag is set, the result will include the total size of the result, across all pages. This might decrease performance on large data sets. With this flag set to true, hasMore will be be true whenever there is a next page. totalResultSize will always be zero. With this flag set to false, hasMore will always be set to false. totalResultSize will contain the total number of results for this query.  (optional)
include_old = True # bool | When this flag is set to false, the state without the change will not be returned. The default value is true. (optional)

    try:
        # Get audit log for an account
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
 **sort** | **str**|  | [optional] 
 **application_id** | **int**|  | [optional] 
 **entity_path** | **str**| Filter results on a case insensitive matching of the url path of the entity | [optional] 
 **user_id** | **int**|  | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the change creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **with_total_result_size** | **bool**| When this flag is set, the result will include the total size of the result, across all pages. This might decrease performance on large data sets. With this flag set to true, hasMore will be be true whenever there is a next page. totalResultSize will always be zero. With this flag set to false, hasMore will always be set to false. totalResultSize will contain the total number of results for this query.  | [optional] 
 **include_old** | **bool**| When this flag is set to false, the state without the change will not be returned. The default value is true. | [optional] 

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

# **get_coupons**
> InlineResponse2004 get_coupons(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, starts_after=starts_after, starts_before=starts_before, expires_after=expires_after, expires_before=expires_before, valid=valid, batch_id=batch_id, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match)

List coupons (with total count)

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
starts_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
expires_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)

    try:
        # List coupons (with total count)
        api_response = api_instance.get_coupons(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, starts_after=starts_after, starts_before=starts_before, expires_after=expires_after, expires_before=expires_before, valid=valid, batch_id=batch_id, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **starts_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **starts_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **expires_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **expires_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]

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

# **get_coupons_by_attributes**
> InlineResponse2004 get_coupons_by_attributes(application_id, campaign_id, coupon_search, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)

List coupons that match the given attributes

Gets a list of all the coupons that exactly match a set of attributes.  The match is successful if all the attributes of the request are found in a coupon, even if the coupon has more attributes that are not present on the request. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
coupon_search = talon_one.CouponSearch() # CouponSearch | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
        # List coupons that match the given attributes
        api_response = api_instance.get_coupons_by_attributes(application_id, campaign_id, coupon_search, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_coupons_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **coupon_search** | [**CouponSearch**](CouponSearch.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
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

[**InlineResponse2004**](InlineResponse2004.md)

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

# **get_coupons_by_attributes_application_wide**
> InlineResponse2004 get_coupons_by_attributes_application_wide(application_id, coupon_search, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)

List coupons that match the given attributes in all active campaigns of an application (with total count)

Gets a list of all the coupons with attributes matching the query criteria Application wide 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
coupon_search = talon_one.CouponSearch() # CouponSearch | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign. (optional)

    try:
        # List coupons that match the given attributes in all active campaigns of an application (with total count)
        api_response = api_instance.get_coupons_by_attributes_application_wide(application_id, coupon_search, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_coupons_by_attributes_application_wide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **coupon_search** | [**CouponSearch**](CouponSearch.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **campaign_state** | **str**| Filter results by the state of the campaign. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **get_coupons_without_total_count**
> InlineResponse2005 get_coupons_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match)

List coupons

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
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

[**InlineResponse2005**](InlineResponse2005.md)

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

Get Activity Report for Single Customer

Fetch summary report for single application customer based on a time range

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
application_id = 56 # int | 
customer_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # Get Activity Report for Single Customer
        api_response = api_instance.get_customer_activity_report(range_start, range_end, application_id, customer_id, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_activity_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **application_id** | **int**|  | 
 **customer_id** | **int**|  | 
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

# **get_customer_activity_reports**
> InlineResponse20013 get_customer_activity_reports(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)

Get Activity Reports for Application Customers (with total count)

Fetch summary reports for all application customers based on a time range

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
name = 'name_example' # str | Only return reports matching the customer name (optional)
integration_id = 'integration_id_example' # str | Only return reports matching the integrationId (optional)
campaign_name = 'campaign_name_example' # str | Only return reports matching the campaignName (optional)
advocate_name = 'advocate_name_example' # str | Only return reports matching the current customer referrer name (optional)

    try:
        # Get Activity Reports for Application Customers (with total count)
        api_response = api_instance.get_customer_activity_reports(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_activity_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **name** | **str**| Only return reports matching the customer name | [optional] 
 **integration_id** | **str**| Only return reports matching the integrationId | [optional] 
 **campaign_name** | **str**| Only return reports matching the campaignName | [optional] 
 **advocate_name** | **str**| Only return reports matching the current customer referrer name | [optional] 

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

# **get_customer_activity_reports_without_total_count**
> InlineResponse20014 get_customer_activity_reports_without_total_count(range_start, range_end, application_id, page_size=page_size, skip=skip, sort=sort, name=name, integration_id=integration_id, campaign_name=campaign_name, advocate_name=advocate_name)

Get Activity Reports for Application Customers

Fetch summary reports for all application customers based on a time range. Instead of having the total number of results in the response, this endpoint only if there are more results.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    range_start = '2013-10-20T19:20:30+01:00' # datetime | Only return results from after this timestamp, must be an RFC3339 timestamp string
range_end = '2013-10-20T19:20:30+01:00' # datetime | Only return results from before this timestamp, must be an RFC3339 timestamp string
application_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
name = 'name_example' # str | Only return reports matching the customer name (optional)
integration_id = 'integration_id_example' # str | Only return reports matching the integrationId (optional)
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
 **range_start** | **datetime**| Only return results from after this timestamp, must be an RFC3339 timestamp string | 
 **range_end** | **datetime**| Only return results from before this timestamp, must be an RFC3339 timestamp string | 
 **application_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **name** | **str**| Only return reports matching the customer name | [optional] 
 **integration_id** | **str**| Only return reports matching the integrationId | [optional] 
 **campaign_name** | **str**| Only return reports matching the campaignName | [optional] 
 **advocate_name** | **str**| Only return reports matching the current customer referrer name | [optional] 

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

# **get_customer_analytics**
> CustomerAnalytics get_customer_analytics(application_id, customer_id, page_size=page_size, skip=skip, sort=sort)

Get Analytics Report for a Customer

Fetch analytics for single application customer

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
customer_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # Get Analytics Report for a Customer
        api_response = api_instance.get_customer_analytics(application_id, customer_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **customer_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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
> ApplicationCustomer get_customer_profile(customer_id)

Get Customer Profile

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    customer_id = 56 # int | 

    try:
        # Get Customer Profile
        api_response = api_instance.get_customer_profile(customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

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

# **get_customer_profiles**
> InlineResponse20012 get_customer_profiles(page_size=page_size, skip=skip)

List Customer Profiles

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List Customer Profiles
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

# **get_customers_by_attributes**
> InlineResponse20012 get_customers_by_attributes(application_customer_search, page_size=page_size, skip=skip)

List customer profiles that match the given attributes

Get a list of all the customer profiles for the account that exactly match a set of attributes.  The match is successful if all the attributes of the request are found in a profile, even if the profile has more attributes that are not present on the request.  [Customer Profile]: https://help.talon.one/hc/en-us/articles/360005130739-Data-Model#/customerProfile 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_customer_search = talon_one.ApplicationCustomerSearch() # ApplicationCustomerSearch | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List customer profiles that match the given attributes
        api_response = api_instance.get_customers_by_attributes(application_customer_search, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_customers_by_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_customer_search** | [**ApplicationCustomerSearch**](ApplicationCustomerSearch.md)|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

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
> InlineResponse20025 get_event_types(application_ids=application_ids, name=name, include_old_versions=include_old_versions, page_size=page_size, skip=skip, sort=sort)

List event types

Fetch all event type definitions for your account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_ids = 'application_ids_example' # str | Filter by one or more application ids separated by comma (optional)
name = 'name_example' # str | Filter results to event types with the given name. This parameter implies `includeOldVersions`. (optional)
include_old_versions = False # bool | Include all versions of every event type. (optional) (default to False)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # List event types
        api_response = api_instance.get_event_types(application_ids=application_ids, name=name, include_old_versions=include_old_versions, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_event_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_ids** | **str**| Filter by one or more application ids separated by comma | [optional] 
 **name** | **str**| Filter results to event types with the given name. This parameter implies &#x60;includeOldVersions&#x60;. | [optional] 
 **include_old_versions** | **bool**| Include all versions of every event type. | [optional] [default to False]
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

# **get_exports**
> InlineResponse20028 get_exports(page_size=page_size, skip=skip, application_id=application_id, campaign_id=campaign_id, entity=entity)

Get exports

Get a list of all past exports 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
application_id = 56 # int |  (optional)
campaign_id = 56 # int |  (optional)
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
 **application_id** | **int**|  | [optional] 
 **campaign_id** | **int**|  | [optional] 
 **entity** | **str**| The name of the entity type that was exported. | [optional] 

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

# **get_loyalty_points**
> LoyaltyLedger get_loyalty_points(program_id, integration_id)

Get integration's Loyalty Ledger

Get the Loyalty Ledger for this profile integration ID.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.
integration_id = 'integration_id_example' # str | The identifier for the application, must be unique within the account.

    try:
        # Get integration's Loyalty Ledger
        api_response = api_instance.get_loyalty_points(program_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 
 **integration_id** | **str**| The identifier for the application, must be unique within the account. | 

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
> LoyaltyProgram get_loyalty_program(program_id)

Get a loyalty program

Get a loyalty program.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.

    try:
        # Get a loyalty program
        api_response = api_instance.get_loyalty_program(program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 

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
> InlineResponse2007 get_loyalty_programs()

List loyalty programs

List all the loyalty programs.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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

# **get_loyalty_statistics**
> LoyaltyStatistics get_loyalty_statistics(program_id)

Get loyalty program statistics by loyalty program ID

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.

    try:
        # Get loyalty program statistics by loyalty program ID
        api_response = api_instance.get_loyalty_statistics(program_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_loyalty_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 

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

# **get_referrals**
> InlineResponse201 get_referrals(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)

List referrals (with total count)

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
code = 'code_example' # str | Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches referrals in which the expiry date is set and in the past. The second matches referrals in which start date is null or in the past and expiry date is null or in the future, the third matches referrals in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only referrals where `usageCounter < usageLimit` will be returned, \"false\" will return only referrals where `usageCounter >= usageLimit`.  (optional)
advocate = 'advocate_example' # str | Filter results by match with a profile id specified in the referral's AdvocateProfileIntegrationId field (optional)

    try:
        # List referrals (with total count)
        api_response = api_instance.get_referrals(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_referrals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **code** | **str**| Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches referrals in which the expiry date is set and in the past. The second matches referrals in which start date is null or in the past and expiry date is null or in the future, the third matches referrals in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only referrals where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only referrals where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **advocate** | **str**| Filter results by match with a profile id specified in the referral&#39;s AdvocateProfileIntegrationId field | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

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
> InlineResponse2006 get_referrals_without_total_count(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort, code=code, created_before=created_before, created_after=created_after, valid=valid, usable=usable, advocate=advocate)

List referrals

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **code** | **str**| Filter results performing case-insensitive matching against the referral code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the referral creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches referrals in which the expiry date is set and in the past. The second matches referrals in which start date is null or in the past and expiry date is null or in the future, the third matches referrals in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only referrals where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only referrals where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **advocate** | **str**| Filter results by match with a profile id specified in the referral&#39;s AdvocateProfileIntegrationId field | [optional] 

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

# **get_role**
> Role get_role(role_id)

Get information for the specified role

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    role_id = 56 # int | 

    try:
        # Get information for the specified role
        api_response = api_instance.get_role(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**|  | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

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

Retrieve the details of a ruleset.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
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
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
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
> InlineResponse2003 get_rulesets(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort)

List rulesets

List all rulesets in the given campaign.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # List rulesets
        api_response = api_instance.get_rulesets(application_id, campaign_id, page_size=page_size, skip=skip, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 

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

# **get_user**
> User get_user(user_id)

Get a single User

Retrieves the data (including an invitation code) for a user. Non-admin users can only get themselves. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    user_id = 56 # int | 

    try:
        # Get a single User
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

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
> InlineResponse20026 get_users(page_size=page_size, skip=skip, sort=sort)

List users

Retrieve all users in your account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # List users
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
 **sort** | **str**|  | [optional] 

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

# **get_webhook**
> Webhook get_webhook(webhook_id)

Get Webhook

Returns an webhook by its id.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    webhook_id = 56 # int | 

    try:
        # Get Webhook
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
> InlineResponse20023 get_webhook_activation_logs(page_size=page_size, skip=skip, sort=sort, integration_request_uuid=integration_request_uuid, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, created_before=created_before, created_after=created_after)

List Webhook activation Log Entries

Webhook activation log entries would be created as soon as an integration request triggered an effect with a webhook

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
integration_request_uuid = 'integration_request_uuid_example' # str | Filter results by integration request UUID. (optional)
webhook_id = 3.4 # float | Filter results by Webhook. (optional)
application_id = 3.4 # float |  (optional)
campaign_id = 3.4 # float | Filter results by campaign. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)

    try:
        # List Webhook activation Log Entries
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
 **sort** | **str**|  | [optional] 
 **integration_request_uuid** | **str**| Filter results by integration request UUID. | [optional] 
 **webhook_id** | **float**| Filter results by Webhook. | [optional] 
 **application_id** | **float**|  | [optional] 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **created_before** | **datetime**| Only return events created before this date. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 

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

# **get_webhook_logs**
> InlineResponse20024 get_webhook_logs(page_size=page_size, skip=skip, sort=sort, status=status, webhook_id=webhook_id, application_id=application_id, campaign_id=campaign_id, request_uuid=request_uuid, created_before=created_before, created_after=created_after)

List Webhook Log Entries

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
status = 'status_example' # str | Filter results by HTTP status codes. (optional)
webhook_id = 3.4 # float | Filter results by Webhook. (optional)
application_id = 3.4 # float |  (optional)
campaign_id = 3.4 # float | Filter results by campaign. (optional)
request_uuid = 'request_uuid_example' # str | Filter results by request UUID. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries before parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. (optional)

    try:
        # List Webhook Log Entries
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
 **sort** | **str**|  | [optional] 
 **status** | **str**| Filter results by HTTP status codes. | [optional] 
 **webhook_id** | **float**| Filter results by Webhook. | [optional] 
 **application_id** | **float**|  | [optional] 
 **campaign_id** | **float**| Filter results by campaign. | [optional] 
 **request_uuid** | **str**| Filter results by request UUID. | [optional] 
 **created_before** | **datetime**| Filter results where request and response times to return entries before parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results where request and response times to return entries after parameter value, expected to be an RFC3339 timestamp string. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 

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

# **get_webhooks**
> InlineResponse20022 get_webhooks(application_ids=application_ids, sort=sort, page_size=page_size, skip=skip)

List Webhooks

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_ids = 'application_ids_example' # str | Filter by one or more application ids separated by comma (optional)
sort = 'sort_example' # str |  (optional)
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)

    try:
        # List Webhooks
        api_response = api_instance.get_webhooks(application_ids=application_ids, sort=sort, page_size=page_size, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_ids** | **str**| Filter by one or more application ids separated by comma | [optional] 
 **sort** | **str**|  | [optional] 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 

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

# **import_coupons**
> ModelImport import_coupons(application_id, campaign_id, upfile=upfile)

Import coupons via CSV file

Upload a CSV file containing the coupons that should be created. The file should be sent as multipart data.

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
upfile = 'upfile_example' # str | The file with the information about the loyalty points that should be imported. (optional)

    try:
        # Import coupons via CSV file
        api_response = api_instance.import_coupons(application_id, campaign_id, upfile=upfile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **upfile** | **str**| The file with the information about the loyalty points that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_loyalty_points**
> ModelImport import_loyalty_points(program_id, up_file=up_file)

Import loyalty points via CSV file

Upload a CSV file containing the loyalty points that should be created. The file should be sent as multipart data.

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.
up_file = 'up_file_example' # str | The file with the information about the loyalty points that should be imported. (optional)

    try:
        # Import loyalty points via CSV file
        api_response = api_instance.import_loyalty_points(program_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 
 **up_file** | **str**| The file with the information about the loyalty points that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_pool_giveaways**
> ModelImport import_pool_giveaways(pool_id, upfile=upfile)

Import giveaways codes into a giveaways pool

Upload a CSV file containing the giveaways codes that should be created. Send the file as multipart data.  The CSV file can contain the following columns: - `code` (required): the code of your giveaway, for instance, a gift card redemption code. - `startdate`:  the start date in RFC3339 of the code redemption period. - `enddate`: the last date in RFC3339 of the code redemption period. - `attributes`: A json object describing _custom_ giveaways attribute names and their values. Double the double-quotes in the object.   For example, if you created a custom attribute called `provider`, set it with `\"{\"\"provider\"\": \"\"myPartnerCompany\"\"}\"`.  The `startdate` and `enddate` have nothing to do with the _validity_ of the codes. They are only used by the Rule Engine to award the codes or not. You can use the timezone of your choice. It is converted to UTC internally by Talon.One. 

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    pool_id = 56 # int | 
upfile = 'upfile_example' # str | The file with the information about the loyalty points that should be imported. (optional)

    try:
        # Import giveaways codes into a giveaways pool
        api_response = api_instance.import_pool_giveaways(pool_id, upfile=upfile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_pool_giveaways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**|  | 
 **upfile** | **str**| The file with the information about the loyalty points that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

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

Import referrals via CSV file

Upload a CSV file containing the referrals that should be created. The file should be sent as multipart data.  The CSV file can contain the following colums:  - `code` (required): the referral code. - `advocateprofileintegrationid` (required): The profile ID of the advocate. - `startdate`: the start date in RFC3339 of the code redemption period. - `expirydate`: the end date in RFC3339 of the code redemption period. - `limitval`: The maximum amount of redemptions of this code. Unlimited (0) when blank. - `attributes`: A json object describing _custom_ referral attribute names and their values. Double the double-quotes in the object.   For example, if you created a custom attribute called `category`, set it with `\"{\"\"category\"\": \"\"10_off\"\"}\"`.  You can use the timezone of your choice. It is converted to UTC internally by Talon.One. 

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
up_file = 'up_file_example' # str | The file with the information about the loyalty points that should be imported. (optional)

    try:
        # Import referrals via CSV file
        api_response = api_instance.import_referrals(application_id, campaign_id, up_file=up_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->import_referrals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **up_file** | **str**| The file with the information about the loyalty points that should be imported. | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_loyalty_points**
> remove_loyalty_points(program_id, integration_id, loyalty_points)

Deduct points in a loyalty program for the specified customer

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    program_id = 56 # int | The identifier for the loyalty program, must be unique within the account.
integration_id = 'integration_id_example' # str | 
loyalty_points = talon_one.LoyaltyPoints() # LoyaltyPoints | 

    try:
        # Deduct points in a loyalty program for the specified customer
        api_instance.remove_loyalty_points(program_id, integration_id, loyalty_points)
    except ApiException as e:
        print("Exception when calling ManagementApi->remove_loyalty_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **int**| The identifier for the loyalty program, must be unique within the account. | 
 **integration_id** | **str**|  | 
 **loyalty_points** | [**LoyaltyPoints**](LoyaltyPoints.md)|  | 

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

# **reset_password**
> NewPassword reset_password(new_password)

Reset password

Consumes the supplied password reset token and updates the password for the associated account. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    new_password = talon_one.NewPassword() # NewPassword | 

    try:
        # Reset password
        api_response = api_instance.reset_password(new_password)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_password** | [**NewPassword**](NewPassword.md)|  | 

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

# **search_coupons_advanced**
> InlineResponse2004 search_coupons_advanced(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)

List coupons that match the given attributes (with total count)

Gets a list of all the coupons with attributes matching the query criteria 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
body = None # object | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
        # List coupons that match the given attributes (with total count)
        api_response = api_instance.search_coupons_advanced(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **body** | **object**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
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

[**InlineResponse2004**](InlineResponse2004.md)

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

# **search_coupons_advanced_application_wide**
> InlineResponse2004 search_coupons_advanced_application_wide(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)

List coupons that match the given attributes in all active campaigns of an application (with total count)

Get a list of all the coupons with attributes matching the query criteria in all active campaigns of an application 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
body = None # object | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign. (optional)

    try:
        # List coupons that match the given attributes in all active campaigns of an application (with total count)
        api_response = api_instance.search_coupons_advanced_application_wide(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_application_wide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **body** | **object**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **campaign_state** | **str**| Filter results by the state of the campaign. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **search_coupons_advanced_application_wide_without_total_count**
> InlineResponse2005 search_coupons_advanced_application_wide_without_total_count(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)

List coupons that match the given attributes in all active campaigns of an application

List of all the coupons with attributes matching the query criteria in all active campaigns of an application. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
body = None # object | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
value = 'value_example' # str | Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. (optional)
valid = 'valid_example' # str | Either \"expired\", \"validNow\", or \"validFuture\". The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  (optional)
usable = 'usable_example' # str | Either \"true\" or \"false\". If \"true\", only coupons where `usageCounter < usageLimit` will be returned, \"false\" will return only coupons where `usageCounter >= usageLimit`.  (optional)
referral_id = 56 # int | Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. (optional)
recipient_integration_id = 'recipient_integration_id_example' # str | Filter results by match with a profile id specified in the coupon's RecipientIntegrationId field (optional)
batch_id = 'batch_id_example' # str | Filter results by batches of coupons (optional)
exact_match = False # bool | Filter results to an exact case-insensitive matching against the coupon code (optional) (default to False)
campaign_state = 'campaign_state_example' # str | Filter results by the state of the campaign. (optional)

    try:
        # List coupons that match the given attributes in all active campaigns of an application
        api_response = api_instance.search_coupons_advanced_application_wide_without_total_count(application_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, batch_id=batch_id, exact_match=exact_match, campaign_state=campaign_state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_application_wide_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **body** | **object**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
 **value** | **str**| Filter results performing case-insensitive matching against the coupon code. Both the code and the query are folded to remove all non-alpha-numeric characters. | [optional] 
 **created_before** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **created_after** | **datetime**| Filter results comparing the parameter value, expected to be an RFC3339 timestamp string, to the coupon creation timestamp. You can use any timezone. Talon.One will convert to UTC internally. | [optional] 
 **valid** | **str**| Either \&quot;expired\&quot;, \&quot;validNow\&quot;, or \&quot;validFuture\&quot;. The first option matches coupons in which the expiry date is set and in the past. The second matches coupons in which start date is null or in the past and expiry date is null or in the future, the third matches coupons in which start date is set and in the future.  | [optional] 
 **usable** | **str**| Either \&quot;true\&quot; or \&quot;false\&quot;. If \&quot;true\&quot;, only coupons where &#x60;usageCounter &lt; usageLimit&#x60; will be returned, \&quot;false\&quot; will return only coupons where &#x60;usageCounter &gt;&#x3D; usageLimit&#x60;.  | [optional] 
 **referral_id** | **int**| Filter the results by matching them with the Id of a referral, that meaning the coupons that had been created as an effect of the usage of a referral code. | [optional] 
 **recipient_integration_id** | **str**| Filter results by match with a profile id specified in the coupon&#39;s RecipientIntegrationId field | [optional] 
 **batch_id** | **str**| Filter results by batches of coupons | [optional] 
 **exact_match** | **bool**| Filter results to an exact case-insensitive matching against the coupon code | [optional] [default to False]
 **campaign_state** | **str**| Filter results by the state of the campaign. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_coupons_advanced_without_total_count**
> InlineResponse2005 search_coupons_advanced_without_total_count(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)

List coupons that match the given attributes

List of all the coupons with attributes matching the query criteria. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
body = None # object | 
page_size = 56 # int | The number of items to include in this response. When omitted, the maximum value of 1000 will be used. (optional)
skip = 56 # int | Skips the given number of items when paging through large result sets. (optional)
sort = 'sort_example' # str |  (optional)
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
        # List coupons that match the given attributes
        api_response = api_instance.search_coupons_advanced_without_total_count(application_id, campaign_id, body, page_size=page_size, skip=skip, sort=sort, value=value, created_before=created_before, created_after=created_after, valid=valid, usable=usable, referral_id=referral_id, recipient_integration_id=recipient_integration_id, exact_match=exact_match, batch_id=batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->search_coupons_advanced_without_total_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **body** | **object**|  | 
 **page_size** | **int**| The number of items to include in this response. When omitted, the maximum value of 1000 will be used. | [optional] 
 **skip** | **int**| Skips the given number of items when paging through large result sets. | [optional] 
 **sort** | **str**|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_additional_cost**
> AccountAdditionalCost update_additional_cost(additional_cost_id, new_additional_cost)

Update an additional cost

Updates an existing additional cost. Once created, the only property of an additional cost that can be changed is the title (human readable description). This restriction is in place to prevent accidentally breaking live integrations. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    additional_cost_id = 56 # int | 
new_additional_cost = talon_one.NewAdditionalCost() # NewAdditionalCost | 

    try:
        # Update an additional cost
        api_response = api_instance.update_additional_cost(additional_cost_id, new_additional_cost)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_additional_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_cost_id** | **int**|  | 
 **new_additional_cost** | [**NewAdditionalCost**](NewAdditionalCost.md)|  | 

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
> Attribute update_attribute(attribute_id, new_attribute)

Update a custom attribute

Updates an existing custom attribute. Once created, the only property of a custom attribute that can be changed is the title (human readable description). This restriction is in place to prevent accidentally breaking live integrations. E.g. if you have a customer profile attribute with the name `region`, and your integration is sending `attributes.region` with customer profile updates, changing the name to `locale` would cause the integration requests to begin failing.  If you **really** need to change the `type` or `name` property of a custom attribute, create a new attribute and update any relevant integrations and rules to use the new attribute. Then delete the old attribute when you are confident you have migrated any needed data from the old attribute to the new one. 

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    attribute_id = 56 # int | 
new_attribute = talon_one.NewAttribute() # NewAttribute | 

    try:
        # Update a custom attribute
        api_response = api_instance.update_attribute(attribute_id, new_attribute)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **int**|  | 
 **new_attribute** | [**NewAttribute**](NewAttribute.md)|  | 

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
> Campaign update_campaign(application_id, campaign_id, update_campaign)

Update campaign

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
update_campaign = talon_one.UpdateCampaign() # UpdateCampaign | 

    try:
        # Update campaign
        api_response = api_instance.update_campaign(application_id, campaign_id, update_campaign)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **update_campaign** | [**UpdateCampaign**](UpdateCampaign.md)|  | 

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

# **update_coupon**
> Coupon update_coupon(application_id, campaign_id, coupon_id, update_coupon)

Update coupon

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
coupon_id = 'coupon_id_example' # str | The ID of the coupon code to update
update_coupon = talon_one.UpdateCoupon() # UpdateCoupon | 

    try:
        # Update coupon
        api_response = api_instance.update_coupon(application_id, campaign_id, coupon_id, update_coupon)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **coupon_id** | **str**| The ID of the coupon code to update | 
 **update_coupon** | [**UpdateCoupon**](UpdateCoupon.md)|  | 

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
> update_coupon_batch(application_id, campaign_id, update_coupon_batch)

Update a batch of coupons

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
update_coupon_batch = talon_one.UpdateCouponBatch() # UpdateCouponBatch | 

    try:
        # Update a batch of coupons
        api_instance.update_coupon_batch(application_id, campaign_id, update_coupon_batch)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_coupon_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **update_coupon_batch** | [**UpdateCouponBatch**](UpdateCouponBatch.md)|  | 

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

# **update_referral**
> Referral update_referral(application_id, campaign_id, referral_id, update_referral)

Update referral

### Example

```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)


# Enter a context with an instance of the API client
with talon_one.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
referral_id = 'referral_id_example' # str | The ID of the referral code to delete
update_referral = talon_one.UpdateReferral() # UpdateReferral | 

    try:
        # Update referral
        api_response = api_instance.update_referral(application_id, campaign_id, referral_id, update_referral)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_referral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **referral_id** | **str**| The ID of the referral code to delete | 
 **update_referral** | [**UpdateReferral**](UpdateReferral.md)|  | 

### Return type

[**Referral**](Referral.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ruleset**
> Ruleset update_ruleset(application_id, campaign_id, ruleset_id, new_ruleset)

Update ruleset

Update the specified ruleset.

### Example

* Bearer Authentication (manager_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://your_domain.your_region.talon.one
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://your_domain.your_region.talon.one"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: manager_auth
configuration = talon_one.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.ManagementApi(api_client)
    application_id = 56 # int | 
campaign_id = 56 # int | 
ruleset_id = 56 # int | 
new_ruleset = talon_one.NewRuleset() # NewRuleset | 

    try:
        # Update ruleset
        api_response = api_instance.update_ruleset(application_id, campaign_id, ruleset_id, new_ruleset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManagementApi->update_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **ruleset_id** | **int**|  | 
 **new_ruleset** | [**NewRuleset**](NewRuleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

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

