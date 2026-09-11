# RewardWithUnlocks

A reward and details of each time a customer profile has unlocked it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID of the reward. | 
**integration_id** | **str** | A unique identifier used to reference the reward in API integrations. | 
**name** | **str** | The customer-facing name of the reward. | 
**description** | **str** | Customer-facing description of the reward. | [optional] 
**rule** | [**RuleMetadata**](RuleMetadata.md) |  | 
**unlocked** | [**list[CustomerReward]**](CustomerReward.md) | The customer profile&#39;s unlocks of this reward that are not yet &#x60;used&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


