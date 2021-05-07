
import talon_one
from talon_one.rest import ApiException
from pprint import pprint
import json
import csv

# Create configuration with your host destination and authorization using api_key_v1
configuration = talon_one.Configuration(
    host = 'http://localhost:9000',
    api_key_prefix = {
        'Authorization': 'ApiKey-v1'
    },
    api_key = {
        'Authorization': 'f10e9ee8463785b1aa0f40fa64bfed336253bddf2f3b55d76cb65055e638fdc9'
    }
)
# # Configure API key authorization: api_key_v1
# configuration = talon_one.Configuration()
# configuration.host = "http://localhost:9000"
# # configuration.host = "http://host.docker.internal:9000"

# configuration.api_key["Authorization"] = "f10e9ee8463785b1aa0f40fa64bfed336253bddf2f3b55d76cb65055e638fdc9"
# configuration.api_key_prefix["Authorization"] = "ApiKey-v1"
configuration.debug = True

# create an instance of the API class
integration_api = talon_one.IntegrationApi(talon_one.ApiClient(configuration))

##########################################################################################
##########################################################################################
##########################################################################################

# # Integration API example to send a customer session update
# customer_session = talon_one.NewCustomerSession(
#   "", # profile_id
#   "", # coupon
#   "", # referral
#   "open", # state
#   None, # cart_items
#   None, # identifiers
#   123.45, # total
#   None # attributes
# )

# try:
#     # Create a new session
#     api_response = integration_api.update_customer_session("my_unique_session_id", customer_session, dry=False)
#     print(">>> Integration API update_customer_session call succeeded\n\n")
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling IntegrationApi->update_customer_session: %s\n" % e)



##########################################################################################
##########################################################################################
##########################################################################################

# # Integration API example to send a customer profile update
# customer_profile = talon_one.NewCustomerProfile(attributes={
#   "Name": "WOHHHOOOO"
# })


# try:
#     # Create/update a customer profile using `update_customer_profile` function
#     api_response = integration_api.update_customer_profile("my_unique_profile_id", customer_profile)
#     print("\n\n>>> Integration API update_customer_profile call succeeded\n\n")
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling IntegrationApi->update_customer_profile: %s\n" % e)

##########################################################################################
##########################################################################################
##########################################################################################

# # Integration API example to get a customer profile inventory
# try:
#     # Create/update a customer profile using `update_customer_profile` function
#     api_response = integration_api.get_customer_inventory("my_unique_profile_id", profile=True, coupons=True, loyalty=True)
#     print("\n\n>>> Integration API get_customer_inventory call succeeded\n\n")
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling IntegrationApi->get_customer_inventory: %s\n" % e)

##########################################################################################
##########################################################################################
##########################################################################################

# # Integration API example to send a customer session v2 update
# customer_session = talon_one.NewCustomerSessionV2()
# customer_session.cart_items = [
#     talon_one.CartItem("Pita", "pit", 1, 2.2, "Foods"),
#     talon_one.CartItem("Pita2", "pit2", 2, 1.5, "Foods"),
# ]
# customer_session.coupon_codes = [
#     "Cool_Stuff"
# ]

# integration_request = talon_one.IntegrationRequest(
#     customer_session,
#     ["customerSession", "ruleFailureReasons"]
# )


# try:
#     # Create a new session
#     api_response = integration_api.update_customer_session_v2("my_unique_session_id_22", integration_request)
#     print(">>> Integration API update_customer_session_v2 call succeeded\n\n")
#     pprint(api_response)

#     # Parsing the returned effects list, please consult https://developers.talon.one/Integration-API/handling-effects-v2 for the full list of effects and their corresponding properties
#     for effect in api_response.effects:
#         if effect.effect_type == "setDiscount":
#             # Initiating right props instance according to the effect type
#             setDiscountProps = integration_api.api_client.deserialize_model(effect.props, talon_one.SetDiscountEffectProps)

#             # Access the specific effect's properties
#             # print(f"Set a discount '{setDiscountProps.name}' of {setDiscountProps.value}")
#             # Or, if you use python <3
#             print("Set a discount '{name}' of {value}".format(
#                 name = setDiscountProps.name,
#                 value = setDiscountProps.value
#             ))
#         elif effect.effect_type == "rejectCoupon":
#             rejectCouponEffectProps = integration_api.api_client.deserialize_model(effect.props, talon_one.RejectCouponEffectProps)

#             # Work with AcceptCouponEffectProps' properties
#             # ...
# except ApiException as e:
#     print("Exception when calling IntegrationApi->update_customer_session_v2: %s\n" % e)

##########################################################################################
##########################################################################################
##########################################################################################

# # Integration API example to send a customer profile v2 update
# customer_profile_request = talon_one.CustomerProfileIntegrationRequestV2(
#     attributes = {
#         "Name": "neuer",
#         "Email": "neuer@bayern.de",
#     },
#     response_content = [
#         "customerProfile",
#         "loyalty"
#     ]
# )

# try:
#     # Create a new session
#     api_response = integration_api.update_customer_profile_v2("my_unique_profile_321", customer_profile_request, dry=True, run_rule_engine=True)
#     print(">>> Integration API update_customer_profile_v2 call succeeded\n\n")
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling IntegrationApi->update_customer_profile_v2: %s\n" % e)

##########################################################################################
##########################################################################################
##########################################################################################


# # Create configuration with your host destination
# manage_configuration = talon_one.Configuration(
#     host = "http://localhost:9000"
# )

# # Management API example to load application with id 7
# management_api = talon_one.ManagementApi(talon_one.ApiClient(manage_configuration))

# try:
#     # Acquire session token
#     login_params = talon_one.LoginParams("demo@talon.one", "Demo1234")
#     session = management_api.create_session(login_params)

#     # Save token in the configuration for future management API calls
#     manage_configuration.api_key["Authorization"] = session.token
#     manage_configuration.api_key_prefix["Authorization"] = "Bearer"

#     # Calling get_application function with the desired id (7)
#     application = management_api.get_application(1)
#     print("\n\n>>> Management API get_application call succeeded\n\n")
#     pprint(application)
# except ApiException as e:
#     print("Exception when calling ManagementApi->get_application: %s\n" % e)

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


# Create configuration with your host destination
manage_configuration = talon_one.Configuration(
    host = "http://localhost:9000"
)

# Management API example to load application with id 7
management_api = talon_one.ManagementApi(talon_one.ApiClient(manage_configuration))

try:
    # Acquire session token
    login_params = talon_one.LoginParams("demo@talon.one", "Demo1234")
    session = management_api.create_session(login_params)

    # Save token in the configuration for future management API calls
    manage_configuration.api_key["Authorization"] = session.token
    manage_configuration.api_key_prefix["Authorization"] = "Bearer"

    # Calling get_application function with the desired id (7)
    loyalty_program_id = "1"
    export_contents = management_api.export_loyalty_balance(loyalty_program_id)
    csv_reader = csv.reader(export_contents.splitlines())
    print("\n\n>>> Management API export_loyalty_balance call succeeded\n\n")

    for line in csv_reader:
        print(line)
except ApiException as e:
    print("Exception when calling ManagementApi->export_loyalty_balance: %s\n" % e)

##########################################################################################
##########################################################################################
##########################################################################################
