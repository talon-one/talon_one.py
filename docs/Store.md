# Store

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**name** | **str** | The name of the store. | 
**description** | **str** | The description of the store. | 
**attributes** | [**object**](.md) | The attributes of the store. | [optional] 
**integration_id** | **str** | The integration ID of the store. You choose this ID when you create a store.  **Note**: You cannot edit the &#x60;integrationId&#x60; after the store has been created.  | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**updated** | **datetime** | Timestamp of the most recent update on this entity. | 
**linked_campaign_ids** | **list[int]** | A list of IDs of the campaigns that are linked with current store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


