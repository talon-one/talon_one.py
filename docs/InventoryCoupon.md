# InventoryCoupon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | 
**value** | **str** | The coupon code. | 
**usage_limit** | **int** | The number of times the coupon code can be redeemed. &#x60;0&#x60; means unlimited redemptions but any campaign usage limits will still apply.  | 
**discount_limit** | **float** | The total discount value that the code can give. Typically used to represent a gift card value.  | [optional] 
**reservation_limit** | **int** | The number of reservations that can be made with this coupon code.  | [optional] 
**start_date** | **datetime** | Timestamp at which point the coupon becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiration date of the coupon. Coupon never expires if this is omitted. | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Limits configuration for a coupon. These limits will override the limits set from the campaign.  **Note:** Only usable when creating a single coupon which is not tied to a specific recipient. Only per-profile limits are allowed to be configured.  | [optional] 
**usage_counter** | **int** | The number of times the coupon has been successfully redeemed. | 
**discount_counter** | **float** | The amount of discounts given on rules redeeming this coupon. Only usable if a coupon discount budget was set for this coupon. | [optional] 
**discount_remainder** | **float** | The remaining discount this coupon can give. | [optional] 
**reservation_counter** | **float** | The number of times this coupon has been reserved. | [optional] 
**attributes** | [**object**](.md) | Custom attributes associated with this coupon. | [optional] 
**referral_id** | **int** | The integration ID of the referring customer (if any) for whom this coupon was created as an effect. | [optional] 
**recipient_integration_id** | **str** | The Integration ID of the customer that is allowed to redeem this coupon. | [optional] 
**import_id** | **int** | The ID of the Import which created this coupon. | [optional] 
**reservation** | **bool** | Defines the reservation type: - &#x60;true&#x60;: The coupon can be reserved for multiple customers. - &#x60;false&#x60;: The coupon can be reserved only for one customer. It is a personal code.  | [optional] [default to True]
**batch_id** | **str** | The id of the batch the coupon belongs to. | [optional] 
**is_reservation_mandatory** | **bool** | An indication of whether the code can be redeemed only if it has been reserved first. | [optional] [default to False]
**implicitly_reserved** | **bool** | An indication of whether the coupon is implicitly reserved for all customers. | [optional] 
**profile_redemption_count** | **int** | The number of times the coupon was redeemed by the profile. | 
**state** | **str** | Can be:  - &#x60;active&#x60;: The coupon can be used. It is a reserved coupon that is not pending, used, or expired, and it has a non-exhausted limit counter.    **Note:** This coupon state is returned for [scheduled campaigns](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-schedule), but the coupon cannot be used until the campaign is **running**. - &#x60;used&#x60;: The coupon has been redeemed and cannot be used again. It is not pending and has reached its redemption limit or was redeemed by the profile before expiration. - &#x60;expired&#x60;: The coupon was never redeemed, and it is now expired. It is non-pending, non-active, and non-used by the profile. - &#x60;pending&#x60;: The coupon will be usable in the future. - &#x60;disabled&#x60;: The coupon is part of a non-active campaign.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


