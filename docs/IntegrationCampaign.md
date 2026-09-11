# IntegrationCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **int** | The ID of the Application that owns this entity. | 
**id** | **int** | Unique ID of Campaign. | 
**name** | **str** | The name of the campaign. | 
**description** | **str** | A detailed description of the campaign. | [optional] 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp when the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**state** | **str** | The state of the campaign.  | [default to 'enabled']
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | The features enabled in this campaign. | 
**rules** | [**list[RuleMetadata]**](RuleMetadata.md) | A list of rules containing customer-facing details of the rewards defined in the campaign. | 
**linked_store_ids** | **list[int]** | A list of store IDs linked to this campaign. | [optional] 
**linked_audience_ids** | **list[int]** | A list of audience IDs linked to this campaign. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


