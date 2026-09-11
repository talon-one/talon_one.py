# CustomerProfileReward

A reward instance held by a customer profile.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the customer reward instance. A customer profile can have multiple instances of the same reward. | 
**integration_id** | **str** | The integration ID of the customer reward instance. | 
**reward_id** | **int** | The ID of the reward this instance belongs to. | 
**reward_integration_id** | **str** | The integration ID of the reward this instance belongs to. | 
**reward_name** | **str** | The name of the reward. | 
**description** | **str** | The customer-facing description of the reward. | [optional] 
**rule** | [**RuleMetadata**](RuleMetadata.md) |  | [optional] 
**status** | **str** | The status of the customer reward: - &#x60;unlocked&#x60;: The reward is available for use. - &#x60;used&#x60;: The reward has been used.  | 
**unlocked_at** | **datetime** | The date and time when the reward was unlocked. | 
**unlocked_by_profile_integration_id** | **str** | The integration ID of the customer profile that unlocked the reward.   For rewards unlocked with a loyalty card, this can be any customer profile  linked to that loyalty card.  | [optional] 
**used_at** | **datetime** | The date and time when the reward was used. | [optional] 
**used_by_profile_integration_id** | **str** | The integration ID of the customer profile that used the reward.   For rewards unlocked with a loyalty card, this can be any customer profile  linked to that loyalty card.   Only returned when the reward has been used.  | [optional] 
**loyalty_program_id** | **int** | The ID of the loyalty program that the loyalty card belongs to. Only returned for rewards unlocked with a loyalty card. | [optional] 
**loyalty_card_identifier** | **str** | The identifier of the loyalty card, which must match the regular expression &#x60;^[A-Za-z0-9._%+@-]+$&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


