# RuleEligibilityFailureDetails

The details about why the customer was not eligible for the rule in the current session.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_code** | **str** | A code identifying why the customer was not eligible for the rule in the current session. | 
**coupon_id** | **int** | The ID of the coupon that was being evaluated when the rule failed.  | [optional] 
**coupon_value** | **str** | The coupon code that was being evaluated when the rule failed.  | [optional] 
**referral_id** | **int** | The ID of the referral that was being evaluated when the rule failed.  | [optional] 
**referral_value** | **str** | The referral code that was being evaluated when the rule failed.  | [optional] 
**condition_index** | **int** | The index of the condition that caused the rule to fail. | [optional] 
**effect_index** | **int** | The index of the effect that caused the rule to fail. | [optional] 
**rule_index** | **int** | The index of the rule that failed within the ruleset. | [optional] 
**ruleset_id** | **int** | The ID of the ruleset containing the rule that failed. | [optional] 
**details** | **str** | Additional details about the failure. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


