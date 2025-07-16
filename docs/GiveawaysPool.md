# GiveawaysPool

Giveaways pools is an entity for managing multiple similar giveaways.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of this giveaways pool. | 
**description** | **str** | The description of this giveaways pool. | [optional] 
**subscribed_applications_ids** | **list[int]** | A list of the IDs of the applications that this giveaways pool is enabled for. | [optional] 
**sandbox** | **bool** | Indicates if this program is a live or sandbox program. Programs of a given type can only be connected to Applications of the same type. | 
**modified** | **datetime** | Timestamp of the most recent update to the giveaways pool. | [optional] 
**created_by** | **int** | ID of the user who created this giveaways pool. | 
**modified_by** | **int** | ID of the user who last updated this giveaways pool if available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


