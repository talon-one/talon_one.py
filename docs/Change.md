# Change

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**user_id** | **int** | The ID of the account that owns this entity. | 
**application_id** | **int** | ID of application associated with change | [optional] 
**entity** | **str** | API endpoint on which the change was initiated. | 
**old** | [**object**](.md) | Resource before the change occurred. | [optional] 
**new** | [**object**](.md) | Resource after the change occurred. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


