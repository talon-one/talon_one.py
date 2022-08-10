# CampaignCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**description** | **str** | A short description of the purpose of this collection. | [optional] 
**name** | **str** | The name of this collection. | 
**modified_by** | **int** | ID of the user who last updated this effect if available. | [optional] 
**created_by** | **int** | ID of the user who created this effect. | 
**application_id** | **int** | The ID of the Application that owns this entity. | [optional] 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | [optional] 
**payload** | **list[str]** | The content of the collection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


