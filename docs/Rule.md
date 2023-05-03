# Rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the rule. | [optional] 
**parent_id** | **str** | The ID of the rule that was copied to create this rule. | [optional] 
**title** | **str** | A short description of the rule. | 
**description** | **str** | A longer, more detailed description of the rule. | [optional] 
**bindings** | [**list[Binding]**](Binding.md) | An array that provides objects with variable names (name) and talang expressions to whose result they are bound (expression) during rule evaluation. The order of the evaluation is decided by the position in the array. | [optional] 
**condition** | **list[object]** | A Talang expression that will be evaluated in the context of the given event. | 
**effects** | **list[object]** | An array of effectful Talang expressions in arrays that will be evaluated when a rule matches. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


