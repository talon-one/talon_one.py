# UpdateCoupon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_limit** | **int** | The number of times a coupon code can be redeemed. This can be set to 0 for no limit, but any campaign usage limits will still apply.  | [optional] 
**discount_limit** | **float** | The amount of discounts that can be given with this coupon code.  | [optional] 
**start_date** | **datetime** | Timestamp at which point the coupon becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative. | [optional] 
**recipient_integration_id** | **str** | The integration ID for this coupon&#39;s beneficiary&#39;s profile | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


