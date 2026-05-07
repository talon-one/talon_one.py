# UpdateBlueprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display name for the blueprint. | [optional] 
**description** | **str** | A longer, more detailed description of the blueprint. | [optional] 
**category** | **str** | Category used to group blueprints. | [optional] 
**rules** | [**list[CatalogRule]**](CatalogRule.md) | Replaces the stored rules. Rules should only contain title (no description, as description is at the blueprint level). | [optional] 
**cart_item_filters** | [**list[CartItemFilterTemplate]**](CartItemFilterTemplate.md) | Replaces the stored cart item filters. Cart item filters should only contain name (no description, as description is at the blueprint level). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


