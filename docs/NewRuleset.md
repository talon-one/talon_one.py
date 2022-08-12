# NewRuleset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**list[Rule]**](Rule.md) | Set of rules to apply. | 
**bindings** | [**list[Binding]**](Binding.md) | An array that provides objects with variable names (name) and talang expressions to whose result they are bound (expression) during rule evaluation. The order of the evaluation is decided by the position in the array. | 
**rb_version** | **str** | The version of the rulebuilder used to create this ruleset. | [optional] 
**activate** | **bool** | Indicates whether this created ruleset should be activated for the campaign that owns it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


