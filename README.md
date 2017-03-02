# Talon.One Python 2.X SDK

Talon.One enables marketers to create coupon, discount, loyalty, and referral
marketing campaigns of virtually unlimited power and flexibility. This library
provides following API clients:

## Getting started with the Integration API

First, you will need to find your API endpoint, Application ID and Application Key in the Camapaign Manager by going to the "Settings" tab.

With these basic setting options we can set up the integration API client:
```python
from talon_one import integration

# setup my company specific application settings
my_endpoint_url="https://mycompany.talon.one"
my_app_id=1
my_app_key="a78cc977fce0fd53"

# create API client
talon_client = integration.Client(my_endpoint_url, my_app_id, my_app_key)
```
Once the `client` has been created, you can start sending customer profiles,
sessions and events to Talon.One:

```python
# When the customer registers or updates their account
data = {"advocateId": "",
         "attributes": {
             "Name": "Val Kust",
             "BillingAddress1": "21 Jump St."
         }
        }
client.update_customer_profile("my_unique_profile_id", data)

# Create a new referral code for a profile that could be used in customer sessions
data = {"advocateProfileIntegrationId": self.__class__.profile_id,
        "campaignId": self.campaign["id"],
        "expiryDate": "2017-08-17T16:08:52.018206901+02:00",
        "startDate": "2017-02-28T16:08:52.018206901+01:00"}
client.create_referral_code(data)

# When the customer adds an item to their cart
data = {"profileId": "my_unique_profile_id",
        "cartItems": [{"name": "Shiny Red Shoes",
                       "sku": "srs_1234",
                       "price": 49.99,
                       "quantity": 1,
                       "currency": "USD"
                       }],
        "attributes": { "ShippingCost": 3.75 },
        "referral": "996732pucn",
        "state": "open",
        "total": 53.74
        }
client.update_customer_session("my_unique_session_id", data)

# When the customer does something else interesting using already defined EventType viewed_promo_page
client.track_event("my_unique_session_id", "viewed_promo_page", {"url": "http://example.com/summer-shoes-2016"})
```

## Handling of responses and errors

### Respponse
Successfull response from API is a Python `dict` represnting decode JSON response from API call.

### Errors
Invalid calls to API results in raising `TalonOneAPIError` exception that provides details about what went wrong.

Example usage with exception handling:
```python
try:
   client.track_event("foo", {"bar": False})
except exceptions.TalonOneAPIError as te:
   print te
```
Exception is wrapping HTTP, JSON and errors as well as API validation error messages.

## Installation
```bash
$ pip install -r requirements.txt
$ pip install -e .
```

## Testing

```bash
$ nosetests tests/
$ nosetests --with-coverage --cover-erase --cover-html --cover-package=talon_one
```

To view the full list of data that each of these API calls accepts, please consult our [API documentation][1].

[1]: http://developers.talon.one/integration-api/reference/
