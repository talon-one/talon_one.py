# Application


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of this application. | 
**description** | **str** | A longer description of the application. | [optional] 
**timezone** | **str** | A string containing an IANA timezone descriptor. | 
**currency** | **str** | A string describing a default currency for new customer sessions. | 
**case_sensitivity** | **str** | A string indicating how should campaigns in this application deal with case sensitivity on coupon codes. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Default limits for campaigns created in this application | [optional] 
**campaign_priority** | **str** | Default priority for campaigns created in this application, can be one of (universal, stackable, exclusive). If no value is provided, this is set to \&quot;universal\&quot; | [optional] 
**exclusive_campaigns_strategy** | **str** | The strategy used when choosing exclusive campaigns for evaluation, can be one of (listOrder, lowestDiscount, highestDiscount). If no value is provided, this is set to \&quot;listOrder\&quot; | [optional] 
**enable_cascading_discounts** | **bool** | Flag indicating if discounts should cascade for this application | [optional] 
**enable_flattened_cart_items** | **bool** | Flag indicating if cart items of quantity larger than one should be separated into different items of quantity one | [optional] 
**attributes_settings** | [**AttributesSettings**](AttributesSettings.md) |  | [optional] 
**sandbox** | **bool** | Flag indicating if this is a live or sandbox application | [optional] 
**loyalty_programs** | [**list[LoyaltyProgram]**](LoyaltyProgram.md) | An array containing all the loyalty programs to which this application is subscribed | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


