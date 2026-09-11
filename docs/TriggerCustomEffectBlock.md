# TriggerCustomEffectBlock

A block that triggers a configured custom effect and passes its required parameters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**custom_effect** | [**TriggerCustomEffectBlockCustomEffect**](TriggerCustomEffectBlockCustomEffect.md) |  | 
**params** | [**object**](.md) | The custom effect&#39;s parameters, in configured order. Each property name is the parameter&#39;s title, lowercased with spaces replaced by underscores (for example, &#x60;Order ID&#x60; becomes &#x60;order_id&#x60;); falls back to &#x60;param_0&#x60;, &#x60;param_1&#x60;, and so on if a title is blank or collides with another. | [optional] 
**target** | [**TriggerCustomEffectBlockTarget**](TriggerCustomEffectBlockTarget.md) |  | 
**on_error** | **dict(str, list[object])** | Named error handlers evaluated when a specific error occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


