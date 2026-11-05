# UpdateExperimentBlueprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display name for the experiment blueprint. | [optional] 
**description** | **str** | A longer, more detailed description of the experiment blueprint. | [optional] 
**category** | **str** | Category used to group experiment blueprints. | [optional] 
**variants** | [**list[ExperimentBlueprintVariant]**](ExperimentBlueprintVariant.md) | Replaces the stored experiment variant templates. | [optional] 
**cart_item_filters** | [**list[CartItemFilterTemplate]**](CartItemFilterTemplate.md) | Replaces the stored cart item filters. Cart item filters should only contain name (no description, as description is at the experiment blueprint level). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


