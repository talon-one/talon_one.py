# IncreaseAchievementProgressEffectProps

The properties specific to the \"increaseAchievementProgress\" effect. This gets triggered whenever a validated rule contained an \"increase customer progress\" effect.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievement_id** | **int** | The internal ID of the achievement. | 
**achievement_name** | **str** | The name of the achievement. | 
**progress_tracker_id** | **int** | The internal ID of the achievement progress tracker. | [optional] 
**delta** | **float** | The value by which the customer&#39;s current progress in the achievement is increased. | 
**value** | **float** | The current progress of the customer in the achievement. | 
**target** | **float** | The target value to complete the achievement. | 
**is_just_completed** | **bool** | Indicates if the customer has completed the achievement in the current session. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


