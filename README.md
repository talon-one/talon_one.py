# talon_one
The Talon.One API is used to manage applications and campaigns, as well as to
integrate with your application. The operations in the _Integration API_ section
are used to integrate with our platform, while the other operations are
used to manage applications and campaigns.

### Where is the API?

The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`

[updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 3.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/talon-one/talon_one.py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/talon-one/talon_one.py.git`)

Then import the package:
```python
import talon_one
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import talon_one
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

### Integration API

```python
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Create configuration with your host destination
configuration = talon_one.Configuration()
configuration.host = 'https://mycompany.talon.one'

# Configure API key authorization: api_key_v1
configuration.api_key['Authorization'] = 'e18149e88f42247f0123456789abcdef9302722577ad60cebc86c4333b6fb70'
configuration.api_key_prefix['Authorization'] = 'ApiKey-v1'

# Integration API example to send a session update
integration_api = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
customer_session = talon_one.NewCustomerSession(
  'DEADDYBEEF', # profile_id
  '', # coupon
  '996732pucn', # referral
  'open', # state
  None, # cart_items
  None, # identifiers
  123.45, # total
  None # attributes
)

try:
    # Create/update a customer session using `update_customer_session` function
    api_response = integration_api.update_customer_session('my_unique_session_id', customer_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_customer_session: %s\n" % e)
```

### Management API

```python
# Create configuration with your host destination
configuration = talon_one.Configuration()
configuration.host = 'https://mycompany.talon.one'

# Management API example to load application with id 7
management_api = talon_one.ManagementApi(talon_one.ApiClient(configuration))

try:
    # Acquire session token
    login_params = talon_one.LoginParams('admin@talon.one', 'Password!@@')
    session = management_api.create_session(login_params)

    # Save token in the configuration for future management API calls
    configuration.api_key['Authorization'] = session.token
    configuration.api_key_prefix['Authorization'] = 'Bearer'

    # Calling get_application function with the desired id (7)
    application = management_api.get_application(7)
    pprint(application)
except ApiException as e:
    print("Exception when calling ManagementApi: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IntegrationApi* | [**create_coupon_reservation**](docs/IntegrationApi.md#create_coupon_reservation) | **POST** /v1/coupon_reservations/{couponValue} | Create a new coupon reservation
*IntegrationApi* | [**create_referral**](docs/IntegrationApi.md#create_referral) | **POST** /v1/referrals | Create a referral code for an advocate
*IntegrationApi* | [**delete_coupon_reservation**](docs/IntegrationApi.md#delete_coupon_reservation) | **DELETE** /v1/coupon_reservations/{couponValue} | Delete coupon reservations
*IntegrationApi* | [**delete_customer_data**](docs/IntegrationApi.md#delete_customer_data) | **DELETE** /v1/customer_data/{integrationId} | Delete the personal data of a customer.
*IntegrationApi* | [**get_customer_inventory**](docs/IntegrationApi.md#get_customer_inventory) | **GET** /v1/customer_profiles/{integrationId}/inventory | Get an inventory of all data associated with a specific customer profile.
*IntegrationApi* | [**get_reserved_coupons**](docs/IntegrationApi.md#get_reserved_coupons) | **GET** /v1/coupon_reservations/coupons/{integrationId} | Get all valid reserved coupons
*IntegrationApi* | [**get_reserved_customers**](docs/IntegrationApi.md#get_reserved_customers) | **GET** /v1/coupon_reservations/customerprofiles/{couponValue} | Get the users that have this coupon reserved
*IntegrationApi* | [**track_event**](docs/IntegrationApi.md#track_event) | **POST** /v1/events | Track an Event
*IntegrationApi* | [**update_customer_profile**](docs/IntegrationApi.md#update_customer_profile) | **PUT** /v1/customer_profiles/{integrationId} | Update a Customer Profile
*IntegrationApi* | [**update_customer_session**](docs/IntegrationApi.md#update_customer_session) | **PUT** /v1/customer_sessions/{customerSessionId} | Update a Customer Session
*IntegrationApi* | [**update_customer_session_v2**](docs/IntegrationApi.md#update_customer_session_v2) | **PUT** /v2/customer_sessions/{customerSessionId} | Update a Customer Session
*ManagementApi* | [**add_loyalty_points**](docs/ManagementApi.md#add_loyalty_points) | **PUT** /v1/loyalty_programs/{programID}/profile/{integrationID}/add_points | Add points in a certain loyalty program for the specified customer
*ManagementApi* | [**copy_campaign_to_applications**](docs/ManagementApi.md#copy_campaign_to_applications) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/copy | Copy the campaign into every specified application
*ManagementApi* | [**create_additional_cost**](docs/ManagementApi.md#create_additional_cost) | **POST** /v1/additional_costs | Define a new additional cost
*ManagementApi* | [**create_attribute**](docs/ManagementApi.md#create_attribute) | **POST** /v1/attributes | Define a new custom attribute
*ManagementApi* | [**create_campaign**](docs/ManagementApi.md#create_campaign) | **POST** /v1/applications/{applicationId}/campaigns | Create a Campaign
*ManagementApi* | [**create_coupons**](docs/ManagementApi.md#create_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Create Coupons
*ManagementApi* | [**create_password_recovery_email**](docs/ManagementApi.md#create_password_recovery_email) | **POST** /v1/password_recovery_emails | Request a password reset
*ManagementApi* | [**create_ruleset**](docs/ManagementApi.md#create_ruleset) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets | Create a Ruleset
*ManagementApi* | [**create_session**](docs/ManagementApi.md#create_session) | **POST** /v1/sessions | Create a Session
*ManagementApi* | [**delete_campaign**](docs/ManagementApi.md#delete_campaign) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId} | Delete a Campaign
*ManagementApi* | [**delete_coupon**](docs/ManagementApi.md#delete_coupon) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Delete one Coupon
*ManagementApi* | [**delete_coupons**](docs/ManagementApi.md#delete_coupons) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Delete Coupons
*ManagementApi* | [**delete_referral**](docs/ManagementApi.md#delete_referral) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Delete one Referral
*ManagementApi* | [**delete_ruleset**](docs/ManagementApi.md#delete_ruleset) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Delete a Ruleset
*ManagementApi* | [**get_access_logs**](docs/ManagementApi.md#get_access_logs) | **GET** /v1/applications/{applicationId}/access_logs | Get access logs for application
*ManagementApi* | [**get_access_logs_without_total_count**](docs/ManagementApi.md#get_access_logs_without_total_count) | **GET** /v1/applications/{applicationId}/access_logs/no_total | Get access logs for application
*ManagementApi* | [**get_account**](docs/ManagementApi.md#get_account) | **GET** /v1/accounts/{accountId} | Get Account Details
*ManagementApi* | [**get_account_analytics**](docs/ManagementApi.md#get_account_analytics) | **GET** /v1/accounts/{accountId}/analytics | Get Account Analytics
*ManagementApi* | [**get_additional_cost**](docs/ManagementApi.md#get_additional_cost) | **GET** /v1/additional_costs/{additionalCostId} | Get an additional cost
*ManagementApi* | [**get_additional_costs**](docs/ManagementApi.md#get_additional_costs) | **GET** /v1/additional_costs | List additional costs
*ManagementApi* | [**get_all_access_logs**](docs/ManagementApi.md#get_all_access_logs) | **GET** /v1/access_logs | Get all access logs
*ManagementApi* | [**get_all_roles**](docs/ManagementApi.md#get_all_roles) | **GET** /v1/roles | Get all roles.
*ManagementApi* | [**get_application**](docs/ManagementApi.md#get_application) | **GET** /v1/applications/{applicationId} | Get Application
*ManagementApi* | [**get_application_api_health**](docs/ManagementApi.md#get_application_api_health) | **GET** /v1/applications/{applicationId}/health_report | Get report of health of application API
*ManagementApi* | [**get_application_customer**](docs/ManagementApi.md#get_application_customer) | **GET** /v1/applications/{applicationId}/customers/{customerId} | Get Application Customer
*ManagementApi* | [**get_application_customers**](docs/ManagementApi.md#get_application_customers) | **GET** /v1/applications/{applicationId}/customers | List Application Customers
*ManagementApi* | [**get_application_customers_by_attributes**](docs/ManagementApi.md#get_application_customers_by_attributes) | **POST** /v1/application_customer_search | Get a list of the customer profiles that match the given attributes
*ManagementApi* | [**get_application_event_types**](docs/ManagementApi.md#get_application_event_types) | **GET** /v1/applications/{applicationId}/event_types | List Applications Event Types
*ManagementApi* | [**get_application_events**](docs/ManagementApi.md#get_application_events) | **GET** /v1/applications/{applicationId}/events | List Applications Events
*ManagementApi* | [**get_application_events_without_total_count**](docs/ManagementApi.md#get_application_events_without_total_count) | **GET** /v1/applications/{applicationId}/events/no_total | List Applications Events
*ManagementApi* | [**get_application_session**](docs/ManagementApi.md#get_application_session) | **GET** /v1/applications/{applicationId}/sessions/{sessionId} | Get Application Session
*ManagementApi* | [**get_application_sessions**](docs/ManagementApi.md#get_application_sessions) | **GET** /v1/applications/{applicationId}/sessions | List Application Sessions
*ManagementApi* | [**get_applications**](docs/ManagementApi.md#get_applications) | **GET** /v1/applications | List Applications
*ManagementApi* | [**get_attribute**](docs/ManagementApi.md#get_attribute) | **GET** /v1/attributes/{attributeId} | Get a custom attribute
*ManagementApi* | [**get_attributes**](docs/ManagementApi.md#get_attributes) | **GET** /v1/attributes | List custom attributes
*ManagementApi* | [**get_campaign**](docs/ManagementApi.md#get_campaign) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId} | Get a Campaign
*ManagementApi* | [**get_campaign_analytics**](docs/ManagementApi.md#get_campaign_analytics) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/analytics | Get analytics of campaigns
*ManagementApi* | [**get_campaign_by_attributes**](docs/ManagementApi.md#get_campaign_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns_search | Get a list of all campaigns that match the given attributes
*ManagementApi* | [**get_campaign_set**](docs/ManagementApi.md#get_campaign_set) | **GET** /v1/applications/{applicationId}/campaign_set | List CampaignSet
*ManagementApi* | [**get_campaigns**](docs/ManagementApi.md#get_campaigns) | **GET** /v1/applications/{applicationId}/campaigns | List your Campaigns
*ManagementApi* | [**get_changes**](docs/ManagementApi.md#get_changes) | **GET** /v1/changes | Get audit log for an account
*ManagementApi* | [**get_coupons**](docs/ManagementApi.md#get_coupons) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | List Coupons
*ManagementApi* | [**get_coupons_by_attributes**](docs/ManagementApi.md#get_coupons_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search | Get a list of the coupons that match the given attributes
*ManagementApi* | [**get_coupons_by_attributes_application_wide**](docs/ManagementApi.md#get_coupons_by_attributes_application_wide) | **POST** /v1/applications/{applicationId}/coupons_search | Get a list of the coupons that match the given attributes in all active campaigns of an application
*ManagementApi* | [**get_coupons_without_total_count**](docs/ManagementApi.md#get_coupons_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/no_total | List Coupons
*ManagementApi* | [**get_customer_activity_report**](docs/ManagementApi.md#get_customer_activity_report) | **GET** /v1/applications/{applicationId}/customer_activity_reports/{customerId} | Get Activity Report for Single Customer
*ManagementApi* | [**get_customer_activity_reports**](docs/ManagementApi.md#get_customer_activity_reports) | **GET** /v1/applications/{applicationId}/customer_activity_reports | Get Activity Reports for Application Customers
*ManagementApi* | [**get_customer_activity_reports_without_total_count**](docs/ManagementApi.md#get_customer_activity_reports_without_total_count) | **GET** /v1/applications/{applicationId}/customer_activity_reports/no_total | Get Activity Reports for Application Customers
*ManagementApi* | [**get_customer_analytics**](docs/ManagementApi.md#get_customer_analytics) | **GET** /v1/applications/{applicationId}/customers/{customerId}/analytics | Get Analytics Report for a Customer
*ManagementApi* | [**get_customer_profile**](docs/ManagementApi.md#get_customer_profile) | **GET** /v1/customers/{customerId} | Get Customer Profile
*ManagementApi* | [**get_customer_profiles**](docs/ManagementApi.md#get_customer_profiles) | **GET** /v1/customers/no_total | List Customer Profiles
*ManagementApi* | [**get_customers_by_attributes**](docs/ManagementApi.md#get_customers_by_attributes) | **POST** /v1/customer_search/no_total | Get a list of the customer profiles that match the given attributes
*ManagementApi* | [**get_event_types**](docs/ManagementApi.md#get_event_types) | **GET** /v1/event_types | List Event Types
*ManagementApi* | [**get_exports**](docs/ManagementApi.md#get_exports) | **GET** /v1/exports | Get Exports
*ManagementApi* | [**get_imports**](docs/ManagementApi.md#get_imports) | **GET** /v1/imports | Get Imports
*ManagementApi* | [**get_loyalty_points**](docs/ManagementApi.md#get_loyalty_points) | **GET** /v1/loyalty_programs/{programID}/profile/{integrationID} | get the Loyalty Ledger for this integrationID
*ManagementApi* | [**get_loyalty_program**](docs/ManagementApi.md#get_loyalty_program) | **GET** /v1/loyalty_programs/{programID} | Get a loyalty program
*ManagementApi* | [**get_loyalty_programs**](docs/ManagementApi.md#get_loyalty_programs) | **GET** /v1/loyalty_programs | List all loyalty Programs
*ManagementApi* | [**get_referrals**](docs/ManagementApi.md#get_referrals) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals | List Referrals
*ManagementApi* | [**get_referrals_without_total_count**](docs/ManagementApi.md#get_referrals_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/no_total | List Referrals
*ManagementApi* | [**get_role**](docs/ManagementApi.md#get_role) | **GET** /v1/roles/{roleId} | Get information for the specified role.
*ManagementApi* | [**get_ruleset**](docs/ManagementApi.md#get_ruleset) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Get a Ruleset
*ManagementApi* | [**get_rulesets**](docs/ManagementApi.md#get_rulesets) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets | List Campaign Rulesets
*ManagementApi* | [**get_user**](docs/ManagementApi.md#get_user) | **GET** /v1/users/{userId} | Get a single User
*ManagementApi* | [**get_users**](docs/ManagementApi.md#get_users) | **GET** /v1/users | List Users in your account
*ManagementApi* | [**get_webhook**](docs/ManagementApi.md#get_webhook) | **GET** /v1/webhooks/{webhookId} | Get Webhook
*ManagementApi* | [**get_webhook_activation_logs**](docs/ManagementApi.md#get_webhook_activation_logs) | **GET** /v1/webhook_activation_logs | List Webhook activation Log Entries
*ManagementApi* | [**get_webhook_logs**](docs/ManagementApi.md#get_webhook_logs) | **GET** /v1/webhook_logs | List Webhook Log Entries
*ManagementApi* | [**get_webhooks**](docs/ManagementApi.md#get_webhooks) | **GET** /v1/webhooks | List Webhooks
*ManagementApi* | [**remove_loyalty_points**](docs/ManagementApi.md#remove_loyalty_points) | **PUT** /v1/loyalty_programs/{programID}/profile/{integrationID}/deduct_points | Deduct points in a certain loyalty program for the specified customer
*ManagementApi* | [**reset_password**](docs/ManagementApi.md#reset_password) | **POST** /v1/reset_password | Reset password
*ManagementApi* | [**search_coupons_advanced**](docs/ManagementApi.md#search_coupons_advanced) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced | Get a list of the coupons that match the given attributes
*ManagementApi* | [**search_coupons_advanced_application_wide**](docs/ManagementApi.md#search_coupons_advanced_application_wide) | **POST** /v1/applications/{applicationId}/coupons_search_advanced | Get a list of the coupons that match the given attributes in all active campaigns of an application
*ManagementApi* | [**search_coupons_advanced_application_wide_without_total_count**](docs/ManagementApi.md#search_coupons_advanced_application_wide_without_total_count) | **POST** /v1/applications/{applicationId}/coupons_search_advanced/no_total | Get a list of the coupons that match the given attributes in all active campaigns of an application
*ManagementApi* | [**search_coupons_advanced_without_total_count**](docs/ManagementApi.md#search_coupons_advanced_without_total_count) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced/no_total | Get a list of the coupons that match the given attributes
*ManagementApi* | [**update_additional_cost**](docs/ManagementApi.md#update_additional_cost) | **PUT** /v1/additional_costs/{additionalCostId} | Update an additional cost
*ManagementApi* | [**update_attribute**](docs/ManagementApi.md#update_attribute) | **PUT** /v1/attributes/{attributeId} | Update a custom attribute
*ManagementApi* | [**update_campaign**](docs/ManagementApi.md#update_campaign) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId} | Update a Campaign
*ManagementApi* | [**update_campaign_set**](docs/ManagementApi.md#update_campaign_set) | **PUT** /v1/applications/{applicationId}/campaign_set | Update a Campaign Set
*ManagementApi* | [**update_coupon**](docs/ManagementApi.md#update_coupon) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Update a Coupon
*ManagementApi* | [**update_coupon_batch**](docs/ManagementApi.md#update_coupon_batch) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Update a Batch of Coupons
*ManagementApi* | [**update_ruleset**](docs/ManagementApi.md#update_ruleset) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Update a Ruleset


## Documentation For Models

 - [APIError](docs/APIError.md)
 - [AcceptCouponEffectProps](docs/AcceptCouponEffectProps.md)
 - [AcceptReferralEffectProps](docs/AcceptReferralEffectProps.md)
 - [AccessLogEntry](docs/AccessLogEntry.md)
 - [Account](docs/Account.md)
 - [AccountAdditionalCost](docs/AccountAdditionalCost.md)
 - [AccountAnalytics](docs/AccountAnalytics.md)
 - [AccountEntity](docs/AccountEntity.md)
 - [AccountLimits](docs/AccountLimits.md)
 - [AddFreeItemEffectProps](docs/AddFreeItemEffectProps.md)
 - [AddLoyaltyPointsEffectProps](docs/AddLoyaltyPointsEffectProps.md)
 - [AdditionalCost](docs/AdditionalCost.md)
 - [Application](docs/Application.md)
 - [ApplicationAPIKey](docs/ApplicationAPIKey.md)
 - [ApplicationApiHealth](docs/ApplicationApiHealth.md)
 - [ApplicationCustomer](docs/ApplicationCustomer.md)
 - [ApplicationCustomerEntity](docs/ApplicationCustomerEntity.md)
 - [ApplicationCustomerSearch](docs/ApplicationCustomerSearch.md)
 - [ApplicationEntity](docs/ApplicationEntity.md)
 - [ApplicationEvent](docs/ApplicationEvent.md)
 - [ApplicationSession](docs/ApplicationSession.md)
 - [ApplicationSessionEntity](docs/ApplicationSessionEntity.md)
 - [Attribute](docs/Attribute.md)
 - [AttributesMandatory](docs/AttributesMandatory.md)
 - [AttributesSettings](docs/AttributesSettings.md)
 - [BaseSamlConnection](docs/BaseSamlConnection.md)
 - [Binding](docs/Binding.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignAnalytics](docs/CampaignAnalytics.md)
 - [CampaignCopy](docs/CampaignCopy.md)
 - [CampaignEntity](docs/CampaignEntity.md)
 - [CampaignSearch](docs/CampaignSearch.md)
 - [CampaignSet](docs/CampaignSet.md)
 - [CampaignSetBranchNode](docs/CampaignSetBranchNode.md)
 - [CampaignSetLeafNode](docs/CampaignSetLeafNode.md)
 - [CampaignSetNode](docs/CampaignSetNode.md)
 - [CartItem](docs/CartItem.md)
 - [CartItemAdjustment](docs/CartItemAdjustment.md)
 - [Change](docs/Change.md)
 - [ChangeProfilePassword](docs/ChangeProfilePassword.md)
 - [CodeGeneratorSettings](docs/CodeGeneratorSettings.md)
 - [Coupon](docs/Coupon.md)
 - [CouponConstraints](docs/CouponConstraints.md)
 - [CouponCreatedEffectProps](docs/CouponCreatedEffectProps.md)
 - [CouponRejectionReason](docs/CouponRejectionReason.md)
 - [CouponReservations](docs/CouponReservations.md)
 - [CouponSearch](docs/CouponSearch.md)
 - [CouponValue](docs/CouponValue.md)
 - [CreateApplicationAPIKey](docs/CreateApplicationAPIKey.md)
 - [CustomerActivityReport](docs/CustomerActivityReport.md)
 - [CustomerAnalytics](docs/CustomerAnalytics.md)
 - [CustomerInventory](docs/CustomerInventory.md)
 - [CustomerProfile](docs/CustomerProfile.md)
 - [CustomerProfileSearchQuery](docs/CustomerProfileSearchQuery.md)
 - [CustomerSession](docs/CustomerSession.md)
 - [CustomerSessionV2](docs/CustomerSessionV2.md)
 - [DeductLoyaltyPointsEffectProps](docs/DeductLoyaltyPointsEffectProps.md)
 - [Effect](docs/Effect.md)
 - [EffectEntity](docs/EffectEntity.md)
 - [EmailEntity](docs/EmailEntity.md)
 - [Entity](docs/Entity.md)
 - [Environment](docs/Environment.md)
 - [ErrorEffectProps](docs/ErrorEffectProps.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorSource](docs/ErrorSource.md)
 - [Event](docs/Event.md)
 - [EventType](docs/EventType.md)
 - [Export](docs/Export.md)
 - [FeatureFlag](docs/FeatureFlag.md)
 - [FeatureFlags](docs/FeatureFlags.md)
 - [FeaturesFeed](docs/FeaturesFeed.md)
 - [FuncArgDef](docs/FuncArgDef.md)
 - [FunctionDef](docs/FunctionDef.md)
 - [ImportCoupons](docs/ImportCoupons.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [IntegrationEntity](docs/IntegrationEntity.md)
 - [IntegrationEvent](docs/IntegrationEvent.md)
 - [IntegrationProfileEntity](docs/IntegrationProfileEntity.md)
 - [IntegrationRequest](docs/IntegrationRequest.md)
 - [IntegrationState](docs/IntegrationState.md)
 - [IntegrationStateV2](docs/IntegrationStateV2.md)
 - [LedgerEntry](docs/LedgerEntry.md)
 - [LibraryAttribute](docs/LibraryAttribute.md)
 - [LimitConfig](docs/LimitConfig.md)
 - [LoginParams](docs/LoginParams.md)
 - [Loyalty](docs/Loyalty.md)
 - [LoyaltyLedger](docs/LoyaltyLedger.md)
 - [LoyaltyLedgerEntry](docs/LoyaltyLedgerEntry.md)
 - [LoyaltyMembership](docs/LoyaltyMembership.md)
 - [LoyaltyPoints](docs/LoyaltyPoints.md)
 - [LoyaltyProgram](docs/LoyaltyProgram.md)
 - [LoyaltyProgramBalance](docs/LoyaltyProgramBalance.md)
 - [LoyaltyProgramLedgers](docs/LoyaltyProgramLedgers.md)
 - [LoyaltySubLedger](docs/LoyaltySubLedger.md)
 - [ManagerConfig](docs/ManagerConfig.md)
 - [Meta](docs/Meta.md)
 - [MiscUpdateUserLatestFeature](docs/MiscUpdateUserLatestFeature.md)
 - [ModelImport](docs/ModelImport.md)
 - [MultiApplicationEntity](docs/MultiApplicationEntity.md)
 - [MutableEntity](docs/MutableEntity.md)
 - [NewAccount](docs/NewAccount.md)
 - [NewAccountSignUp](docs/NewAccountSignUp.md)
 - [NewAdditionalCost](docs/NewAdditionalCost.md)
 - [NewApplication](docs/NewApplication.md)
 - [NewApplicationAPIKey](docs/NewApplicationAPIKey.md)
 - [NewAttribute](docs/NewAttribute.md)
 - [NewCampaign](docs/NewCampaign.md)
 - [NewCampaignSet](docs/NewCampaignSet.md)
 - [NewCoupons](docs/NewCoupons.md)
 - [NewCustomerProfile](docs/NewCustomerProfile.md)
 - [NewCustomerSession](docs/NewCustomerSession.md)
 - [NewCustomerSessionV2](docs/NewCustomerSessionV2.md)
 - [NewEvent](docs/NewEvent.md)
 - [NewEventType](docs/NewEventType.md)
 - [NewFeatureFlags](docs/NewFeatureFlags.md)
 - [NewImport](docs/NewImport.md)
 - [NewInvitation](docs/NewInvitation.md)
 - [NewInviteEmail](docs/NewInviteEmail.md)
 - [NewLoyaltyProgram](docs/NewLoyaltyProgram.md)
 - [NewPassword](docs/NewPassword.md)
 - [NewPasswordEmail](docs/NewPasswordEmail.md)
 - [NewReferral](docs/NewReferral.md)
 - [NewRole](docs/NewRole.md)
 - [NewRuleset](docs/NewRuleset.md)
 - [NewSamlConnection](docs/NewSamlConnection.md)
 - [NewTemplateDef](docs/NewTemplateDef.md)
 - [NewUser](docs/NewUser.md)
 - [NewWebhook](docs/NewWebhook.md)
 - [Notification](docs/Notification.md)
 - [RedeemReferralEffectProps](docs/RedeemReferralEffectProps.md)
 - [Referral](docs/Referral.md)
 - [ReferralCreatedEffectProps](docs/ReferralCreatedEffectProps.md)
 - [ReferralRejectionReason](docs/ReferralRejectionReason.md)
 - [RejectCouponEffectProps](docs/RejectCouponEffectProps.md)
 - [RejectReferralEffectProps](docs/RejectReferralEffectProps.md)
 - [Role](docs/Role.md)
 - [RoleAssign](docs/RoleAssign.md)
 - [RoleMembership](docs/RoleMembership.md)
 - [RollbackCouponEffectProps](docs/RollbackCouponEffectProps.md)
 - [RollbackDiscountEffectProps](docs/RollbackDiscountEffectProps.md)
 - [Rule](docs/Rule.md)
 - [Ruleset](docs/Ruleset.md)
 - [SamlConnection](docs/SamlConnection.md)
 - [SamlConnectionMetadata](docs/SamlConnectionMetadata.md)
 - [SamlLoginEndpoint](docs/SamlLoginEndpoint.md)
 - [Session](docs/Session.md)
 - [SetDiscountEffectProps](docs/SetDiscountEffectProps.md)
 - [SetDiscountPerItemEffectProps](docs/SetDiscountPerItemEffectProps.md)
 - [ShowBundleMetadataEffectProps](docs/ShowBundleMetadataEffectProps.md)
 - [ShowNotificationEffectProps](docs/ShowNotificationEffectProps.md)
 - [SlotDef](docs/SlotDef.md)
 - [TemplateArgDef](docs/TemplateArgDef.md)
 - [TemplateDef](docs/TemplateDef.md)
 - [TriggerWebhookEffectProps](docs/TriggerWebhookEffectProps.md)
 - [UpdateAccount](docs/UpdateAccount.md)
 - [UpdateApplication](docs/UpdateApplication.md)
 - [UpdateAttributeEffectProps](docs/UpdateAttributeEffectProps.md)
 - [UpdateCampaign](docs/UpdateCampaign.md)
 - [UpdateCoupon](docs/UpdateCoupon.md)
 - [UpdateCouponBatch](docs/UpdateCouponBatch.md)
 - [UpdateLoyaltyProgram](docs/UpdateLoyaltyProgram.md)
 - [UpdateRole](docs/UpdateRole.md)
 - [UpdateUser](docs/UpdateUser.md)
 - [User](docs/User.md)
 - [UserEntity](docs/UserEntity.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookActivationLogEntry](docs/WebhookActivationLogEntry.md)
 - [WebhookLogEntry](docs/WebhookLogEntry.md)


## Documentation For Authorization


## api_key_v1

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## integration_auth

- **Type**: API key
- **API key parameter name**: Content-Signature
- **Location**: HTTP header


## manager_auth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




