# Revision

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**activate_at** | **datetime** | Timestamp when the revision will be activated. | [optional] 
**account_id** | **int** | The ID of the account that owns this entity. | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**campaign_id** | **int** | The ID of the campaign that the revision was created from. | 
**created** | **datetime** | Timestamp when the revision was created. | 
**created_by** | **int** | The ID of the user who created this revision. | 
**activated_at** | **datetime** | Timestamp when this revision was activated. | [optional] 
**activated_by** | **int** | The ID of the user who activated this revision. | [optional] 
**current_version** | [**RevisionVersion**](RevisionVersion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


