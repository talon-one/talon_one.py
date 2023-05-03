# ApplicationEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**profile_id** | **int** | The globally unique Talon.One ID of the customer that created this entity. | [optional] 
**session_id** | **int** | The globally unique Talon.One ID of the session that contains this event. | [optional] 
**type** | **str** | A string representing the event. Must not be a reserved event name. | 
**attributes** | [**object**](.md) | Additional JSON serialized data associated with the event. | 
**effects** | [**list[Effect]**](Effect.md) | An array containing the effects that were applied as a result of this event. | 
**rule_failure_reasons** | [**list[RuleFailureReason]**](RuleFailureReason.md) | An array containing the rule failure reasons which happened during this event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


