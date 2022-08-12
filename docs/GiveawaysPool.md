# GiveawaysPool

Giveaways pools is an entity for managing multiple similar giveaways.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of this giveaways pool. | 
**description** | **str** | The description of this giveaways pool. | [optional] 
**subscribed_applications_ids** | **list[int]** | A list of the IDs of the applications that this giveaways pool is enabled for. | [optional] 
**modified** | **datetime** | Timestamp of the most recent update to the giveaways pool. | [optional] 
**created_by** | **int** | ID of the user who created this giveaways pool. | 
**modified_by** | **int** | ID of the user who last updated this giveaways pool if available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


