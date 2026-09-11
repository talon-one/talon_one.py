# RewardCatalogItem

A reward returned by the rewards catalog Integration API endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID of the reward. | 
**name** | **str** | The customer-facing name of the reward. | 
**description** | **str** | The customer-facing description of the reward. | [optional] 
**points_required** | [**list[RewardPointsRequired]**](RewardPointsRequired.md) | The loyalty points required to activate the reward. | [optional] 
**rule** | [**RuleMetadata**](RuleMetadata.md) |  | 
**eligibility** | [**RewardEligibility**](RewardEligibility.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


