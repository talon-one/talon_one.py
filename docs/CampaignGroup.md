# CampaignGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**modified** | **datetime** | The time this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of the campaign access group. | 
**description** | **str** | A longer description of the campaign access group. | [optional] 
**subscribed_applications_ids** | **list[int]** | A list of IDs of the Applications that this campaign access group is enabled for. | [optional] 
**campaign_ids** | **list[int]** | A list of IDs of the campaigns that are part of the campaign access group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


