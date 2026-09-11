# UpdateAttributeValueBlock

A block that sets or updates an attribute. The `type` may be empty for [built-in attributes](https://docs.talon.one/docs/dev/concepts/attributes).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**operator** | **str** | The update operation applied to the attribute. | 
**attribute** | [**UpdateAttributeValueBlockAttribute**](UpdateAttributeValueBlockAttribute.md) |  | 
**value** | [**object**](.md) | The value of the attribute. Omitted when operator is set to &#x60;toggle&#x60;. | [optional] 
**target** | [**UpdateAttributeValueBlockTarget**](UpdateAttributeValueBlockTarget.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


