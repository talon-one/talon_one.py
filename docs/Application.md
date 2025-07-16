# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**modified** | **datetime** | The time this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of this application. | 
**description** | **str** | A longer description of the application. | [optional] 
**timezone** | **str** | A string containing an IANA timezone descriptor. | 
**currency** | **str** | The default currency for new customer sessions. | 
**case_sensitivity** | **str** | The case sensitivity behavior to check coupon codes in the campaigns of this Application. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Default limits for campaigns created in this application. | [optional] 
**default_discount_scope** | **str** | The default scope to apply &#x60;setDiscount&#x60; effects on if no scope was provided with the effect.  | [optional] 
**enable_cascading_discounts** | **bool** | Indicates if discounts should cascade for this Application. | [optional] 
**enable_flattened_cart_items** | **bool** | Indicates if cart items of quantity larger than one should be separated into different items of quantity one.  | [optional] 
**attributes_settings** | [**AttributesSettings**](AttributesSettings.md) |  | [optional] 
**sandbox** | **bool** | Indicates if this is a live or sandbox Application. | [optional] 
**enable_partial_discounts** | **bool** | Indicates if this Application supports partial discounts. | [optional] 
**default_discount_additional_cost_per_item_scope** | **str** | The default scope to apply &#x60;setDiscountPerItem&#x60; effects on if no scope was provided with the effect.  | [optional] 
**default_evaluation_group_id** | **int** | The ID of the default campaign evaluation group to which new campaigns will be added unless a different group is selected when creating the campaign. | [optional] 
**default_cart_item_filter_id** | **int** | The ID of the default Cart-Item-Filter for this application. | [optional] 
**enable_campaign_state_management** | **bool** | Indicates whether the campaign staging and revisions feature is enabled for the Application.  **Important:** After this feature is enabled, it cannot be disabled.  | [optional] 
**loyalty_programs** | [**list[LoyaltyProgram]**](LoyaltyProgram.md) | An array containing all the loyalty programs to which this application is subscribed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


