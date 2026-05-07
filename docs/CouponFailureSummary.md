# CouponFailureSummary

Summary of the reasons for coupon redemption failure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the evaluation record. | 
**event_id** | **int** | ID of the event. | 
**session_id** | **str** | ID of the customer session set by your integration layer. | [optional] 
**profile_id** | **str** | ID of the customer profile set by your integration layer. | [optional] 
**status** | **str** | Status defines if the coupon code was applied or rejected. | 
**coupon_code** | **str** | Coupon code passed for evaluation. | 
**language** | **str** | Language of the summary. | 
**summary** | **str** | A summary of the reasons for coupon redemption failure. | 
**created_at** | **datetime** | Timestamp when the request was made. | 
**updated_at** | **datetime** | Timestamp when the request was last updated. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


