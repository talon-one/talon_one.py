# NewExperimentBlueprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display name for the experiment blueprint. | 
**description** | **str** | A longer, more detailed description of the experiment blueprint. | [optional] 
**category** | **str** | Category used to group experiment blueprints. | [optional] [default to 'custom']
**variants** | [**list[ExperimentBlueprintVariant]**](ExperimentBlueprintVariant.md) | Array of experiment variant templates to store in this experiment blueprint. At least one variant or cart item filter is required. | [optional] 
**cart_item_filters** | [**list[CartItemFilterTemplate]**](CartItemFilterTemplate.md) | Array of cart item filters to store in this experiment blueprint. If not provided, will be extracted from the variant rulesets. Cart item filters should only contain name (no description, as description is at the experiment blueprint level). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


