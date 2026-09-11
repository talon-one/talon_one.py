# UnlockRewardEffectProps

The properties specific to the \"unlockReward\" effect. This gets triggered whenever a validated rule unlocks a reward for a customer profile.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The integration ID assigned to the customer reward unlock. | 
**reward_id** | **int** | The internal ID of the reward that was unlocked. | 
**application_id** | **int** | The internal ID of the application the reward belongs to. | 
**profile_integration_id** | **str** | The integration ID of the customer profile that unlocked the reward. | 
**unlocked_at** | **datetime** | The time the reward was unlocked. | 
**card_identifier** | **str** | The identifier of the loyalty card, which must match the regular expression &#x60;^[A-Za-z0-9._%+@-]+$&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


