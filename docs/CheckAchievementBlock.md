# CheckAchievementBlock

A block that checks the current customer's completion or progress status in an achievement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**operator** | **str** | The comparison operator applied to the achievement. | 
**achievement** | [**CheckAchievementBlockAchievement**](CheckAchievementBlockAchievement.md) |  | 
**on_failure** | **list[object]** | Promotion blocks evaluated when this block fails or returns false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


