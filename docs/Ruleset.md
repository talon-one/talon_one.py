# Ruleset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | 
**user_id** | **int** | The ID of the account that owns this entity. | 
**rules** | [**list[Rule]**](Rule.md) | Set of rules to apply. | 
**bindings** | [**list[Binding]**](Binding.md) | An array that provides objects with variable names (name) and talang expressions to whose result they are bound (expression) during rule evaluation. The order of the evaluation is decided by the position in the array. | 
**rb_version** | **str** | A string indicating which version of the rulebuilder was used to create this ruleset. | [optional] 
**activate** | **bool** | A boolean indicating whether this newly created ruleset should also be activated for the campaign owns it | [optional] 
**activated_at** | **datetime** | Timestamp indicating when this Ruleset was activated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


