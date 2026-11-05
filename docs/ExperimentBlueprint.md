# ExperimentBlueprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this experiment blueprint. | 
**account_id** | **int** | The ID of the account that owns this experiment blueprint. | 
**application_id** | **int** | The ID of the Application that owns this experiment blueprint. | 
**title** | **str** | A short description of the experiment blueprint. | 
**description** | **str** | A longer, more detailed description of the experiment blueprint. | [optional] 
**category** | **str** | Category used to group experiment blueprints. | 
**source** | **str** | Indicates whether the experiment blueprint is custom or shipped by Talon.One. | 
**variants** | [**list[ExperimentBlueprintVariant]**](ExperimentBlueprintVariant.md) | Array of experiment variant templates in this experiment blueprint. Variants only contain name, weight, ruleset and the primary flag. | 
**cart_item_filters** | [**list[CartItemFilterTemplate]**](CartItemFilterTemplate.md) | Array of cart item filter templates in this experiment blueprint. Cart item filters only contain name (no description, as description is at the experiment blueprint level). | 
**created** | **datetime** | Timestamp when the experiment blueprint was created. | 
**created_by** | **int** | ID of the user who created the experiment blueprint. | 
**modified** | **datetime** | Timestamp when the experiment blueprint was last updated. | [optional] 
**modified_by** | **int** | ID of the user who last updated the experiment blueprint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


