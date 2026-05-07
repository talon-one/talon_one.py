# Experiment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**is_variant_assignment_external** | **bool** | The source of the assignment. - false - The variant assignment is handled internally by Talon.One. - true - The variant assignment is handled externally.  | [optional] 
**campaign** | [**Campaign**](Campaign.md) |  | [optional] 
**activated** | **datetime** | The date and time the experiment was activated.  | [optional] 
**state** | **str** | A disabled experiment is not evaluated for rules or coupons.  | [default to 'disabled']
**variants** | [**list[ExperimentVariant]**](ExperimentVariant.md) |  | [optional] 
**deletedat** | **datetime** | The date and time the experiment was deleted.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


