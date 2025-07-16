# PriceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**account_id** | **int** | The ID of the account that owns this price type. | [optional] 
**name** | **str** | The API name of the price type. This is an immutable value. | 
**title** | **str** | The title of the price type. | 
**description** | **str** | The description of the price type. | [optional] 
**modified** | **datetime** | The date and time when the price type was last modified. | 
**subscribed_catalogs_ids** | **list[int]** | A list of the IDs of the catalogs that are subscribed to this price type. | 
**targeted_audiences_ids** | **list[int]** | A list of the IDs of the audiences that are targeted by this price type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


