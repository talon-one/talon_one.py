# RuleFailureReason

Details about why a rule failed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | The ID of the campaign that contains the rule that failed. | 
**campaign_name** | **str** | The name of the campaign that contains the rule that failed. | 
**ruleset_id** | **int** | The ID of the ruleset that contains the rule that failed. | 
**coupon_id** | **int** | The ID of the coupon that was being evaluated at the time of the rule failure. | [optional] 
**coupon_value** | **str** | The code of the coupon that was being evaluated at the time of the rule failure. | [optional] 
**referral_id** | **int** | The ID of the referral that was being evaluated at the time of the rule failure. | [optional] 
**referral_value** | **str** | The code of the referral that was being evaluated at the time of the rule failure. | [optional] 
**rule_index** | **int** | The index of the rule that failed within the ruleset. | 
**rule_name** | **str** | The name of the rule that failed within the ruleset. | 
**condition_index** | **int** | The index of the condition that failed. | [optional] 
**effect_index** | **int** | The index of the effect that failed. | [optional] 
**details** | **str** | More details about the failure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


