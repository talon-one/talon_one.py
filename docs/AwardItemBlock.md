# AwardItemBlock

A block that awards a free cart item to the customer. The item is identified by SKU and name and has a configurable quantity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**sku** | **str** | The stock keeping unit of the item to award. | 
**name** | **str** | The display name of the item to award. | 
**quantity** | **str** | The number of items to award. Supports template placeholders (e.g. \&quot;{{$Session.Total / 2}}\&quot;) for dynamic quantities. | 
**partial** | **bool** | When set to &#x60;true&#x60;, applies a partial item reward if the remaining budget is insufficient to award the full reward. | [optional] 
**on_failure** | **list[object]** | Blocks evaluated when this block fails or returns false. | [optional] 
**on_error** | **dict(str, list[object])** | Named error handlers evaluated when a specific error occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


