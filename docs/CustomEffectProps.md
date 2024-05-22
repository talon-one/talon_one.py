# CustomEffectProps

Effect containing custom payload.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect_id** | **int** | The ID of the custom effect that was triggered. | 
**name** | **str** | The type of the custom effect. | 
**cart_item_position** | **float** | The index of the item in the cart item list to which the custom effect is applied. | [optional] 
**cart_item_sub_position** | **float** | For cart items with quantity &gt; 1, the sub position indicates to which item unit the custom effect is applied.  | [optional] 
**bundle_index** | **int** | The position of the bundle in a list of item bundles created from the same bundle definition. | [optional] 
**bundle_name** | **str** | The name of the bundle definition. | [optional] 
**payload** | [**object**](.md) | The JSON payload of the custom effect. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


