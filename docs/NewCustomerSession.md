# NewCustomerSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID. | [optional] 
**coupon** | **str** | Any coupon code entered. | [optional] 
**referral** | **str** | Any referral code entered. | [optional] 
**state** | **str** | Indicates the current state of the session. All sessions must start in the \&quot;open\&quot; state, after which valid transitions are...  1. open -&gt; closed 2. open -&gt; cancelled 3. closed -&gt; cancelled  | [optional] [default to 'open']
**cart_items** | [**list[CartItem]**](CartItem.md) | Serialized JSON representation. | [optional] 
**identifiers** | **list[str]** | Identifiers for the customer, this can be used for limits on values such as device ID. | [optional] 
**total** | **float** | The total sum of the cart in one session. | [optional] 
**attributes** | [**object**](.md) | A key-value map of the sessions attributes. The potentially valid attributes are configured in your accounts developer settings.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


