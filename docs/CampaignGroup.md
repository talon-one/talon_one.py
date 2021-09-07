# CampaignGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of this campaign group. | 
**description** | **str** | A longer description of the campaign group. | [optional] 
**subscribed_applications_ids** | **list[int]** | A list of the IDs of the applications that this campaign group is enabled for | [optional] 
**campaign_ids** | **list[int]** | A list of the IDs of the campaigns that this campaign group owns | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


