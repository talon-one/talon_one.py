# RejectCouponEffectProps

The properties specific to the \"rejectCoupon\" effect. This gets triggered whenever the coupon was rejected. See rejectionReason for more info on why.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The coupon code that was rejected. | 
**rejection_reason** | **str** | The reason why this coupon was rejected. | 
**condition_index** | **int** | The index of the condition that caused the rejection of the coupon. | [optional] 
**effect_index** | **int** | The index of the effect that caused the rejection of the coupon. | [optional] 
**details** | **str** | More details about the failure. | [optional] 
**campaign_exclusion_reason** | **str** | The reason why the campaign was not applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


