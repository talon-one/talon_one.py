# Ruleset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**user_id** | **int** | The ID of the user associated with this entity. | 
**rules** | [**list[Rule]**](Rule.md) | Set of rules to apply. | 
**strikethrough_rules** | [**list[Rule]**](Rule.md) | Set of rules to apply for strikethrough. | [optional] 
**bindings** | [**list[Binding]**](Binding.md) | An array that provides objects with variable names (name) and talang expressions to whose result they are bound (expression) during rule evaluation. The order of the evaluation is decided by the position in the array. | 
**rb_version** | **str** | The version of the rulebuilder used to create this ruleset. | [optional] 
**activate** | **bool** | Indicates whether this created ruleset should be activated for the campaign that owns it. | [optional] 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | [optional] 
**template_id** | **int** | The ID of the campaign template that owns this entity. | [optional] 
**activated_at** | **datetime** | Timestamp indicating when this Ruleset was activated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


