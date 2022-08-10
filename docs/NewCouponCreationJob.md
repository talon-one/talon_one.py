# NewCouponCreationJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_limit** | **int** | The number of times the coupon code can be redeemed. &#x60;0&#x60; means unlimited redemptions but any campaign usage limits will still apply.  | 
**discount_limit** | **float** | The amount of discounts that can be given with this coupon code.  | [optional] 
**start_date** | **datetime** | Timestamp at which point the coupon becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative. | [optional] 
**number_of_coupons** | **int** | The number of new coupon codes to generate for the campaign. Must be between 20,001 and 5,000,000. | 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with coupons. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


