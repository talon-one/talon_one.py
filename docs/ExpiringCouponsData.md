# ExpiringCouponsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_value** | **str** | The coupon code. | 
**created_date** | **datetime** | Timestamp at which point the coupon was created. | [optional] 
**valid_from** | **datetime** | Timestamp at which point the coupon becomes valid. | [optional] 
**valid_until** | **datetime** | Timestamp at which point the coupon expires. Coupon never expires if this is omitted, zero, or negative. | [optional] 
**campaign_id** | **int** | The ID of the campaign to which the coupon belongs. | 
**customer_profile_id** | **str** | The Integration ID of the customer that is allowed to redeem this coupon. | [optional] 
**usage_limit** | **int** | The number of times the coupon code can be redeemed. &#x60;0&#x60; means unlimited redemptions but any campaign usage limits will still apply.  | 
**usage_counter** | **int** | The number of times the coupon has been successfully redeemed. | 
**batch_id** | **str** | The ID of the batch the coupon belongs to. | [optional] 
**attributes** | [**object**](.md) | Custom attributes associated with this coupon. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


