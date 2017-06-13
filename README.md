# Talon.One Python SDK [![Build Status](https://travis-ci.org/talon-one/talon_one.py.svg?branch=master)](https://travis-ci.org/talon-one/talon_one.py)

[Talon.One][1] enables marketers to create coupon, discount, loyalty, and referral
marketing campaigns of virtually unlimited power and flexibility. This library
provides SDK for working with integration API.

## Getting started with the Integration API

First, you will need to find your API endpoint, Application ID and Application Key in the Camapaign Manager (CAMA) by going to the "Settings" tab.

There are three ways how to configure API client:
* Client constructor parameters
* Client setters
* ENV variables (see table bellow)

### Basics
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

### Create a customer profile
```python
# When the customer registers or updates their account
data = {"advocateId": "",
         "attributes": {
             "Name": "Val Kust",
             "BillingAddress1": "21 Jump St."
         }
        }
client.update_customer_profile("my_unique_profile_id", data)
```

### Create a new referral code
```python
# Create a new referral code for a profile that could be used in customer sessions
data = {"advocateProfileIntegrationId": "my_unique_profile_id",
        "campaignId": 1,
        "expiryDate": "2017-08-17T16:08:52.018206901+02:00",
        "startDate": "2017-02-28T16:08:52.018206901+01:00"}
client.create_referral_code(data)
```

### Open a customer session
```python
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
```

### Track a custom event related to opened session

```python
# When the customer does something else interesting using already defined EventType viewed_promo_page
client.track_event("my_unique_session_id", "viewed_promo_page", {"url": "http://example.com/summer-shoes-2016"})
```

### Close an opened session
```python
# Finally you close session to finalize whole transaction
client.close_customer_session("my_unique_session_id")
```

Supported configuration ENV variables:

| Name              | Type    | Description              |
| ----------------- | ------- | ------------------------ |
| TALONONE_ENDPOINT | string  | Your CAMA domain         |
| TALONONE_APP_ID   | integer | Your application id      |
| TALONONE_APP_KEY  | string  | Your application API key |

## Handling of responses and errors
SDK raises an error in case of HTTP, validation and logical errors otherwise return result from API in form of JSON.

### Response
Successfull response from API is a Python `dict` representing decoded JSON response from API call.

### Errors
Invalid calls to API results in raising `TalonOneAPIError` exception that provides details about what went wrong.

Example usage with exception handling:
```python
try:
   client.track_event("foo", {"bar": False})
except exceptions.TalonOneAPIError as te:
   print te
```
Exception is wrapping HTTP, JSON and errors as well as [API validation error][3] messages.

## Requirements
* openssl-dev (for `hashlib` package)
* python 2 or 3

## Installation

### Python 2
As of now we recommend pulling directly from GitHub and running local `pip` installation:
```bash
$ pip install -r requirements.txt
$ pip install -e .
```

### Python 3
As of now we recommend pulling directly from GitHub and running local `pip3` installation:
```bash
$ pip3 install -r requirements.txt
$ pip3 install -e .
```

## Testing

First make sure you have following dependencies installed:
* unittest
* nose
* coverage

```bash
$ nosetests tests/
$ nosetests --with-coverage --cover-erase --cover-html --cover-package=talon_one
```

To view the full list of data that each of these API calls accepts, please consult our [API documentation][2].

[1]: https://talon.one/
[2]: http://developers.talon.one/integration-api/reference/
[3]: https://developers.talon.one/integration-api/errors/
