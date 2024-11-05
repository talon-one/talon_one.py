import talon_one
from talon_one.rest import ApiException
from pprint import pprint
import json
import os

# Create configuration with your host destination and authorization using api_key_v1
configuration = talon_one.Configuration(
    host = "http://localhost:9000",
    api_key_prefix = {
        "Authorization": "ApiKey-v1"
    },
    api_key = {
        "Authorization": os.environ["TALON_API_KEY"]
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
