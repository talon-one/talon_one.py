# RoleV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**modified** | **datetime** | The time this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | Name of the role. | [optional] 
**description** | **str** | Description of the role. | [optional] 
**permissions** | [**RoleV2Permissions**](RoleV2Permissions.md) |  | [optional] 
**members** | **list[int]** | A list of user IDs the role is assigned to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


