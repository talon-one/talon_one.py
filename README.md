# Talon.One Python SDK

This SDK supports all of the operations of Talon.One's Integration API and Management API.

## Installation and usage

### pip install

The SDK is available on [PyPi](https://pypi.org/project/talon-one-python-sdk/):

```sh
pip install talon-one-python-sdk
```

**Note**: You may need to run `pip` with root permissions: `sudo pip install talon-one-python-sdk`.

### Setuptools

You can also install the SDK via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
python setup.py install --user
```

**Note**: To install the package for all users, run `sudo python setup.py install`.

## Determining the base URL of the endpoints

The API is available at the same hostname as your Campaign Manager deployment.
For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one`,
the URL for the [Update customer session](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint
is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`.

## Getting started

### Integration API

The following code shows an example of using the Integration API:

```python
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
import json

# Create configuration with your host destination and authorization using api_key_v1
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one", # No trailing slash!
    api_key_prefix = {
        "Authorization": "ApiKey-v1"
    },
    api_key = {
        "Authorization": "e18149e88f42247f0123456789abcdef9302722577ad60cebc86c4333b6fb70"
    }
)

# Integration API example to send a session update
integration_api = talon_one.IntegrationApi(talon_one.ApiClient(configuration))

# Preparing a NewCustomerSessionV2 object
customer_session = talon_one.NewCustomerSessionV2(
  "PROFILE_ID"
)
customer_session.cart_items = [
    talon_one.CartItem(name="Red Spring Blouse",
                       sku="rdbs-1111",
                       quantity=1,
                       price=49,
                       category="Shirts"),
    talon_one.CartItem(name="Denim Trousers",
                       sku="dtr-2222",
                       quantity=1,
                       price=74,
                       category="Trousers"),
]
customer_session.coupon_codes = [
    "Cool_Stuff"
]

# Instantiating a new IntegrationRequest object
integration_request = talon_one.IntegrationRequest(
    customer_session,
    # Optional list of requested information to be present on the response.
    # See models/integration_request.py for full list
    # ["customerSession", "loyalty"]
)

try:
    # Create/update a customer session using `update_customer_session_v2` function
    api_response = integration_api.update_customer_session_v2("my_unique_session_v2_id", integration_request)
    encoded_data = json.dumps(api_response.to_dict(), default=str)
    pprint(encoded_data)

    # Parsing the returned effects list, please consult https://developers.talon.one/Integration-API/handling-effects-v2 for the full list of effects and their corresponding properties
    for effect in api_response.effects:
        if effect.effect_type == "setDiscount":
            # Initiating right props instance according to the effect type
            setDiscountProps = integration_api.api_client.deserialize_model(effect.props, talon_one.SetDiscountEffectProps)

            # Access the specific effect's properties
            print("Set a discount '{name}' of {value}".format(
                name = setDiscountProps.name,
                value = setDiscountProps.value
            ))
        elif effect.effect_type == "rejectCoupon":
            rejectCouponEffectProps = integration_api.api_client.deserialize_model(effect.props, talon_one.RejectCouponEffectProps)

            # Work with AcceptCouponEffectProps' properties
            # ...
except ApiException as e:
    print("Exception when calling IntegrationApi->update_customer_session_v2: %s\n" % e)
```

### Management API

The following code shows an example of using the Management API:

```python
import talon_one
from pprint import pprint
import json

# Create configuration with your host destination and authorization using management_key
configuration = talon_one.Configuration(
    host = "https://yourbaseurl.talon.one", # No trailing slash!
    api_key_prefix = {
        "Authorization": "ManagementKey-v1"
    },
    api_key = {
        "Authorization": "2f0dce055da01ae595005d7d79154bae7448d319d5fc7c5b2951fadd6ba1ea07"
    }
)

# Management API example to load application with id 7
management_api = talon_one.ManagementApi(talon_one.ApiClient(configuration))

try:
    # Calling get_application function with the desired id (7)
    application = management_api.get_application(7)
    encoded_data = json.dumps(application.to_dict(), default=str)
    pprint(encoded_data)
except ApiException as e:
    print("Exception when calling ManagementApi: %s\n" % e)
```

## Documentation for API endpoints

All URLs are relative to `https://yourbaseurl.talon.one`.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IntegrationApi* | [**create_audience_v2**](docs/IntegrationApi.md#create_audience_v2) | **POST** /v2/audiences | Create audience
*IntegrationApi* | [**create_coupon_reservation**](docs/IntegrationApi.md#create_coupon_reservation) | **POST** /v1/coupon_reservations/{couponValue} | Create coupon reservation
*IntegrationApi* | [**create_referral**](docs/IntegrationApi.md#create_referral) | **POST** /v1/referrals | Create referral code for an advocate
*IntegrationApi* | [**create_referrals_for_multiple_advocates**](docs/IntegrationApi.md#create_referrals_for_multiple_advocates) | **POST** /v1/referrals_for_multiple_advocates | Create referral codes for multiple advocates
*IntegrationApi* | [**delete_audience_memberships_v2**](docs/IntegrationApi.md#delete_audience_memberships_v2) | **DELETE** /v2/audiences/{audienceId}/memberships | Delete audience memberships
*IntegrationApi* | [**delete_audience_v2**](docs/IntegrationApi.md#delete_audience_v2) | **DELETE** /v2/audiences/{audienceId} | Delete audience
*IntegrationApi* | [**delete_coupon_reservation**](docs/IntegrationApi.md#delete_coupon_reservation) | **DELETE** /v1/coupon_reservations/{couponValue} | Delete coupon reservations
*IntegrationApi* | [**delete_customer_data**](docs/IntegrationApi.md#delete_customer_data) | **DELETE** /v1/customer_data/{integrationId} | Delete customer&#39;s personal data
*IntegrationApi* | [**generate_loyalty_card**](docs/IntegrationApi.md#generate_loyalty_card) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/cards | Generate loyalty card
*IntegrationApi* | [**get_customer_achievement_history**](docs/IntegrationApi.md#get_customer_achievement_history) | **GET** /v1/customer_profiles/{integrationId}/achievements/{achievementId} | List customer&#39;s achievement history
*IntegrationApi* | [**get_customer_achievements**](docs/IntegrationApi.md#get_customer_achievements) | **GET** /v1/customer_profiles/{integrationId}/achievements | List customer&#39;s available achievements
*IntegrationApi* | [**get_customer_inventory**](docs/IntegrationApi.md#get_customer_inventory) | **GET** /v1/customer_profiles/{integrationId}/inventory | List customer data
*IntegrationApi* | [**get_customer_session**](docs/IntegrationApi.md#get_customer_session) | **GET** /v2/customer_sessions/{customerSessionId} | Get customer session
*IntegrationApi* | [**get_loyalty_balances**](docs/IntegrationApi.md#get_loyalty_balances) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/balances | Get customer&#39;s loyalty balances
*IntegrationApi* | [**get_loyalty_card_balances**](docs/IntegrationApi.md#get_loyalty_card_balances) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/balances | Get card&#39;s point balances
*IntegrationApi* | [**get_loyalty_card_points**](docs/IntegrationApi.md#get_loyalty_card_points) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/points | List card&#39;s unused loyalty points
*IntegrationApi* | [**get_loyalty_card_transactions**](docs/IntegrationApi.md#get_loyalty_card_transactions) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/transactions | List card&#39;s transactions
*IntegrationApi* | [**get_loyalty_program_profile_points**](docs/IntegrationApi.md#get_loyalty_program_profile_points) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/points | List customer&#39;s unused loyalty points
*IntegrationApi* | [**get_loyalty_program_profile_transactions**](docs/IntegrationApi.md#get_loyalty_program_profile_transactions) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/transactions | List customer&#39;s loyalty transactions
*IntegrationApi* | [**get_reserved_customers**](docs/IntegrationApi.md#get_reserved_customers) | **GET** /v1/coupon_reservations/customerprofiles/{couponValue} | List customers that have this coupon reserved
*IntegrationApi* | [**link_loyalty_card_to_profile**](docs/IntegrationApi.md#link_loyalty_card_to_profile) | **POST** /v2/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/link_profile | Link customer profile to card
*IntegrationApi* | [**reopen_customer_session**](docs/IntegrationApi.md#reopen_customer_session) | **PUT** /v2/customer_sessions/{customerSessionId}/reopen | Reopen customer session
*IntegrationApi* | [**return_cart_items**](docs/IntegrationApi.md#return_cart_items) | **POST** /v2/customer_sessions/{customerSessionId}/returns | Return cart items
*IntegrationApi* | [**sync_catalog**](docs/IntegrationApi.md#sync_catalog) | **PUT** /v1/catalogs/{catalogId}/sync | Sync cart item catalog
*IntegrationApi* | [**track_event_v2**](docs/IntegrationApi.md#track_event_v2) | **POST** /v2/events | Track event
*IntegrationApi* | [**update_audience_customers_attributes**](docs/IntegrationApi.md#update_audience_customers_attributes) | **PUT** /v2/audience_customers/{audienceId}/attributes | Update profile attributes for all customers in audience
*IntegrationApi* | [**update_audience_v2**](docs/IntegrationApi.md#update_audience_v2) | **PUT** /v2/audiences/{audienceId} | Update audience name
*IntegrationApi* | [**update_customer_profile_audiences**](docs/IntegrationApi.md#update_customer_profile_audiences) | **POST** /v2/customer_audiences | Update multiple customer profiles&#39; audiences
*IntegrationApi* | [**update_customer_profile_v2**](docs/IntegrationApi.md#update_customer_profile_v2) | **PUT** /v2/customer_profiles/{integrationId} | Update customer profile
*IntegrationApi* | [**update_customer_profiles_v2**](docs/IntegrationApi.md#update_customer_profiles_v2) | **PUT** /v2/customer_profiles | Update multiple customer profiles
*IntegrationApi* | [**update_customer_session_v2**](docs/IntegrationApi.md#update_customer_session_v2) | **PUT** /v2/customer_sessions/{customerSessionId} | Update customer session
*ManagementApi* | [**activate_user_by_email**](docs/ManagementApi.md#activate_user_by_email) | **POST** /v1/users/activate | Enable user by email address
*ManagementApi* | [**add_loyalty_card_points**](docs/ManagementApi.md#add_loyalty_card_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/add_points | Add points to card
*ManagementApi* | [**add_loyalty_points**](docs/ManagementApi.md#add_loyalty_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/add_points | Add points to customer profile
*ManagementApi* | [**copy_campaign_to_applications**](docs/ManagementApi.md#copy_campaign_to_applications) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/copy | Copy the campaign into the specified Application
*ManagementApi* | [**create_account_collection**](docs/ManagementApi.md#create_account_collection) | **POST** /v1/collections | Create account-level collection
*ManagementApi* | [**create_achievement**](docs/ManagementApi.md#create_achievement) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/achievements | Create achievement
*ManagementApi* | [**create_additional_cost**](docs/ManagementApi.md#create_additional_cost) | **POST** /v1/additional_costs | Create additional cost
*ManagementApi* | [**create_attribute**](docs/ManagementApi.md#create_attribute) | **POST** /v1/attributes | Create custom attribute
*ManagementApi* | [**create_batch_loyalty_cards**](docs/ManagementApi.md#create_batch_loyalty_cards) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/cards/batch | Create loyalty cards
*ManagementApi* | [**create_campaign_from_template**](docs/ManagementApi.md#create_campaign_from_template) | **POST** /v1/applications/{applicationId}/create_campaign_from_template | Create campaign from campaign template
*ManagementApi* | [**create_collection**](docs/ManagementApi.md#create_collection) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/collections | Create campaign-level collection
*ManagementApi* | [**create_coupons**](docs/ManagementApi.md#create_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Create coupons
*ManagementApi* | [**create_coupons_async**](docs/ManagementApi.md#create_coupons_async) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_async | Create coupons asynchronously
*ManagementApi* | [**create_coupons_deletion_job**](docs/ManagementApi.md#create_coupons_deletion_job) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_deletion_jobs | Creates a coupon deletion job
*ManagementApi* | [**create_coupons_for_multiple_recipients**](docs/ManagementApi.md#create_coupons_for_multiple_recipients) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_with_recipients | Create coupons for multiple recipients
*ManagementApi* | [**create_invite_email**](docs/ManagementApi.md#create_invite_email) | **POST** /v1/invite_emails | Resend invitation email
*ManagementApi* | [**create_invite_v2**](docs/ManagementApi.md#create_invite_v2) | **POST** /v2/invites | Invite user
*ManagementApi* | [**create_password_recovery_email**](docs/ManagementApi.md#create_password_recovery_email) | **POST** /v1/password_recovery_emails | Request a password reset
*ManagementApi* | [**create_session**](docs/ManagementApi.md#create_session) | **POST** /v1/sessions | Create session
*ManagementApi* | [**create_store**](docs/ManagementApi.md#create_store) | **POST** /v1/applications/{applicationId}/stores | Create store
*ManagementApi* | [**deactivate_user_by_email**](docs/ManagementApi.md#deactivate_user_by_email) | **POST** /v1/users/deactivate | Disable user by email address
*ManagementApi* | [**deduct_loyalty_card_points**](docs/ManagementApi.md#deduct_loyalty_card_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/deduct_points | Deduct points from card
*ManagementApi* | [**delete_account_collection**](docs/ManagementApi.md#delete_account_collection) | **DELETE** /v1/collections/{collectionId} | Delete account-level collection
*ManagementApi* | [**delete_achievement**](docs/ManagementApi.md#delete_achievement) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/achievements/{achievementId} | Delete achievement
*ManagementApi* | [**delete_campaign**](docs/ManagementApi.md#delete_campaign) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId} | Delete campaign
*ManagementApi* | [**delete_collection**](docs/ManagementApi.md#delete_collection) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Delete campaign-level collection
*ManagementApi* | [**delete_coupon**](docs/ManagementApi.md#delete_coupon) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Delete coupon
*ManagementApi* | [**delete_coupons**](docs/ManagementApi.md#delete_coupons) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Delete coupons
*ManagementApi* | [**delete_loyalty_card**](docs/ManagementApi.md#delete_loyalty_card) | **DELETE** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId} | Delete loyalty card
*ManagementApi* | [**delete_referral**](docs/ManagementApi.md#delete_referral) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Delete referral
*ManagementApi* | [**delete_store**](docs/ManagementApi.md#delete_store) | **DELETE** /v1/applications/{applicationId}/stores/{storeId} | Delete store
*ManagementApi* | [**delete_user**](docs/ManagementApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete user
*ManagementApi* | [**delete_user_by_email**](docs/ManagementApi.md#delete_user_by_email) | **POST** /v1/users/delete | Delete user by email address
*ManagementApi* | [**destroy_session**](docs/ManagementApi.md#destroy_session) | **DELETE** /v1/sessions | Destroy session
*ManagementApi* | [**disconnect_campaign_stores**](docs/ManagementApi.md#disconnect_campaign_stores) | **DELETE** /v1/applications/{applicationId}/campaigns/{campaignId}/stores | Disconnect stores
*ManagementApi* | [**export_account_collection_items**](docs/ManagementApi.md#export_account_collection_items) | **GET** /v1/collections/{collectionId}/export | Export account-level collection&#39;s items
*ManagementApi* | [**export_achievements**](docs/ManagementApi.md#export_achievements) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/achievements/{achievementId}/export | Export achievement customer data
*ManagementApi* | [**export_audiences_memberships**](docs/ManagementApi.md#export_audiences_memberships) | **GET** /v1/audiences/{audienceId}/memberships/export | Export audience members
*ManagementApi* | [**export_campaign_stores**](docs/ManagementApi.md#export_campaign_stores) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/stores/export | Export stores
*ManagementApi* | [**export_collection_items**](docs/ManagementApi.md#export_collection_items) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId}/export | Export campaign-level collection&#39;s items
*ManagementApi* | [**export_coupons**](docs/ManagementApi.md#export_coupons) | **GET** /v1/applications/{applicationId}/export_coupons | Export coupons
*ManagementApi* | [**export_customer_sessions**](docs/ManagementApi.md#export_customer_sessions) | **GET** /v1/applications/{applicationId}/export_customer_sessions | Export customer sessions
*ManagementApi* | [**export_customers_tiers**](docs/ManagementApi.md#export_customers_tiers) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_customers_tiers | Export customers&#39; tier data
*ManagementApi* | [**export_effects**](docs/ManagementApi.md#export_effects) | **GET** /v1/applications/{applicationId}/export_effects | Export triggered effects
*ManagementApi* | [**export_loyalty_balance**](docs/ManagementApi.md#export_loyalty_balance) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_customer_balance | Export customer loyalty balance to CSV
*ManagementApi* | [**export_loyalty_balances**](docs/ManagementApi.md#export_loyalty_balances) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_customer_balances | Export customer loyalty balances
*ManagementApi* | [**export_loyalty_card_balances**](docs/ManagementApi.md#export_loyalty_card_balances) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/export_card_balances | Export all card transaction logs
*ManagementApi* | [**export_loyalty_card_ledger**](docs/ManagementApi.md#export_loyalty_card_ledger) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/export_log | Export card&#39;s ledger log
*ManagementApi* | [**export_loyalty_cards**](docs/ManagementApi.md#export_loyalty_cards) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/export | Export loyalty cards
*ManagementApi* | [**export_loyalty_ledger**](docs/ManagementApi.md#export_loyalty_ledger) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/export_log | Export customer&#39;s transaction logs
*ManagementApi* | [**export_pool_giveaways**](docs/ManagementApi.md#export_pool_giveaways) | **GET** /v1/giveaways/pools/{poolId}/export | Export giveaway codes of a giveaway pool
*ManagementApi* | [**export_referrals**](docs/ManagementApi.md#export_referrals) | **GET** /v1/applications/{applicationId}/export_referrals | Export referrals
*ManagementApi* | [**get_access_logs_without_total_count**](docs/ManagementApi.md#get_access_logs_without_total_count) | **GET** /v1/applications/{applicationId}/access_logs/no_total | Get access logs for Application
*ManagementApi* | [**get_account**](docs/ManagementApi.md#get_account) | **GET** /v1/accounts/{accountId} | Get account details
*ManagementApi* | [**get_account_analytics**](docs/ManagementApi.md#get_account_analytics) | **GET** /v1/accounts/{accountId}/analytics | Get account analytics
*ManagementApi* | [**get_account_collection**](docs/ManagementApi.md#get_account_collection) | **GET** /v1/collections/{collectionId} | Get account-level collection
*ManagementApi* | [**get_achievement**](docs/ManagementApi.md#get_achievement) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/achievements/{achievementId} | Get achievement
*ManagementApi* | [**get_additional_cost**](docs/ManagementApi.md#get_additional_cost) | **GET** /v1/additional_costs/{additionalCostId} | Get additional cost
*ManagementApi* | [**get_additional_costs**](docs/ManagementApi.md#get_additional_costs) | **GET** /v1/additional_costs | List additional costs
*ManagementApi* | [**get_application**](docs/ManagementApi.md#get_application) | **GET** /v1/applications/{applicationId} | Get Application
*ManagementApi* | [**get_application_api_health**](docs/ManagementApi.md#get_application_api_health) | **GET** /v1/applications/{applicationId}/health_report | Get Application health
*ManagementApi* | [**get_application_customer**](docs/ManagementApi.md#get_application_customer) | **GET** /v1/applications/{applicationId}/customers/{customerId} | Get application&#39;s customer
*ManagementApi* | [**get_application_customer_friends**](docs/ManagementApi.md#get_application_customer_friends) | **GET** /v1/applications/{applicationId}/profile/{integrationId}/friends | List friends referred by customer profile
*ManagementApi* | [**get_application_customers**](docs/ManagementApi.md#get_application_customers) | **GET** /v1/applications/{applicationId}/customers | List application&#39;s customers
*ManagementApi* | [**get_application_customers_by_attributes**](docs/ManagementApi.md#get_application_customers_by_attributes) | **POST** /v1/applications/{applicationId}/customer_search | List application customers matching the given attributes
*ManagementApi* | [**get_application_event_types**](docs/ManagementApi.md#get_application_event_types) | **GET** /v1/applications/{applicationId}/event_types | List Applications event types
*ManagementApi* | [**get_application_events_without_total_count**](docs/ManagementApi.md#get_application_events_without_total_count) | **GET** /v1/applications/{applicationId}/events/no_total | List Applications events
*ManagementApi* | [**get_application_session**](docs/ManagementApi.md#get_application_session) | **GET** /v1/applications/{applicationId}/sessions/{sessionId} | Get Application session
*ManagementApi* | [**get_application_sessions**](docs/ManagementApi.md#get_application_sessions) | **GET** /v1/applications/{applicationId}/sessions | List Application sessions
*ManagementApi* | [**get_applications**](docs/ManagementApi.md#get_applications) | **GET** /v1/applications | List Applications
*ManagementApi* | [**get_attribute**](docs/ManagementApi.md#get_attribute) | **GET** /v1/attributes/{attributeId} | Get custom attribute
*ManagementApi* | [**get_attributes**](docs/ManagementApi.md#get_attributes) | **GET** /v1/attributes | List custom attributes
*ManagementApi* | [**get_audience_memberships**](docs/ManagementApi.md#get_audience_memberships) | **GET** /v1/audiences/{audienceId}/memberships | List audience members
*ManagementApi* | [**get_audiences**](docs/ManagementApi.md#get_audiences) | **GET** /v1/audiences | List audiences
*ManagementApi* | [**get_audiences_analytics**](docs/ManagementApi.md#get_audiences_analytics) | **GET** /v1/audiences/analytics | List audience analytics
*ManagementApi* | [**get_campaign**](docs/ManagementApi.md#get_campaign) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId} | Get campaign
*ManagementApi* | [**get_campaign_analytics**](docs/ManagementApi.md#get_campaign_analytics) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/analytics | Get analytics of campaigns
*ManagementApi* | [**get_campaign_by_attributes**](docs/ManagementApi.md#get_campaign_by_attributes) | **POST** /v1/applications/{applicationId}/campaigns_search | List campaigns that match the given attributes
*ManagementApi* | [**get_campaign_group**](docs/ManagementApi.md#get_campaign_group) | **GET** /v1/campaign_groups/{campaignGroupId} | Get campaign access group
*ManagementApi* | [**get_campaign_groups**](docs/ManagementApi.md#get_campaign_groups) | **GET** /v1/campaign_groups | List campaign access groups
*ManagementApi* | [**get_campaign_templates**](docs/ManagementApi.md#get_campaign_templates) | **GET** /v1/campaign_templates | List campaign templates
*ManagementApi* | [**get_campaigns**](docs/ManagementApi.md#get_campaigns) | **GET** /v1/applications/{applicationId}/campaigns | List campaigns
*ManagementApi* | [**get_changes**](docs/ManagementApi.md#get_changes) | **GET** /v1/changes | Get audit logs for an account
*ManagementApi* | [**get_collection**](docs/ManagementApi.md#get_collection) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Get campaign-level collection
*ManagementApi* | [**get_collection_items**](docs/ManagementApi.md#get_collection_items) | **GET** /v1/collections/{collectionId}/items | Get collection items
*ManagementApi* | [**get_coupons_without_total_count**](docs/ManagementApi.md#get_coupons_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/no_total | List coupons
*ManagementApi* | [**get_customer_activity_report**](docs/ManagementApi.md#get_customer_activity_report) | **GET** /v1/applications/{applicationId}/customer_activity_reports/{customerId} | Get customer&#39;s activity report
*ManagementApi* | [**get_customer_activity_reports_without_total_count**](docs/ManagementApi.md#get_customer_activity_reports_without_total_count) | **GET** /v1/applications/{applicationId}/customer_activity_reports/no_total | Get Activity Reports for Application Customers
*ManagementApi* | [**get_customer_analytics**](docs/ManagementApi.md#get_customer_analytics) | **GET** /v1/applications/{applicationId}/customers/{customerId}/analytics | Get customer&#39;s analytics report
*ManagementApi* | [**get_customer_profile**](docs/ManagementApi.md#get_customer_profile) | **GET** /v1/customers/{customerId} | Get customer profile
*ManagementApi* | [**get_customer_profile_achievement_progress**](docs/ManagementApi.md#get_customer_profile_achievement_progress) | **GET** /v1/applications/{applicationId}/achievement_progress/{integrationId} | List customer achievements
*ManagementApi* | [**get_customer_profiles**](docs/ManagementApi.md#get_customer_profiles) | **GET** /v1/customers/no_total | List customer profiles
*ManagementApi* | [**get_customers_by_attributes**](docs/ManagementApi.md#get_customers_by_attributes) | **POST** /v1/customer_search/no_total | List customer profiles matching the given attributes
*ManagementApi* | [**get_dashboard_statistics**](docs/ManagementApi.md#get_dashboard_statistics) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/dashboard | Get statistics for loyalty dashboard
*ManagementApi* | [**get_event_types**](docs/ManagementApi.md#get_event_types) | **GET** /v1/event_types | List event types
*ManagementApi* | [**get_exports**](docs/ManagementApi.md#get_exports) | **GET** /v1/exports | Get exports
*ManagementApi* | [**get_loyalty_card**](docs/ManagementApi.md#get_loyalty_card) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId} | Get loyalty card
*ManagementApi* | [**get_loyalty_card_transaction_logs**](docs/ManagementApi.md#get_loyalty_card_transaction_logs) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/logs | List card&#39;s transactions
*ManagementApi* | [**get_loyalty_cards**](docs/ManagementApi.md#get_loyalty_cards) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/cards | List loyalty cards
*ManagementApi* | [**get_loyalty_points**](docs/ManagementApi.md#get_loyalty_points) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId} | Get customer&#39;s full loyalty ledger
*ManagementApi* | [**get_loyalty_program**](docs/ManagementApi.md#get_loyalty_program) | **GET** /v1/loyalty_programs/{loyaltyProgramId} | Get loyalty program
*ManagementApi* | [**get_loyalty_program_transactions**](docs/ManagementApi.md#get_loyalty_program_transactions) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/transactions | List loyalty program transactions
*ManagementApi* | [**get_loyalty_programs**](docs/ManagementApi.md#get_loyalty_programs) | **GET** /v1/loyalty_programs | List loyalty programs
*ManagementApi* | [**get_loyalty_statistics**](docs/ManagementApi.md#get_loyalty_statistics) | **GET** /v1/loyalty_programs/{loyaltyProgramId}/statistics | Get loyalty program statistics
*ManagementApi* | [**get_message_logs**](docs/ManagementApi.md#get_message_logs) | **GET** /v1/message_logs | List message log entries
*ManagementApi* | [**get_referrals_without_total_count**](docs/ManagementApi.md#get_referrals_without_total_count) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/no_total | List referrals
*ManagementApi* | [**get_role_v2**](docs/ManagementApi.md#get_role_v2) | **GET** /v2/roles/{roleId} | Get role
*ManagementApi* | [**get_ruleset**](docs/ManagementApi.md#get_ruleset) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets/{rulesetId} | Get ruleset
*ManagementApi* | [**get_rulesets**](docs/ManagementApi.md#get_rulesets) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/rulesets | List campaign rulesets
*ManagementApi* | [**get_store**](docs/ManagementApi.md#get_store) | **GET** /v1/applications/{applicationId}/stores/{storeId} | Get store
*ManagementApi* | [**get_user**](docs/ManagementApi.md#get_user) | **GET** /v1/users/{userId} | Get user
*ManagementApi* | [**get_users**](docs/ManagementApi.md#get_users) | **GET** /v1/users | List users in account
*ManagementApi* | [**get_webhook**](docs/ManagementApi.md#get_webhook) | **GET** /v1/webhooks/{webhookId} | Get webhook
*ManagementApi* | [**get_webhook_activation_logs**](docs/ManagementApi.md#get_webhook_activation_logs) | **GET** /v1/webhook_activation_logs | List webhook activation log entries
*ManagementApi* | [**get_webhook_logs**](docs/ManagementApi.md#get_webhook_logs) | **GET** /v1/webhook_logs | List webhook log entries
*ManagementApi* | [**get_webhooks**](docs/ManagementApi.md#get_webhooks) | **GET** /v1/webhooks | List webhooks
*ManagementApi* | [**import_account_collection**](docs/ManagementApi.md#import_account_collection) | **POST** /v1/collections/{collectionId}/import | Import data into existing account-level collection
*ManagementApi* | [**import_allowed_list**](docs/ManagementApi.md#import_allowed_list) | **POST** /v1/attributes/{attributeId}/allowed_list/import | Import allowed values for attribute
*ManagementApi* | [**import_audiences_memberships**](docs/ManagementApi.md#import_audiences_memberships) | **POST** /v1/audiences/{audienceId}/memberships/import | Import audience members
*ManagementApi* | [**import_campaign_stores**](docs/ManagementApi.md#import_campaign_stores) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/stores/import | Import stores
*ManagementApi* | [**import_collection**](docs/ManagementApi.md#import_collection) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId}/import | Import data into existing campaign-level collection
*ManagementApi* | [**import_coupons**](docs/ManagementApi.md#import_coupons) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_coupons | Import coupons
*ManagementApi* | [**import_loyalty_cards**](docs/ManagementApi.md#import_loyalty_cards) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/import_cards | Import loyalty cards
*ManagementApi* | [**import_loyalty_customers_tiers**](docs/ManagementApi.md#import_loyalty_customers_tiers) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/import_customers_tiers | Import customers into loyalty tiers
*ManagementApi* | [**import_loyalty_points**](docs/ManagementApi.md#import_loyalty_points) | **POST** /v1/loyalty_programs/{loyaltyProgramId}/import_points | Import loyalty points
*ManagementApi* | [**import_pool_giveaways**](docs/ManagementApi.md#import_pool_giveaways) | **POST** /v1/giveaways/pools/{poolId}/import | Import giveaway codes into a giveaway pool
*ManagementApi* | [**import_referrals**](docs/ManagementApi.md#import_referrals) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/import_referrals | Import referrals
*ManagementApi* | [**invite_user_external**](docs/ManagementApi.md#invite_user_external) | **POST** /v1/users/invite | Invite user from identity provider
*ManagementApi* | [**list_account_collections**](docs/ManagementApi.md#list_account_collections) | **GET** /v1/collections | List collections in account
*ManagementApi* | [**list_achievements**](docs/ManagementApi.md#list_achievements) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/achievements | List achievements
*ManagementApi* | [**list_all_roles_v2**](docs/ManagementApi.md#list_all_roles_v2) | **GET** /v2/roles | List roles
*ManagementApi* | [**list_catalog_items**](docs/ManagementApi.md#list_catalog_items) | **GET** /v1/catalogs/{catalogId}/items | List items in a catalog
*ManagementApi* | [**list_collections**](docs/ManagementApi.md#list_collections) | **GET** /v1/applications/{applicationId}/campaigns/{campaignId}/collections | List collections in campaign
*ManagementApi* | [**list_collections_in_application**](docs/ManagementApi.md#list_collections_in_application) | **GET** /v1/applications/{applicationId}/collections | List collections in Application
*ManagementApi* | [**list_stores**](docs/ManagementApi.md#list_stores) | **GET** /v1/applications/{applicationId}/stores | List stores
*ManagementApi* | [**okta_event_handler_challenge**](docs/ManagementApi.md#okta_event_handler_challenge) | **GET** /v1/provisioning/okta | Validate Okta API ownership
*ManagementApi* | [**remove_loyalty_points**](docs/ManagementApi.md#remove_loyalty_points) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/profile/{integrationId}/deduct_points | Deduct points from customer profile
*ManagementApi* | [**reset_password**](docs/ManagementApi.md#reset_password) | **POST** /v1/reset_password | Reset password
*ManagementApi* | [**scim_create_user**](docs/ManagementApi.md#scim_create_user) | **POST** /v1/provisioning/scim/Users | Create SCIM user
*ManagementApi* | [**scim_delete_user**](docs/ManagementApi.md#scim_delete_user) | **DELETE** /v1/provisioning/scim/Users/{userId} | Delete SCIM user
*ManagementApi* | [**scim_get_resource_types**](docs/ManagementApi.md#scim_get_resource_types) | **GET** /v1/provisioning/scim/ResourceTypes | List supported SCIM resource types
*ManagementApi* | [**scim_get_schemas**](docs/ManagementApi.md#scim_get_schemas) | **GET** /v1/provisioning/scim/Schemas | List supported SCIM schemas
*ManagementApi* | [**scim_get_service_provider_config**](docs/ManagementApi.md#scim_get_service_provider_config) | **GET** /v1/provisioning/scim/ServiceProviderConfig | Get SCIM service provider configuration
*ManagementApi* | [**scim_get_user**](docs/ManagementApi.md#scim_get_user) | **GET** /v1/provisioning/scim/Users/{userId} | Get SCIM user
*ManagementApi* | [**scim_get_users**](docs/ManagementApi.md#scim_get_users) | **GET** /v1/provisioning/scim/Users | List SCIM users
*ManagementApi* | [**scim_patch_user**](docs/ManagementApi.md#scim_patch_user) | **PATCH** /v1/provisioning/scim/Users/{userId} | Update SCIM user attributes
*ManagementApi* | [**scim_replace_user_attributes**](docs/ManagementApi.md#scim_replace_user_attributes) | **PUT** /v1/provisioning/scim/Users/{userId} | Update SCIM user
*ManagementApi* | [**search_coupons_advanced_application_wide_without_total_count**](docs/ManagementApi.md#search_coupons_advanced_application_wide_without_total_count) | **POST** /v1/applications/{applicationId}/coupons_search_advanced/no_total | List coupons that match the given attributes (without total count)
*ManagementApi* | [**search_coupons_advanced_without_total_count**](docs/ManagementApi.md#search_coupons_advanced_without_total_count) | **POST** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons_search_advanced/no_total | List coupons that match the given attributes in campaign (without total count)
*ManagementApi* | [**transfer_loyalty_card**](docs/ManagementApi.md#transfer_loyalty_card) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId}/transfer | Transfer card data
*ManagementApi* | [**update_account_collection**](docs/ManagementApi.md#update_account_collection) | **PUT** /v1/collections/{collectionId} | Update account-level collection
*ManagementApi* | [**update_achievement**](docs/ManagementApi.md#update_achievement) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/achievements/{achievementId} | Update achievement
*ManagementApi* | [**update_additional_cost**](docs/ManagementApi.md#update_additional_cost) | **PUT** /v1/additional_costs/{additionalCostId} | Update additional cost
*ManagementApi* | [**update_attribute**](docs/ManagementApi.md#update_attribute) | **PUT** /v1/attributes/{attributeId} | Update custom attribute
*ManagementApi* | [**update_campaign**](docs/ManagementApi.md#update_campaign) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId} | Update campaign
*ManagementApi* | [**update_collection**](docs/ManagementApi.md#update_collection) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/collections/{collectionId} | Update campaign-level collection&#39;s description
*ManagementApi* | [**update_coupon**](docs/ManagementApi.md#update_coupon) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons/{couponId} | Update coupon
*ManagementApi* | [**update_coupon_batch**](docs/ManagementApi.md#update_coupon_batch) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/coupons | Update coupons
*ManagementApi* | [**update_loyalty_card**](docs/ManagementApi.md#update_loyalty_card) | **PUT** /v1/loyalty_programs/{loyaltyProgramId}/cards/{loyaltyCardId} | Update loyalty card status
*ManagementApi* | [**update_referral**](docs/ManagementApi.md#update_referral) | **PUT** /v1/applications/{applicationId}/campaigns/{campaignId}/referrals/{referralId} | Update referral
*ManagementApi* | [**update_role_v2**](docs/ManagementApi.md#update_role_v2) | **PUT** /v2/roles/{roleId} | Update role
*ManagementApi* | [**update_store**](docs/ManagementApi.md#update_store) | **PUT** /v1/applications/{applicationId}/stores/{storeId} | Update store
*ManagementApi* | [**update_user**](docs/ManagementApi.md#update_user) | **PUT** /v1/users/{userId} | Update user

## Documentation for models

- [APIError](docs/APIError.md)
- [AcceptCouponEffectProps](docs/AcceptCouponEffectProps.md)
- [AcceptReferralEffectProps](docs/AcceptReferralEffectProps.md)
- [AccessLogEntry](docs/AccessLogEntry.md)
- [Account](docs/Account.md)
- [AccountAdditionalCost](docs/AccountAdditionalCost.md)
- [AccountAnalytics](docs/AccountAnalytics.md)
- [AccountDashboardStatistic](docs/AccountDashboardStatistic.md)
- [AccountDashboardStatisticCampaigns](docs/AccountDashboardStatisticCampaigns.md)
- [AccountDashboardStatisticDiscount](docs/AccountDashboardStatisticDiscount.md)
- [AccountDashboardStatisticLoyaltyPoints](docs/AccountDashboardStatisticLoyaltyPoints.md)
- [AccountDashboardStatisticReferrals](docs/AccountDashboardStatisticReferrals.md)
- [AccountDashboardStatisticRevenue](docs/AccountDashboardStatisticRevenue.md)
- [AccountEntity](docs/AccountEntity.md)
- [AccountLimits](docs/AccountLimits.md)
- [Achievement](docs/Achievement.md)
- [AchievementAdditionalProperties](docs/AchievementAdditionalProperties.md)
- [AchievementBase](docs/AchievementBase.md)
- [AchievementProgress](docs/AchievementProgress.md)
- [AchievementProgressWithDefinition](docs/AchievementProgressWithDefinition.md)
- [AchievementStatusEntry](docs/AchievementStatusEntry.md)
- [AddFreeItemEffectProps](docs/AddFreeItemEffectProps.md)
- [AddItemCatalogAction](docs/AddItemCatalogAction.md)
- [AddLoyaltyPoints](docs/AddLoyaltyPoints.md)
- [AddLoyaltyPointsEffectProps](docs/AddLoyaltyPointsEffectProps.md)
- [AddToAudienceEffectProps](docs/AddToAudienceEffectProps.md)
- [AddedDeductedPointsNotificationPolicy](docs/AddedDeductedPointsNotificationPolicy.md)
- [AdditionalCampaignProperties](docs/AdditionalCampaignProperties.md)
- [AdditionalCost](docs/AdditionalCost.md)
- [AnalyticsDataPoint](docs/AnalyticsDataPoint.md)
- [AnalyticsDataPointWithTrend](docs/AnalyticsDataPointWithTrend.md)
- [AnalyticsDataPointWithTrendAndInfluencedRate](docs/AnalyticsDataPointWithTrendAndInfluencedRate.md)
- [AnalyticsDataPointWithTrendAndUplift](docs/AnalyticsDataPointWithTrendAndUplift.md)
- [AnalyticsProduct](docs/AnalyticsProduct.md)
- [AnalyticsSKU](docs/AnalyticsSKU.md)
- [Application](docs/Application.md)
- [ApplicationAPIKey](docs/ApplicationAPIKey.md)
- [ApplicationAnalyticsDataPoint](docs/ApplicationAnalyticsDataPoint.md)
- [ApplicationApiHealth](docs/ApplicationApiHealth.md)
- [ApplicationCIF](docs/ApplicationCIF.md)
- [ApplicationCIFExpression](docs/ApplicationCIFExpression.md)
- [ApplicationCIFReferences](docs/ApplicationCIFReferences.md)
- [ApplicationCampaignAnalytics](docs/ApplicationCampaignAnalytics.md)
- [ApplicationCampaignStats](docs/ApplicationCampaignStats.md)
- [ApplicationCustomer](docs/ApplicationCustomer.md)
- [ApplicationCustomerEntity](docs/ApplicationCustomerEntity.md)
- [ApplicationEntity](docs/ApplicationEntity.md)
- [ApplicationEvent](docs/ApplicationEvent.md)
- [ApplicationNotification](docs/ApplicationNotification.md)
- [ApplicationReferee](docs/ApplicationReferee.md)
- [ApplicationSession](docs/ApplicationSession.md)
- [ApplicationSessionEntity](docs/ApplicationSessionEntity.md)
- [ApplicationStoreEntity](docs/ApplicationStoreEntity.md)
- [AsyncCouponCreationResponse](docs/AsyncCouponCreationResponse.md)
- [AsyncCouponDeletionJobResponse](docs/AsyncCouponDeletionJobResponse.md)
- [Attribute](docs/Attribute.md)
- [AttributesMandatory](docs/AttributesMandatory.md)
- [AttributesSettings](docs/AttributesSettings.md)
- [Audience](docs/Audience.md)
- [AudienceAnalytics](docs/AudienceAnalytics.md)
- [AudienceCustomer](docs/AudienceCustomer.md)
- [AudienceIntegrationID](docs/AudienceIntegrationID.md)
- [AudienceMembership](docs/AudienceMembership.md)
- [AwardGiveawayEffectProps](docs/AwardGiveawayEffectProps.md)
- [BaseCampaign](docs/BaseCampaign.md)
- [BaseLoyaltyProgram](docs/BaseLoyaltyProgram.md)
- [BaseNotification](docs/BaseNotification.md)
- [BaseNotificationEntity](docs/BaseNotificationEntity.md)
- [BaseNotificationWebhook](docs/BaseNotificationWebhook.md)
- [BaseNotifications](docs/BaseNotifications.md)
- [BaseSamlConnection](docs/BaseSamlConnection.md)
- [Binding](docs/Binding.md)
- [BulkApplicationNotification](docs/BulkApplicationNotification.md)
- [BulkCampaignNotification](docs/BulkCampaignNotification.md)
- [BulkOperationOnCampaigns](docs/BulkOperationOnCampaigns.md)
- [Campaign](docs/Campaign.md)
- [CampaignActivationRequest](docs/CampaignActivationRequest.md)
- [CampaignAnalytics](docs/CampaignAnalytics.md)
- [CampaignBudget](docs/CampaignBudget.md)
- [CampaignCollection](docs/CampaignCollection.md)
- [CampaignCollectionEditedNotification](docs/CampaignCollectionEditedNotification.md)
- [CampaignCollectionWithoutPayload](docs/CampaignCollectionWithoutPayload.md)
- [CampaignCopy](docs/CampaignCopy.md)
- [CampaignCreatedNotification](docs/CampaignCreatedNotification.md)
- [CampaignDeletedNotification](docs/CampaignDeletedNotification.md)
- [CampaignDetail](docs/CampaignDetail.md)
- [CampaignEditedNotification](docs/CampaignEditedNotification.md)
- [CampaignEntity](docs/CampaignEntity.md)
- [CampaignEvaluationGroup](docs/CampaignEvaluationGroup.md)
- [CampaignEvaluationPosition](docs/CampaignEvaluationPosition.md)
- [CampaignEvaluationTreeChangedNotification](docs/CampaignEvaluationTreeChangedNotification.md)
- [CampaignGroup](docs/CampaignGroup.md)
- [CampaignGroupEntity](docs/CampaignGroupEntity.md)
- [CampaignNotification](docs/CampaignNotification.md)
- [CampaignNotificationPolicy](docs/CampaignNotificationPolicy.md)
- [CampaignRulesetChangedNotification](docs/CampaignRulesetChangedNotification.md)
- [CampaignSearch](docs/CampaignSearch.md)
- [CampaignSet](docs/CampaignSet.md)
- [CampaignSetBranchNode](docs/CampaignSetBranchNode.md)
- [CampaignSetLeafNode](docs/CampaignSetLeafNode.md)
- [CampaignSetNode](docs/CampaignSetNode.md)
- [CampaignStateChangedNotification](docs/CampaignStateChangedNotification.md)
- [CampaignStoreBudget](docs/CampaignStoreBudget.md)
- [CampaignStoreBudgetLimitConfig](docs/CampaignStoreBudgetLimitConfig.md)
- [CampaignTemplate](docs/CampaignTemplate.md)
- [CampaignTemplateCollection](docs/CampaignTemplateCollection.md)
- [CampaignTemplateCouponReservationSettings](docs/CampaignTemplateCouponReservationSettings.md)
- [CampaignTemplateParams](docs/CampaignTemplateParams.md)
- [CampaignVersions](docs/CampaignVersions.md)
- [CardAddedDeductedPointsNotificationPolicy](docs/CardAddedDeductedPointsNotificationPolicy.md)
- [CardExpiringPointsNotificationPolicy](docs/CardExpiringPointsNotificationPolicy.md)
- [CardExpiringPointsNotificationTrigger](docs/CardExpiringPointsNotificationTrigger.md)
- [CardLedgerPointsEntryIntegrationAPI](docs/CardLedgerPointsEntryIntegrationAPI.md)
- [CardLedgerTransactionLogEntry](docs/CardLedgerTransactionLogEntry.md)
- [CardLedgerTransactionLogEntryIntegrationAPI](docs/CardLedgerTransactionLogEntryIntegrationAPI.md)
- [CartItem](docs/CartItem.md)
- [Catalog](docs/Catalog.md)
- [CatalogAction](docs/CatalogAction.md)
- [CatalogActionFilter](docs/CatalogActionFilter.md)
- [CatalogItem](docs/CatalogItem.md)
- [CatalogSyncRequest](docs/CatalogSyncRequest.md)
- [CatalogsStrikethroughNotificationPolicy](docs/CatalogsStrikethroughNotificationPolicy.md)
- [Change](docs/Change.md)
- [ChangeLoyaltyTierLevelEffectProps](docs/ChangeLoyaltyTierLevelEffectProps.md)
- [ChangeProfilePassword](docs/ChangeProfilePassword.md)
- [CodeGeneratorSettings](docs/CodeGeneratorSettings.md)
- [Collection](docs/Collection.md)
- [CollectionItem](docs/CollectionItem.md)
- [CollectionWithoutPayload](docs/CollectionWithoutPayload.md)
- [Coupon](docs/Coupon.md)
- [CouponConstraints](docs/CouponConstraints.md)
- [CouponCreatedEffectProps](docs/CouponCreatedEffectProps.md)
- [CouponCreationJob](docs/CouponCreationJob.md)
- [CouponDeletionFilters](docs/CouponDeletionFilters.md)
- [CouponDeletionJob](docs/CouponDeletionJob.md)
- [CouponLimitConfigs](docs/CouponLimitConfigs.md)
- [CouponRejectionReason](docs/CouponRejectionReason.md)
- [CouponReservations](docs/CouponReservations.md)
- [CouponSearch](docs/CouponSearch.md)
- [CouponValue](docs/CouponValue.md)
- [CouponsNotificationPolicy](docs/CouponsNotificationPolicy.md)
- [CreateAchievement](docs/CreateAchievement.md)
- [CreateApplicationAPIKey](docs/CreateApplicationAPIKey.md)
- [CreateManagementKey](docs/CreateManagementKey.md)
- [CreateTemplateCampaign](docs/CreateTemplateCampaign.md)
- [CreateTemplateCampaignResponse](docs/CreateTemplateCampaignResponse.md)
- [CustomEffect](docs/CustomEffect.md)
- [CustomEffectProps](docs/CustomEffectProps.md)
- [CustomerActivityReport](docs/CustomerActivityReport.md)
- [CustomerAnalytics](docs/CustomerAnalytics.md)
- [CustomerInventory](docs/CustomerInventory.md)
- [CustomerProfile](docs/CustomerProfile.md)
- [CustomerProfileAudienceRequest](docs/CustomerProfileAudienceRequest.md)
- [CustomerProfileAudienceRequestItem](docs/CustomerProfileAudienceRequestItem.md)
- [CustomerProfileIntegrationRequestV2](docs/CustomerProfileIntegrationRequestV2.md)
- [CustomerProfileIntegrationResponseV2](docs/CustomerProfileIntegrationResponseV2.md)
- [CustomerProfileSearchQuery](docs/CustomerProfileSearchQuery.md)
- [CustomerProfileUpdateV2Response](docs/CustomerProfileUpdateV2Response.md)
- [CustomerSession](docs/CustomerSession.md)
- [CustomerSessionV2](docs/CustomerSessionV2.md)
- [DeductLoyaltyPoints](docs/DeductLoyaltyPoints.md)
- [DeductLoyaltyPointsEffectProps](docs/DeductLoyaltyPointsEffectProps.md)
- [DeleteUserRequest](docs/DeleteUserRequest.md)
- [Effect](docs/Effect.md)
- [EffectEntity](docs/EffectEntity.md)
- [EmailEntity](docs/EmailEntity.md)
- [Endpoint](docs/Endpoint.md)
- [Entity](docs/Entity.md)
- [EntityWithTalangVisibleID](docs/EntityWithTalangVisibleID.md)
- [Environment](docs/Environment.md)
- [ErrorEffectProps](docs/ErrorEffectProps.md)
- [ErrorResponse](docs/ErrorResponse.md)
- [ErrorResponseWithStatus](docs/ErrorResponseWithStatus.md)
- [ErrorSource](docs/ErrorSource.md)
- [EvaluableCampaignIds](docs/EvaluableCampaignIds.md)
- [Event](docs/Event.md)
- [EventType](docs/EventType.md)
- [EventV2](docs/EventV2.md)
- [ExpiringCouponsNotificationPolicy](docs/ExpiringCouponsNotificationPolicy.md)
- [ExpiringCouponsNotificationTrigger](docs/ExpiringCouponsNotificationTrigger.md)
- [ExpiringPointsNotificationPolicy](docs/ExpiringPointsNotificationPolicy.md)
- [ExpiringPointsNotificationTrigger](docs/ExpiringPointsNotificationTrigger.md)
- [Export](docs/Export.md)
- [FeatureFlag](docs/FeatureFlag.md)
- [FeaturesFeed](docs/FeaturesFeed.md)
- [FuncArgDef](docs/FuncArgDef.md)
- [FunctionDef](docs/FunctionDef.md)
- [GenerateCampaignDescription](docs/GenerateCampaignDescription.md)
- [GenerateCampaignTags](docs/GenerateCampaignTags.md)
- [GenerateItemFilterDescription](docs/GenerateItemFilterDescription.md)
- [GenerateLoyaltyCard](docs/GenerateLoyaltyCard.md)
- [GenerateRuleTitle](docs/GenerateRuleTitle.md)
- [GenerateRuleTitleRule](docs/GenerateRuleTitleRule.md)
- [GetIntegrationCouponRequest](docs/GetIntegrationCouponRequest.md)
- [Giveaway](docs/Giveaway.md)
- [GiveawaysPool](docs/GiveawaysPool.md)
- [HiddenConditionsEffects](docs/HiddenConditionsEffects.md)
- [IdentifiableEntity](docs/IdentifiableEntity.md)
- [ImportEntity](docs/ImportEntity.md)
- [IncreaseAchievementProgressEffectProps](docs/IncreaseAchievementProgressEffectProps.md)
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
- [InlineResponse20031](docs/InlineResponse20031.md)
- [InlineResponse20032](docs/InlineResponse20032.md)
- [InlineResponse20033](docs/InlineResponse20033.md)
- [InlineResponse20034](docs/InlineResponse20034.md)
- [InlineResponse20035](docs/InlineResponse20035.md)
- [InlineResponse20036](docs/InlineResponse20036.md)
- [InlineResponse20037](docs/InlineResponse20037.md)
- [InlineResponse20038](docs/InlineResponse20038.md)
- [InlineResponse20039](docs/InlineResponse20039.md)
- [InlineResponse2004](docs/InlineResponse2004.md)
- [InlineResponse20040](docs/InlineResponse20040.md)
- [InlineResponse20041](docs/InlineResponse20041.md)
- [InlineResponse20042](docs/InlineResponse20042.md)
- [InlineResponse20043](docs/InlineResponse20043.md)
- [InlineResponse20044](docs/InlineResponse20044.md)
- [InlineResponse20045](docs/InlineResponse20045.md)
- [InlineResponse20046](docs/InlineResponse20046.md)
- [InlineResponse20047](docs/InlineResponse20047.md)
- [InlineResponse20048](docs/InlineResponse20048.md)
- [InlineResponse20049](docs/InlineResponse20049.md)
- [InlineResponse2005](docs/InlineResponse2005.md)
- [InlineResponse2006](docs/InlineResponse2006.md)
- [InlineResponse2007](docs/InlineResponse2007.md)
- [InlineResponse2008](docs/InlineResponse2008.md)
- [InlineResponse2009](docs/InlineResponse2009.md)
- [InlineResponse201](docs/InlineResponse201.md)
- [IntegrationCoupon](docs/IntegrationCoupon.md)
- [IntegrationCustomerSessionResponse](docs/IntegrationCustomerSessionResponse.md)
- [IntegrationEntity](docs/IntegrationEntity.md)
- [IntegrationEvent](docs/IntegrationEvent.md)
- [IntegrationEventV2Request](docs/IntegrationEventV2Request.md)
- [IntegrationProfileEntity](docs/IntegrationProfileEntity.md)
- [IntegrationRequest](docs/IntegrationRequest.md)
- [IntegrationState](docs/IntegrationState.md)
- [IntegrationStateV2](docs/IntegrationStateV2.md)
- [IntegrationStoreEntity](docs/IntegrationStoreEntity.md)
- [InventoryCoupon](docs/InventoryCoupon.md)
- [InventoryReferral](docs/InventoryReferral.md)
- [ItemAttribute](docs/ItemAttribute.md)
- [LedgerEntry](docs/LedgerEntry.md)
- [LedgerInfo](docs/LedgerInfo.md)
- [LedgerPointsEntryIntegrationAPI](docs/LedgerPointsEntryIntegrationAPI.md)
- [LedgerTransactionLogEntryIntegrationAPI](docs/LedgerTransactionLogEntryIntegrationAPI.md)
- [LibraryAttribute](docs/LibraryAttribute.md)
- [LimitConfig](docs/LimitConfig.md)
- [LimitCounter](docs/LimitCounter.md)
- [ListCampaignStoreBudgets](docs/ListCampaignStoreBudgets.md)
- [ListCampaignStoreBudgetsStore](docs/ListCampaignStoreBudgetsStore.md)
- [LoginParams](docs/LoginParams.md)
- [Loyalty](docs/Loyalty.md)
- [LoyaltyBalance](docs/LoyaltyBalance.md)
- [LoyaltyBalanceWithTier](docs/LoyaltyBalanceWithTier.md)
- [LoyaltyBalances](docs/LoyaltyBalances.md)
- [LoyaltyBalancesWithTiers](docs/LoyaltyBalancesWithTiers.md)
- [LoyaltyCard](docs/LoyaltyCard.md)
- [LoyaltyCardBalances](docs/LoyaltyCardBalances.md)
- [LoyaltyCardBatch](docs/LoyaltyCardBatch.md)
- [LoyaltyCardBatchResponse](docs/LoyaltyCardBatchResponse.md)
- [LoyaltyCardProfileRegistration](docs/LoyaltyCardProfileRegistration.md)
- [LoyaltyCardRegistration](docs/LoyaltyCardRegistration.md)
- [LoyaltyDashboardData](docs/LoyaltyDashboardData.md)
- [LoyaltyDashboardPointsBreakdown](docs/LoyaltyDashboardPointsBreakdown.md)
- [LoyaltyLedger](docs/LoyaltyLedger.md)
- [LoyaltyLedgerEntry](docs/LoyaltyLedgerEntry.md)
- [LoyaltyLedgerEntryFlags](docs/LoyaltyLedgerEntryFlags.md)
- [LoyaltyLedgerTransactions](docs/LoyaltyLedgerTransactions.md)
- [LoyaltyMembership](docs/LoyaltyMembership.md)
- [LoyaltyProgram](docs/LoyaltyProgram.md)
- [LoyaltyProgramBalance](docs/LoyaltyProgramBalance.md)
- [LoyaltyProgramEntity](docs/LoyaltyProgramEntity.md)
- [LoyaltyProgramLedgers](docs/LoyaltyProgramLedgers.md)
- [LoyaltyProgramTransaction](docs/LoyaltyProgramTransaction.md)
- [LoyaltySubLedger](docs/LoyaltySubLedger.md)
- [LoyaltyTier](docs/LoyaltyTier.md)
- [ManagementKey](docs/ManagementKey.md)
- [ManagerConfig](docs/ManagerConfig.md)
- [MessageLogEntries](docs/MessageLogEntries.md)
- [MessageLogEntry](docs/MessageLogEntry.md)
- [MessageLogRequest](docs/MessageLogRequest.md)
- [MessageLogResponse](docs/MessageLogResponse.md)
- [MessageTest](docs/MessageTest.md)
- [Meta](docs/Meta.md)
- [ModelImport](docs/ModelImport.md)
- [ModelReturn](docs/ModelReturn.md)
- [MultiApplicationEntity](docs/MultiApplicationEntity.md)
- [MultipleAttribute](docs/MultipleAttribute.md)
- [MultipleAudiences](docs/MultipleAudiences.md)
- [MultipleAudiencesItem](docs/MultipleAudiencesItem.md)
- [MultipleCustomerProfileIntegrationRequest](docs/MultipleCustomerProfileIntegrationRequest.md)
- [MultipleCustomerProfileIntegrationRequestItem](docs/MultipleCustomerProfileIntegrationRequestItem.md)
- [MultipleCustomerProfileIntegrationResponseV2](docs/MultipleCustomerProfileIntegrationResponseV2.md)
- [MultipleNewAttribute](docs/MultipleNewAttribute.md)
- [MultipleNewAudiences](docs/MultipleNewAudiences.md)
- [MutableEntity](docs/MutableEntity.md)
- [NewAccount](docs/NewAccount.md)
- [NewAccountSignUp](docs/NewAccountSignUp.md)
- [NewAdditionalCost](docs/NewAdditionalCost.md)
- [NewAppWideCouponDeletionJob](docs/NewAppWideCouponDeletionJob.md)
- [NewApplication](docs/NewApplication.md)
- [NewApplicationAPIKey](docs/NewApplicationAPIKey.md)
- [NewApplicationCIF](docs/NewApplicationCIF.md)
- [NewApplicationCIFExpression](docs/NewApplicationCIFExpression.md)
- [NewAttribute](docs/NewAttribute.md)
- [NewAudience](docs/NewAudience.md)
- [NewBaseNotification](docs/NewBaseNotification.md)
- [NewCampaign](docs/NewCampaign.md)
- [NewCampaignCollection](docs/NewCampaignCollection.md)
- [NewCampaignEvaluationGroup](docs/NewCampaignEvaluationGroup.md)
- [NewCampaignGroup](docs/NewCampaignGroup.md)
- [NewCampaignSet](docs/NewCampaignSet.md)
- [NewCampaignStoreBudget](docs/NewCampaignStoreBudget.md)
- [NewCampaignStoreBudgetStoreLimit](docs/NewCampaignStoreBudgetStoreLimit.md)
- [NewCampaignTemplate](docs/NewCampaignTemplate.md)
- [NewCatalog](docs/NewCatalog.md)
- [NewCollection](docs/NewCollection.md)
- [NewCouponCreationJob](docs/NewCouponCreationJob.md)
- [NewCouponDeletionJob](docs/NewCouponDeletionJob.md)
- [NewCoupons](docs/NewCoupons.md)
- [NewCouponsForMultipleRecipients](docs/NewCouponsForMultipleRecipients.md)
- [NewCustomEffect](docs/NewCustomEffect.md)
- [NewCustomerProfile](docs/NewCustomerProfile.md)
- [NewCustomerSession](docs/NewCustomerSession.md)
- [NewCustomerSessionV2](docs/NewCustomerSessionV2.md)
- [NewEvent](docs/NewEvent.md)
- [NewEventType](docs/NewEventType.md)
- [NewExternalInvitation](docs/NewExternalInvitation.md)
- [NewGiveawaysPool](docs/NewGiveawaysPool.md)
- [NewInternalAudience](docs/NewInternalAudience.md)
- [NewInvitation](docs/NewInvitation.md)
- [NewInviteEmail](docs/NewInviteEmail.md)
- [NewLoyaltyProgram](docs/NewLoyaltyProgram.md)
- [NewLoyaltyTier](docs/NewLoyaltyTier.md)
- [NewManagementKey](docs/NewManagementKey.md)
- [NewMessageTest](docs/NewMessageTest.md)
- [NewMultipleAudiencesItem](docs/NewMultipleAudiencesItem.md)
- [NewNotificationWebhook](docs/NewNotificationWebhook.md)
- [NewOutgoingIntegrationWebhook](docs/NewOutgoingIntegrationWebhook.md)
- [NewPassword](docs/NewPassword.md)
- [NewPasswordEmail](docs/NewPasswordEmail.md)
- [NewPicklist](docs/NewPicklist.md)
- [NewReferral](docs/NewReferral.md)
- [NewReferralsForMultipleAdvocates](docs/NewReferralsForMultipleAdvocates.md)
- [NewReturn](docs/NewReturn.md)
- [NewRevisionVersion](docs/NewRevisionVersion.md)
- [NewRole](docs/NewRole.md)
- [NewRoleV2](docs/NewRoleV2.md)
- [NewRuleset](docs/NewRuleset.md)
- [NewSamlConnection](docs/NewSamlConnection.md)
- [NewStore](docs/NewStore.md)
- [NewTemplateDef](docs/NewTemplateDef.md)
- [NewUser](docs/NewUser.md)
- [NewWebhook](docs/NewWebhook.md)
- [Notification](docs/Notification.md)
- [NotificationActivation](docs/NotificationActivation.md)
- [NotificationListItem](docs/NotificationListItem.md)
- [OktaEvent](docs/OktaEvent.md)
- [OktaEventPayload](docs/OktaEventPayload.md)
- [OktaEventPayloadData](docs/OktaEventPayloadData.md)
- [OktaEventTarget](docs/OktaEventTarget.md)
- [OneTimeCode](docs/OneTimeCode.md)
- [OutgoingIntegrationBrazePolicy](docs/OutgoingIntegrationBrazePolicy.md)
- [OutgoingIntegrationCleverTapPolicy](docs/OutgoingIntegrationCleverTapPolicy.md)
- [OutgoingIntegrationConfiguration](docs/OutgoingIntegrationConfiguration.md)
- [OutgoingIntegrationIterablePolicy](docs/OutgoingIntegrationIterablePolicy.md)
- [OutgoingIntegrationMoEngagePolicy](docs/OutgoingIntegrationMoEngagePolicy.md)
- [OutgoingIntegrationTemplate](docs/OutgoingIntegrationTemplate.md)
- [OutgoingIntegrationTemplateWithConfigurationDetails](docs/OutgoingIntegrationTemplateWithConfigurationDetails.md)
- [OutgoingIntegrationTemplates](docs/OutgoingIntegrationTemplates.md)
- [OutgoingIntegrationType](docs/OutgoingIntegrationType.md)
- [OutgoingIntegrationTypes](docs/OutgoingIntegrationTypes.md)
- [PatchItemCatalogAction](docs/PatchItemCatalogAction.md)
- [PatchManyItemsCatalogAction](docs/PatchManyItemsCatalogAction.md)
- [PendingPointsNotificationPolicy](docs/PendingPointsNotificationPolicy.md)
- [Picklist](docs/Picklist.md)
- [Product](docs/Product.md)
- [ProductSearchMatch](docs/ProductSearchMatch.md)
- [ProductUnitAnalytics](docs/ProductUnitAnalytics.md)
- [ProductUnitAnalyticsDataPoint](docs/ProductUnitAnalyticsDataPoint.md)
- [ProductUnitAnalyticsTotals](docs/ProductUnitAnalyticsTotals.md)
- [ProfileAudiencesChanges](docs/ProfileAudiencesChanges.md)
- [ProjectedTier](docs/ProjectedTier.md)
- [RedeemReferralEffectProps](docs/RedeemReferralEffectProps.md)
- [Referral](docs/Referral.md)
- [ReferralConstraints](docs/ReferralConstraints.md)
- [ReferralCreatedEffectProps](docs/ReferralCreatedEffectProps.md)
- [ReferralRejectionReason](docs/ReferralRejectionReason.md)
- [RejectCouponEffectProps](docs/RejectCouponEffectProps.md)
- [RejectReferralEffectProps](docs/RejectReferralEffectProps.md)
- [RemoveFromAudienceEffectProps](docs/RemoveFromAudienceEffectProps.md)
- [RemoveItemCatalogAction](docs/RemoveItemCatalogAction.md)
- [RemoveManyItemsCatalogAction](docs/RemoveManyItemsCatalogAction.md)
- [ReopenSessionResponse](docs/ReopenSessionResponse.md)
- [ReserveCouponEffectProps](docs/ReserveCouponEffectProps.md)
- [ReturnIntegrationRequest](docs/ReturnIntegrationRequest.md)
- [ReturnedCartItem](docs/ReturnedCartItem.md)
- [Revision](docs/Revision.md)
- [RevisionActivation](docs/RevisionActivation.md)
- [RevisionActivationRequest](docs/RevisionActivationRequest.md)
- [RevisionVersion](docs/RevisionVersion.md)
- [Role](docs/Role.md)
- [RoleAssign](docs/RoleAssign.md)
- [RoleMembership](docs/RoleMembership.md)
- [RoleV2](docs/RoleV2.md)
- [RoleV2ApplicationDetails](docs/RoleV2ApplicationDetails.md)
- [RoleV2Base](docs/RoleV2Base.md)
- [RoleV2PermissionSet](docs/RoleV2PermissionSet.md)
- [RoleV2Permissions](docs/RoleV2Permissions.md)
- [RoleV2RolesGroup](docs/RoleV2RolesGroup.md)
- [RollbackAddedLoyaltyPointsEffectProps](docs/RollbackAddedLoyaltyPointsEffectProps.md)
- [RollbackCouponEffectProps](docs/RollbackCouponEffectProps.md)
- [RollbackDeductedLoyaltyPointsEffectProps](docs/RollbackDeductedLoyaltyPointsEffectProps.md)
- [RollbackDiscountEffectProps](docs/RollbackDiscountEffectProps.md)
- [RollbackIncreasedAchievementProgressEffectProps](docs/RollbackIncreasedAchievementProgressEffectProps.md)
- [RollbackReferralEffectProps](docs/RollbackReferralEffectProps.md)
- [Rule](docs/Rule.md)
- [RuleFailureReason](docs/RuleFailureReason.md)
- [Ruleset](docs/Ruleset.md)
- [SSOConfig](docs/SSOConfig.md)
- [SamlConnection](docs/SamlConnection.md)
- [SamlConnectionInternal](docs/SamlConnectionInternal.md)
- [SamlConnectionMetadata](docs/SamlConnectionMetadata.md)
- [SamlLoginEndpoint](docs/SamlLoginEndpoint.md)
- [ScimBaseUser](docs/ScimBaseUser.md)
- [ScimBaseUserName](docs/ScimBaseUserName.md)
- [ScimNewUser](docs/ScimNewUser.md)
- [ScimPatchOperation](docs/ScimPatchOperation.md)
- [ScimPatchRequest](docs/ScimPatchRequest.md)
- [ScimResource](docs/ScimResource.md)
- [ScimResourceTypesListResponse](docs/ScimResourceTypesListResponse.md)
- [ScimSchemaResource](docs/ScimSchemaResource.md)
- [ScimSchemasListResponse](docs/ScimSchemasListResponse.md)
- [ScimServiceProviderConfigResponse](docs/ScimServiceProviderConfigResponse.md)
- [ScimServiceProviderConfigResponseBulk](docs/ScimServiceProviderConfigResponseBulk.md)
- [ScimServiceProviderConfigResponseChangePassword](docs/ScimServiceProviderConfigResponseChangePassword.md)
- [ScimServiceProviderConfigResponseFilter](docs/ScimServiceProviderConfigResponseFilter.md)
- [ScimServiceProviderConfigResponsePatch](docs/ScimServiceProviderConfigResponsePatch.md)
- [ScimServiceProviderConfigResponseSort](docs/ScimServiceProviderConfigResponseSort.md)
- [ScimUser](docs/ScimUser.md)
- [ScimUsersListResponse](docs/ScimUsersListResponse.md)
- [Session](docs/Session.md)
- [SetDiscountEffectProps](docs/SetDiscountEffectProps.md)
- [SetDiscountPerAdditionalCostEffectProps](docs/SetDiscountPerAdditionalCostEffectProps.md)
- [SetDiscountPerAdditionalCostPerItemEffectProps](docs/SetDiscountPerAdditionalCostPerItemEffectProps.md)
- [SetDiscountPerItemEffectProps](docs/SetDiscountPerItemEffectProps.md)
- [ShowBundleMetadataEffectProps](docs/ShowBundleMetadataEffectProps.md)
- [ShowNotificationEffectProps](docs/ShowNotificationEffectProps.md)
- [SkuUnitAnalytics](docs/SkuUnitAnalytics.md)
- [SkuUnitAnalyticsDataPoint](docs/SkuUnitAnalyticsDataPoint.md)
- [SlotDef](docs/SlotDef.md)
- [Store](docs/Store.md)
- [StrikethroughChangedItem](docs/StrikethroughChangedItem.md)
- [StrikethroughCustomEffectPerItemProps](docs/StrikethroughCustomEffectPerItemProps.md)
- [StrikethroughDebugResponse](docs/StrikethroughDebugResponse.md)
- [StrikethroughEffect](docs/StrikethroughEffect.md)
- [StrikethroughLabelingNotification](docs/StrikethroughLabelingNotification.md)
- [StrikethroughSetDiscountPerItemEffectProps](docs/StrikethroughSetDiscountPerItemEffectProps.md)
- [StrikethroughTrigger](docs/StrikethroughTrigger.md)
- [SummaryCampaignStoreBudget](docs/SummaryCampaignStoreBudget.md)
- [TalangAttribute](docs/TalangAttribute.md)
- [TalangAttributeVisibility](docs/TalangAttributeVisibility.md)
- [TemplateArgDef](docs/TemplateArgDef.md)
- [TemplateDef](docs/TemplateDef.md)
- [TemplateLimitConfig](docs/TemplateLimitConfig.md)
- [Tier](docs/Tier.md)
- [TierDowngradeNotificationPolicy](docs/TierDowngradeNotificationPolicy.md)
- [TierUpgradeNotificationPolicy](docs/TierUpgradeNotificationPolicy.md)
- [TierWillDowngradeNotificationPolicy](docs/TierWillDowngradeNotificationPolicy.md)
- [TierWillDowngradeNotificationTrigger](docs/TierWillDowngradeNotificationTrigger.md)
- [TimePoint](docs/TimePoint.md)
- [TrackEventV2Response](docs/TrackEventV2Response.md)
- [TransferLoyaltyCard](docs/TransferLoyaltyCard.md)
- [TriggerWebhookEffectProps](docs/TriggerWebhookEffectProps.md)
- [TwoFAConfig](docs/TwoFAConfig.md)
- [UpdateAccount](docs/UpdateAccount.md)
- [UpdateAchievement](docs/UpdateAchievement.md)
- [UpdateApplication](docs/UpdateApplication.md)
- [UpdateApplicationAPIKey](docs/UpdateApplicationAPIKey.md)
- [UpdateApplicationCIF](docs/UpdateApplicationCIF.md)
- [UpdateAttributeEffectProps](docs/UpdateAttributeEffectProps.md)
- [UpdateAudience](docs/UpdateAudience.md)
- [UpdateCampaign](docs/UpdateCampaign.md)
- [UpdateCampaignCollection](docs/UpdateCampaignCollection.md)
- [UpdateCampaignEvaluationGroup](docs/UpdateCampaignEvaluationGroup.md)
- [UpdateCampaignGroup](docs/UpdateCampaignGroup.md)
- [UpdateCampaignTemplate](docs/UpdateCampaignTemplate.md)
- [UpdateCatalog](docs/UpdateCatalog.md)
- [UpdateCollection](docs/UpdateCollection.md)
- [UpdateCoupon](docs/UpdateCoupon.md)
- [UpdateCouponBatch](docs/UpdateCouponBatch.md)
- [UpdateLoyaltyCard](docs/UpdateLoyaltyCard.md)
- [UpdateLoyaltyProgram](docs/UpdateLoyaltyProgram.md)
- [UpdateLoyaltyProgramTier](docs/UpdateLoyaltyProgramTier.md)
- [UpdatePicklist](docs/UpdatePicklist.md)
- [UpdateReferral](docs/UpdateReferral.md)
- [UpdateReferralBatch](docs/UpdateReferralBatch.md)
- [UpdateRole](docs/UpdateRole.md)
- [UpdateStore](docs/UpdateStore.md)
- [UpdateUser](docs/UpdateUser.md)
- [User](docs/User.md)
- [UserEntity](docs/UserEntity.md)
- [ValueMap](docs/ValueMap.md)
- [Webhook](docs/Webhook.md)
- [WebhookActivationLogEntry](docs/WebhookActivationLogEntry.md)
- [WebhookLogEntry](docs/WebhookLogEntry.md)
- [WebhookWithOutgoingIntegrationDetails](docs/WebhookWithOutgoingIntegrationDetails.md)
- [WillAwardGiveawayEffectProps](docs/WillAwardGiveawayEffectProps.md)

## Authorization

Authentication schemes defined for the API:

### api_key_v1

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

### management_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

### manager_auth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

