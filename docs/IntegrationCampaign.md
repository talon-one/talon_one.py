# IntegrationCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID of Campaign. | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**name** | **str** | A user-facing name for this campaign. | 
**description** | **str** | A detailed description of the campaign. | [optional] 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp when the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**state** | **str** | The state of the campaign.  | [default to 'enabled']
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | The features enabled in this campaign. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


