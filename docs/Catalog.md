# Catalog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**name** | **str** | The cart item catalog name. | 
**description** | **str** | A description of this cart item catalog. | 
**subscribed_applications_ids** | **list[int]** | A list of the IDs of the applications that are subscribed to this catalog. | [optional] 
**version** | **int** | The current version of this catalog. | 
**created_by** | **int** | The ID of user who created this catalog. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


