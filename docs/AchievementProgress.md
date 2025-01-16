# AchievementProgress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievement_id** | **int** | The internal ID of the achievement. | 
**name** | **str** | The internal name of the achievement used in API requests.  | 
**title** | **str** | The display name of the achievement in the Campaign Manager. | 
**description** | **str** | The description of the achievement in the Campaign Manager. | 
**campaign_id** | **int** | The ID of the campaign the achievement belongs to. | 
**status** | **str** | The status of the achievement. | 
**target** | **float** | The required number of actions or the transactional milestone to complete the achievement. | [optional] 
**progress** | **float** | The current progress of the customer in the achievement. | 
**start_date** | **datetime** | Timestamp at which the customer started the achievement. | 
**completion_date** | **datetime** | Timestamp at which point the customer completed the achievement. | [optional] 
**end_date** | **datetime** | Timestamp at which point the achievement ends and resets for the customer. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


