# talon_one.IntegrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_reservation**](IntegrationApi.md#create_coupon_reservation) | **POST** /v1/coupon_reservations/{couponValue} | Create a new coupon reservation
[**create_referral**](IntegrationApi.md#create_referral) | **POST** /v1/referrals | Create a referral code for an advocate
[**delete_coupon_reservation**](IntegrationApi.md#delete_coupon_reservation) | **DELETE** /v1/coupon_reservations/{couponValue} | Delete coupon reservations
[**delete_customer_data**](IntegrationApi.md#delete_customer_data) | **DELETE** /v1/customer_data/{integrationId} | Delete the personal data of a customer
[**get_customer_inventory**](IntegrationApi.md#get_customer_inventory) | **GET** /v1/customer_profiles/{integrationId}/inventory | Get an inventory of all data associated with a specific customer profile
[**get_reserved_customers**](IntegrationApi.md#get_reserved_customers) | **GET** /v1/coupon_reservations/customerprofiles/{couponValue} | Get the users that have this coupon reserved
[**track_event**](IntegrationApi.md#track_event) | **POST** /v1/events | Track an Event
[**update_customer_profile**](IntegrationApi.md#update_customer_profile) | **PUT** /v1/customer_profiles/{integrationId} | Update a Customer Profile V1
[**update_customer_profile_audiences**](IntegrationApi.md#update_customer_profile_audiences) | **POST** /v2/customer_audiences | Update a Customer Profile Audiences
[**update_customer_profile_v2**](IntegrationApi.md#update_customer_profile_v2) | **PUT** /v2/customer_profiles/{integrationId} | Update a Customer Profile
[**update_customer_profiles_v2**](IntegrationApi.md#update_customer_profiles_v2) | **PUT** /v2/customer_profiles | Update multiple Customer Profiles
[**update_customer_session**](IntegrationApi.md#update_customer_session) | **PUT** /v1/customer_sessions/{customerSessionId} | Update a Customer Session V1
[**update_customer_session_v2**](IntegrationApi.md#update_customer_session_v2) | **PUT** /v2/customer_sessions/{customerSessionId} | Update a Customer Session


# **create_coupon_reservation**
> Coupon create_coupon_reservation(coupon_value, body)

Create a new coupon reservation

Creates a coupon reservation for all passed customer profiles on this couponID 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    coupon_value = 'coupon_value_example' # str | The value of a coupon
body = talon_one.CouponReservations() # CouponReservations | 

    try:
        # Create a new coupon reservation
        api_response = api_instance.create_coupon_reservation(coupon_value, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->create_coupon_reservation: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_referral**
> Referral create_referral(body)

Create a referral code for an advocate

Creates a referral code for an advocate. The code will be valid for the referral campaign for which is created, indicated in the `campaignId` parameter, and will be associated with the profile specified in the `advocateProfileIntegrationId` parameter as the advocate's profile. 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    body = talon_one.NewReferral() # NewReferral | 

    try:
        # Create a referral code for an advocate
        api_response = api_instance.create_referral(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->create_referral: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_reservation**
> delete_coupon_reservation(coupon_value, body)

Delete coupon reservations

Removes all passed customer profiles reservation from this coupon 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    coupon_value = 'coupon_value_example' # str | The value of a coupon
body = talon_one.CouponReservations() # CouponReservations | 

    try:
        # Delete coupon reservations
        api_instance.delete_coupon_reservation(coupon_value, body)
    except ApiException as e:
        print("Exception when calling IntegrationApi->delete_coupon_reservation: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_data**
> delete_customer_data(integration_id)

Delete the personal data of a customer

Delete all attributes on the customer profile and on entities that reference that customer profile. 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.

    try:
        # Delete the personal data of a customer
        api_instance.delete_customer_data(integration_id)
    except ApiException as e:
        print("Exception when calling IntegrationApi->delete_customer_data: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.

    try:
        # Delete the personal data of a customer
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_inventory**
> CustomerInventory get_customer_inventory(integration_id, profile=profile, referrals=referrals, coupons=coupons, loyalty=loyalty)

Get an inventory of all data associated with a specific customer profile

Get information regarding entities referencing this customer profile's integrationId. Currently we support customer profile information, referral codes and reserved coupons. In the future, this will be expanded with loyalty points.

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.
profile = True # bool | optional flag to decide if you would like customer profile information in the response (optional)
referrals = True # bool | optional flag to decide if you would like referral information in the response (optional)
coupons = True # bool | optional flag to decide if you would like coupon information in the response (optional)
loyalty = True # bool | optional flag to decide if you would like loyalty information in the response (optional)

    try:
        # Get an inventory of all data associated with a specific customer profile
        api_response = api_instance.get_customer_inventory(integration_id, profile=profile, referrals=referrals, coupons=coupons, loyalty=loyalty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->get_customer_inventory: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.
profile = True # bool | optional flag to decide if you would like customer profile information in the response (optional)
referrals = True # bool | optional flag to decide if you would like referral information in the response (optional)
coupons = True # bool | optional flag to decide if you would like coupon information in the response (optional)
loyalty = True # bool | optional flag to decide if you would like loyalty information in the response (optional)

    try:
        # Get an inventory of all data associated with a specific customer profile
        api_response = api_instance.get_customer_inventory(integration_id, profile=profile, referrals=referrals, coupons=coupons, loyalty=loyalty)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->get_customer_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile, must be unique within the account. | 
 **profile** | **bool**| optional flag to decide if you would like customer profile information in the response | [optional] 
 **referrals** | **bool**| optional flag to decide if you would like referral information in the response | [optional] 
 **coupons** | **bool**| optional flag to decide if you would like coupon information in the response | [optional] 
 **loyalty** | **bool**| optional flag to decide if you would like loyalty information in the response | [optional] 

### Return type

[**CustomerInventory**](CustomerInventory.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reserved_customers**
> InlineResponse200 get_reserved_customers(coupon_value)

Get the users that have this coupon reserved

Returns all users that have this coupon marked as reserved 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    coupon_value = 'coupon_value_example' # str | The value of a coupon

    try:
        # Get the users that have this coupon reserved
        api_response = api_instance.get_reserved_customers(coupon_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->get_reserved_customers: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_event**
> IntegrationState track_event(body, dry=dry)

Track an Event

Records an arbitrary event in a customer session. For example, an integration might record an event when a user updates their payment information.  The `sessionId` body parameter is required, an event is always part of a session. Much like updating a customer session, if either the profile or the session do not exist, a new empty one will be created. Note that if the specified session already exists, it must belong to the same `profileId` or an error will be returned.  As with customer sessions, you can use an empty string for `profileId` to indicate that this is an anonymous session.  Updating a customer profile will return a response with the full integration state. This includes the current state of the customer profile, the customer session, the event that was recorded, and an array of effects that took place. 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    body = talon_one.NewEvent() # NewEvent | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Track an Event
        api_response = api_instance.track_event(body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->track_event: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    body = talon_one.NewEvent() # NewEvent | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Track an Event
        api_response = api_instance.track_event(body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->track_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewEvent**](NewEvent.md)|  | 
 **dry** | **bool**| Indicates whether to skip persisting the changes or not (Will not persist if set to &#39;true&#39;). | [optional] 

### Return type

[**IntegrationState**](IntegrationState.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_profile**
> IntegrationState update_customer_profile(integration_id, body, dry=dry)

Update a Customer Profile V1

⚠️ Deprecation Notice: Support for requests to this endpoint will end on 15.07.2021. We will not remove the endpoint, and it will still be accessible for you to use. For new features support, migrate to [API V2.0](/Getting-Started/APIV2).  Update (or create) a [Customer Profile](https://developers.talon.one/Getting-Started/entities#customer-profile). This profile information can then be matched and/or updated by campaign [Rules][].  The `integrationId` may be any identifier that will remain stable for the customer. For example, you might use a database ID, an email, or a phone number as the `integrationId`. It is vital that this ID **not** change over time, so **don't** use any identifier that the customer can update themselves. E.g. if your application allows a customer to update their e-mail address, you should instead use a database ID.  Updating a customer profile will return a response with the full integration state. This includes the current state of the customer profile, the customer session, the event that was recorded, and an array of effects that took place.  [Customer Profile]: /Getting-Started/entities#customer-profile [Rules]: /Getting-Started/entities#campaigns-rulesets-and-coupons 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.
body = talon_one.NewCustomerProfile() # NewCustomerProfile | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Update a Customer Profile V1
        api_response = api_instance.update_customer_profile(integration_id, body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_profile: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile, must be unique within the account.
body = talon_one.NewCustomerProfile() # NewCustomerProfile | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Update a Customer Profile V1
        api_response = api_instance.update_customer_profile(integration_id, body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile, must be unique within the account. | 
 **body** | [**NewCustomerProfile**](NewCustomerProfile.md)|  | 
 **dry** | **bool**| Indicates whether to skip persisting the changes or not (Will not persist if set to &#39;true&#39;). | [optional] 

### Return type

[**IntegrationState**](IntegrationState.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_profile_audiences**
> update_customer_profile_audiences(body)

Update a Customer Profile Audiences

Update one ore multiple Customer Profiles with the specified Audiences 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    body = talon_one.CustomerProfileAudienceRequest() # CustomerProfileAudienceRequest | 

    try:
        # Update a Customer Profile Audiences
        api_instance.update_customer_profile_audiences(body)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_profile_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerProfileAudienceRequest**](CustomerProfileAudienceRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key_v1](../README.md#api_key_v1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_profile_v2**
> IntegrationStateV2 update_customer_profile_v2(integration_id, body, run_rule_engine=run_rule_engine, dry=dry)

Update a Customer Profile

Update (or create) a [Customer Profile](https://developers.talon.one/Getting-Started/entities#customer-profile).  The `integrationId` must be any identifier that remains stable for the customer. Do not use an ID that the customer can update themselves. For example, you can use a database ID.  Updating a customer profile returns a response with the requested integration state. If `runRuleEngine` is set to `true`, the response includes:  - The effects generated by the triggered campaigns. - The created coupons and referral objects. - Any entity that was requested in the `responseContent` request parameter. 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    integration_id = 'integration_id_example' # str | The custom identifier for this profile. Must be unique within the account.
body = talon_one.CustomerProfileIntegrationRequestV2() # CustomerProfileIntegrationRequestV2 | 
run_rule_engine = False # bool | Indicates whether to run the rule engine. (optional) (default to False)
dry = True # bool | Indicates whether to persist the changes. Changes are persisted with `true`. Only used when `runRuleEngine` is set to `true`.  (optional)

    try:
        # Update a Customer Profile
        api_response = api_instance.update_customer_profile_v2(integration_id, body, run_rule_engine=run_rule_engine, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_profile_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The custom identifier for this profile. Must be unique within the account. | 
 **body** | [**CustomerProfileIntegrationRequestV2**](CustomerProfileIntegrationRequestV2.md)|  | 
 **run_rule_engine** | **bool**| Indicates whether to run the rule engine. | [optional] [default to False]
 **dry** | **bool**| Indicates whether to persist the changes. Changes are persisted with &#x60;true&#x60;. Only used when &#x60;runRuleEngine&#x60; is set to &#x60;true&#x60;.  | [optional] 

### Return type

[**IntegrationStateV2**](IntegrationStateV2.md)

### Authorization

[api_key_v1](../README.md#api_key_v1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_profiles_v2**
> MultipleCustomerProfileIntegrationResponseV2 update_customer_profiles_v2(body, silent=silent)

Update multiple Customer Profiles

Update (or create) up to 1000 [Customer Profiles](https://developers.talon.one/Getting-Started/entities#customer-profile) in 1 request.  The `integrationId` must be any identifier that remains stable for the customer. Do not use an ID that the customer can update themselves. For example, you can use a database ID.  A customer profile [can be linked to one or more sessions](https://developers.talon.one/Integration-API/API-Reference#updateCustomerSessionV2). 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    body = talon_one.MultipleCustomerProfileIntegrationRequest() # MultipleCustomerProfileIntegrationRequest | 
silent = 'silent_example' # str | If set to `yes`, response will be an empty 204, otherwise a list of integration states will be generated (up to 1000). (optional)

    try:
        # Update multiple Customer Profiles
        api_response = api_instance.update_customer_profiles_v2(body, silent=silent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_profiles_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MultipleCustomerProfileIntegrationRequest**](MultipleCustomerProfileIntegrationRequest.md)|  | 
 **silent** | **str**| If set to &#x60;yes&#x60;, response will be an empty 204, otherwise a list of integration states will be generated (up to 1000). | [optional] 

### Return type

[**MultipleCustomerProfileIntegrationResponseV2**](MultipleCustomerProfileIntegrationResponseV2.md)

### Authorization

[api_key_v1](../README.md#api_key_v1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_session**
> IntegrationState update_customer_session(customer_session_id, body, dry=dry)

Update a Customer Session V1

⚠️ Deprecation Notice: Support for requests to this endpoint will end on 15.07.2021. We will not remove the endpoint, and it will still be accessible for you to use. For new features support, migrate to [API V2.0](https://developers.talon.one/Getting-Started/APIV2).  Update (or create) a [Customer Session](https://developers.talon.one/Getting-Started/entities#customer-session). For example, use this endpoint to represent which items are in the customer's cart.  The Talon.One platform supports multiple simultaneous sessions for the same profile. If you have multiple ways of accessing the same application you can either:  - Track multiple independent sessions or, - Use the same session across all of them.  You should share sessions when application access points share other state, such as the user's cart. If two points of access to the application have independent states, for example a user can have different items in their cart across the two) they should use independent customer session ID's.  To link a session to a customer profile, set the `profileId` parameter in the request body to a customer profile's `integrationId`. To track an anonymous session use the empty string (`\"\"`) as the `profileId`. **Note:** You do **not** have to create a customer profile first. If the specified profile does not exist, an empty profile is created automatically.  Updating a customer profile returns a response with the full integration state. This includes the current state of the customer profile, the customer session, the event that was recorded, and an array of effects that took place.  The currency for the session and the cart items in the session is the same as that of the application with which the session is associated. 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    customer_session_id = 'customer_session_id_example' # str | The custom identifier for this session, must be unique within the account.
body = talon_one.NewCustomerSession() # NewCustomerSession | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Update a Customer Session V1
        api_response = api_instance.update_customer_session(customer_session_id, body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_session: %s\n" % e)
```

* Api Key Authentication (integration_auth):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: integration_auth
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Content-Signature': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Content-Signature'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    customer_session_id = 'customer_session_id_example' # str | The custom identifier for this session, must be unique within the account.
body = talon_one.NewCustomerSession() # NewCustomerSession | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Update a Customer Session V1
        api_response = api_instance.update_customer_session(customer_session_id, body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_session_id** | **str**| The custom identifier for this session, must be unique within the account. | 
 **body** | [**NewCustomerSession**](NewCustomerSession.md)|  | 
 **dry** | **bool**| Indicates whether to skip persisting the changes or not (Will not persist if set to &#39;true&#39;). | [optional] 

### Return type

[**IntegrationState**](IntegrationState.md)

### Authorization

[api_key_v1](../README.md#api_key_v1), [integration_auth](../README.md#integration_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_session_v2**
> IntegrationStateV2 update_customer_session_v2(customer_session_id, body, dry=dry)

Update a Customer Session

Update (or create) a [Customer Session](https://developers.talon.one/Getting-Started/entities#customer-session). For example, use this endpoint to represent which items are in the customer's cart.  The Talon.One platform supports multiple simultaneous sessions for the same profile. If you have multiple ways of accessing the same application you can either:  - Track multiple independent sessions or, - Use the same session across all of them.  You should share sessions when application access points share other state, such as the user's cart. If two points of access to the application have independent states, for example a user can have different items in their cart across the two) they should use independent customer session ID's.  To link a session to a customer profile, set the `profileId` parameter in the request body to a customer profile's `integrationId`. To track an anonymous session use the empty string (`\"\"`) as the `profileId`. **Note:** You do **not** have to create a customer profile first. If the specified profile does not exist, an empty profile is created automatically.  Updating a customer session returns a response with the requested integration state. If `runRuleEngine` is set to `true`, the response includes:  - The effects generated by the triggered campaigns. - The created coupons and referral objects. - Any entity that was requested in the `responseContent` request parameter.  The currency for the session and the cart items in the session is the same as that of the application with which the session is associated. 

### Example

* Api Key Authentication (api_key_v1):
```python
from __future__ import print_function
import time
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = talon_one.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with talon_one.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = talon_one.IntegrationApi(api_client)
    customer_session_id = 'customer_session_id_example' # str | The custom identifier for this session, must be unique within the account.
body = talon_one.IntegrationRequest() # IntegrationRequest | 
dry = True # bool | Indicates whether to skip persisting the changes or not (Will not persist if set to 'true'). (optional)

    try:
        # Update a Customer Session
        api_response = api_instance.update_customer_session_v2(customer_session_id, body, dry=dry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationApi->update_customer_session_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_session_id** | **str**| The custom identifier for this session, must be unique within the account. | 
 **body** | [**IntegrationRequest**](IntegrationRequest.md)|  | 
 **dry** | **bool**| Indicates whether to skip persisting the changes or not (Will not persist if set to &#39;true&#39;). | [optional] 

### Return type

[**IntegrationStateV2**](IntegrationStateV2.md)

### Authorization

[api_key_v1](../README.md#api_key_v1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

