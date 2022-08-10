# UpdateApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this application. | 
**description** | **str** | A longer description of the application. | [optional] 
**timezone** | **str** | A string containing an IANA timezone descriptor. | 
**currency** | **str** | The default currency for new customer sessions. | 
**case_sensitivity** | **str** | The case sensitivity behavior to check coupon codes in the campaigns of this Application. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Default limits for campaigns created in this application. | [optional] 
**campaign_priority** | **str** | Default [priority](https://docs.talon.one/docs/product/applications/setting-up-campaign-priorities) for campaigns created in this Application.  | [optional] [default to 'universal']
**exclusive_campaigns_strategy** | **str** | The strategy used when choosing exclusive campaigns for evaluation. | [optional] [default to 'listOrder']
**default_discount_scope** | **str** | The default scope to apply &#x60;setDiscount&#x60; effects on if no scope was provided with the effect.  | [optional] 
**enable_cascading_discounts** | **bool** | Indicates if discounts should cascade for this Application. | [optional] 
**enable_flattened_cart_items** | **bool** | Indicates if cart items of quantity larger than one should be separated into different items of quantity one. See [the docs](https://docs.talon.one/docs/product/campaigns/campaign-evaluation/#flattened-cart-items).  | [optional] 
**attributes_settings** | [**AttributesSettings**](AttributesSettings.md) |  | [optional] 
**sandbox** | **bool** | Indicates if this is a live or sandbox Application. | [optional] 
**enable_partial_discounts** | **bool** | Indicates if this Application supports partial discounts. | [optional] 
**default_discount_additional_cost_per_item_scope** | **str** | The default scope to apply &#x60;setDiscountPerItem&#x60; effects on if no scope was provided with the effect.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


