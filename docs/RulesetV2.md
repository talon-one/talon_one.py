# RulesetV2

Ruleset in the V2 JSON block format.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | [optional] [readonly] 
**created** | **datetime** | The time this entity was created. | [optional] [readonly] 
**user_id** | **int** | The ID of the user that created this ruleset. | [optional] [readonly] 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | [optional] [readonly] 
**template_id** | **int** | The ID of the campaign template that owns this entity. | [optional] [readonly] 
**activated_at** | **datetime** | Timestamp indicating when this ruleset was activated. | [optional] [readonly] 
**promotion_rules** | [**list[RuleV2]**](RuleV2.md) | Set of promotion rules. | 
**strikethrough_rules** | [**list[RuleV2]**](RuleV2.md) | Set of strikethrough rules. | [optional] 
**selectors** | [**list[Selector]**](Selector.md) | Variable bindings of type selector. | [optional] [readonly] 
**bundles** | [**list[Bundle]**](Bundle.md) | Variable bindings of type bundle. | [optional] [readonly] 
**parameters** | [**list[TemplateParameter]**](TemplateParameter.md) | Variable bindings of type template parameter. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


