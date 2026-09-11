# AwardDiscountBlock

A block that grants a discount when its rule conditions evaluate to `true`. The `target` field determines what the discount applies to (the whole cart, a subset of items, a bundle, an additional cost, etc.); the `value` field is the discount amount.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**name** | **str** | The human-readable label attached to the discount. | 
**value** | [**object**](.md) | Discount amount. Either a numeric scalar or a &#x60;{{expression}}&#x60; string that resolves to a number at evaluation time. | 
**partial** | **bool** | Whether to apply a partial discount when the requested value exceeds the configured budget. | 
**target** | [**object**](.md) | Identifies the scope a discount applies to. The &#x60;type&#x60; field selects the concrete target variant. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


