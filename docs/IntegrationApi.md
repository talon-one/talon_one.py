# talon_one.IntegrationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_reservation**](IntegrationApi.md#create_coupon_reservation) | **POST** /v1/coupon_reservations/{couponValue} | Create a new coupon reservation
[**create_referral**](IntegrationApi.md#create_referral) | **POST** /v1/referrals | Create a referral code for an advocate
[**delete_coupon_reservation**](IntegrationApi.md#delete_coupon_reservation) | **DELETE** /v1/coupon_reservations/{couponValue} | Delete coupon reservations
[**delete_customer_data**](IntegrationApi.md#delete_customer_data) | **DELETE** /v1/customer_data/{integrationId} | Delete the personal data of a customer.
[**get_customer_inventory**](IntegrationApi.md#get_customer_inventory) | **GET** /v1/customer_profiles/{integrationId}/inventory | Get an inventory of all data associated with a specific customer profile.
[**get_reserved_coupons**](IntegrationApi.md#get_reserved_coupons) | **GET** /v1/coupon_reservations/coupons/{integrationId} | Get all valid reserved coupons
[**get_reserved_customers**](IntegrationApi.md#get_reserved_customers) | **GET** /v1/coupon_reservations/customerprofiles/{couponValue} | Get the users that have this coupon reserved
[**track_event**](IntegrationApi.md#track_event) | **POST** /v1/events | Track an Event
[**update_customer_profile**](IntegrationApi.md#update_customer_profile) | **PUT** /v1/customer_profiles/{integrationId} | Update a Customer Profile
[**update_customer_session**](IntegrationApi.md#update_customer_session) | **PUT** /v1/customer_sessions/{customerSessionId} | Update a Customer Session


# **create_coupon_reservation**
> Coupon create_coupon_reservation(coupon_value, body)

Create a new coupon reservation

Creates a coupon reservation for all passed customer profiles on this couponID 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
coupon_value = 'coupon_value_example' # str | The value of a coupon
body = talon_one.CouponReservations() # CouponReservations | 

try:
    # Create a new coupon reservation
    api_response = api_instance.create_coupon_reservation(coupon_value, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_coupon_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_value** | **str**| The value of a coupon | 
 **body** | [**CouponReservations**](CouponReservations.md)|  | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_referral**
> Referral create_referral(body)

Create a referral code for an advocate

Creates a referral code for an advocate. The code will be valid for the referral campaign for which is created, indicated in the `campaignId` parameter, and will be associated with the profile specified in the `advocateProfileIntegrationId` parameter as the advocate's profile. 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
body = talon_one.NewReferral() # NewReferral | 

try:
    # Create a referral code for an advocate
    api_response = api_instance.create_referral(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_referral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewReferral**](NewReferral.md)|  | 

### Return type

[**Referral**](Referral.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_reservation**
> delete_coupon_reservation(coupon_value, body)

Delete coupon reservations

Removes all passed customer profiles reservation from this coupon 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
coupon_value = 'coupon_value_example' # str | The value of a coupon
body = talon_one.CouponReservations() # CouponReservations | 

try:
    # Delete coupon reservations
    api_instance.delete_coupon_reservation(coupon_value, body)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_coupon_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_value** | **str**| The value of a coupon | 
 **body** | [**CouponReservations**](CouponReservations.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_data**
> delete_customer_data(integration_id)

Delete the personal data of a customer.

Delete all attributes on the customer profile and on entities that reference that customer profile. 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.

try:
    # Delete the personal data of a customer.
    api_instance.delete_customer_data(integration_id)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_customer_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile, must be unique within the account. | 

### Return type

void (empty response body)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_inventory**
> CustomerInventory get_customer_inventory(integration_id, profile=profile, referrals=referrals)

Get an inventory of all data associated with a specific customer profile.

Get information regarding entities referencing this customer profile's integrationId. Currently we support customer profile information and referral codes. In the future, this will be expanded with coupon codes and loyalty points.

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.
profile = NULL # object | optional flag to decide if you would like customer profile information in the response (optional)
referrals = NULL # object | optional flag to decide if you would like referral information in the response (optional)

try:
    # Get an inventory of all data associated with a specific customer profile.
    api_response = api_instance.get_customer_inventory(integration_id, profile=profile, referrals=referrals)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_customer_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile, must be unique within the account. | 
 **profile** | [**object**](.md)| optional flag to decide if you would like customer profile information in the response | [optional] 
 **referrals** | [**object**](.md)| optional flag to decide if you would like referral information in the response | [optional] 

### Return type

[**CustomerInventory**](CustomerInventory.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reserved_coupons**
> InlineResponse2001 get_reserved_coupons(integration_id)

Get all valid reserved coupons

Returns all coupons this user is subscribed to that are valid and usable 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.

try:
    # Get all valid reserved coupons
    api_response = api_instance.get_reserved_coupons(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_reserved_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile, must be unique within the account. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reserved_customers**
> InlineResponse200 get_reserved_customers(coupon_value)

Get the users that have this coupon reserved

Returns all users that have this coupon marked as reserved 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
coupon_value = 'coupon_value_example' # str | The value of a coupon

try:
    # Get the users that have this coupon reserved
    api_response = api_instance.get_reserved_customers(coupon_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_reserved_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_value** | **str**| The value of a coupon | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_event**
> IntegrationState track_event(body)

Track an Event

Records an arbitrary event in a customer session. For example, an integration might record an event when a user updates their payment information.  The `sessionId` body parameter is required, an event is always part of a session. Much like updating a customer session, if either the profile or the session do not exist, a new empty one will be created. Note that if the specified session already exists, it must belong to the same `profileId` or an error will be returned.  As with customer sessions, you can use an empty string for `profileId` to indicate that this is an anonymous session.  Updating a customer profile will return a response with the full integration state. This includes the current state of the customer profile, the customer session, the event that was recorded, and an array of effects that took place. 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
body = talon_one.NewEvent() # NewEvent | 

try:
    # Track an Event
    api_response = api_instance.track_event(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->track_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewEvent**](NewEvent.md)|  | 

### Return type

[**IntegrationState**](IntegrationState.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_profile**
> IntegrationState update_customer_profile(integration_id, body)

Update a Customer Profile

Update (or create) a [Customer Profile][]. This profile information can then be matched and/or updated by campaign [Rules][].  The `integrationId` may be any identifier that will remain stable for the customer. For example, you might use a database ID, an email, or a phone number as the `integrationId`. It is vital that this ID **not** change over time, so **don't** use any identifier that the customer can update themselves. E.g. if your application allows a customer to update their e-mail address, you should instead use a database ID.  Updating a customer profile will return a response with the full integration state. This includes the current state of the customer profile, the customer session, the event that was recorded, and an array of effects that took place.  [Customer Profile]: /Getting-Started/entities#customer-profile [Rules]: /Getting-Started/entities#campaigns-rulesets-and-coupons 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.
body = talon_one.NewCustomerProfile() # NewCustomerProfile | 

try:
    # Update a Customer Profile
    api_response = api_instance.update_customer_profile(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_customer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile, must be unique within the account. | 
 **body** | [**NewCustomerProfile**](NewCustomerProfile.md)|  | 

### Return type

[**IntegrationState**](IntegrationState.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_session**
> IntegrationState update_customer_session(customer_session_id, body)

Update a Customer Session

Update (or create) a [Customer Session][]. For example, the items in a customers cart are part of a session.  The Talon.One platform supports multiple simultaneous sessions for the same profile, so if you have multiple ways of accessing the same application you have the option of either tracking multiple independent sessions or using the same session across all of them. You should share sessions when application access points share other state, such as the users cart. If two points of access to the application have independent state (e.g. a user can have different items in their cart across the two) they should use independent customer session ID's.  The `profileId` parameter in the request body should correspond to an `integrationId` for a customer profile, to track an anonymous session use the empty string (`\"\"`) as the `profileId`. Note that you do **not** need to create a customer profile first: if the specified profile does not yet exist, an empty profile will be created automatically.  Updating a customer profile will return a response with the full integration state. This includes the current state of the customer profile, the customer session, the event that was recorded, and an array of effects that took place.  The currency for the session and the cart items in the session is the same as that of the application with which the session is associated.  [Customer Session]: /Getting-Started/entities#customer-session 

### Example
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: integration_auth
configuration = talon_one.Configuration()
configuration.api_key['Content-Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# create an instance of the API class
api_instance = talon_one.IntegrationApi(talon_one.ApiClient(configuration))
customer_session_id = 'customer_session_id_example' # str | The custom identifier for this session, must be unique within the account.
body = talon_one.NewCustomerSession() # NewCustomerSession | 

try:
    # Update a Customer Session
    api_response = api_instance.update_customer_session(customer_session_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_customer_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_session_id** | **str**| The custom identifier for this session, must be unique within the account. | 
 **body** | [**NewCustomerSession**](NewCustomerSession.md)|  | 

### Return type

[**IntegrationState**](IntegrationState.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

