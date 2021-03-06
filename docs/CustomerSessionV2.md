# CustomerSessionV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The integration ID for this entity sent to and used in the Talon.One system. | 
**created** | **datetime** | The exact moment this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**profile_id** | **str** | ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID. | 
**coupon_codes** | **list[str]** | Any coupon codes entered. | [optional] 
**referral_code** | **str** | Any referral code entered. | [optional] 
**state** | **str** | Indicates the current state of the session. All sessions must start in the \&quot;open\&quot; state, after which valid transitions are...  1. open -&gt; closed 2. open -&gt; cancelled 3. closed -&gt; cancelled  | [default to 'open']
**cart_items** | [**list[CartItem]**](CartItem.md) | All items the customer will be purchasing in this session | 
**additional_costs** | [**dict(str, AdditionalCost)**](AdditionalCost.md) | Any costs associated with the session that can not be explicitly attributed to cart items. Examples include shipping costs and service fees. | [optional] 
**identifiers** | **list[str]** | Identifiers for the customer, this can be used for limits on values such as device ID. | [optional] 
**attributes** | [**object**](.md) | A key-value map of the sessions attributes. The potentially valid attributes are configured in your accounts developer settings.  | 
**first_session** | **bool** | Indicates whether this is the first session for the customer&#39;s profile. Will always be true for anonymous sessions. | 
**total** | **float** | The total sum of cart-items, as well as additional costs, before any discounts applied | 
**cart_item_total** | **float** | The total sum of cart-items before any discounts applied | 
**additional_cost_total** | **float** | The total sum of additional costs before any discounts applied | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


