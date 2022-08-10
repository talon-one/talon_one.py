# CouponCreationJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**usage_limit** | **int** | The number of times the coupon code can be redeemed. &#x60;0&#x60; means unlimited redemptions but any campaign usage limits will still apply.  | 
**discount_limit** | **float** | The amount of discounts that can be given with this coupon code.  | [optional] 
**start_date** | **datetime** | Timestamp at which point the coupon becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative. | [optional] 
**number_of_coupons** | **int** | The number of new coupon codes to generate for the campaign. Must be between 20,001 and 5,000,000. | 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with coupons. | 
**batch_id** | **str** | The batch ID coupons created by this job will bear. | 
**status** | **str** | The current status of this request. Possible values: - &#x60;pending&#x60; - &#x60;completed&#x60; - &#x60;failed&#x60; - &#x60;coupon pattern full&#x60;  | 
**created_amount** | **int** | The number of coupon codes that were already created for this request. | 
**fail_count** | **int** | The number of times this job failed. | 
**errors** | **list[str]** | An array of individual problems encountered during the request. | 
**created_by** | **int** | ID of the user who created this effect. | 
**communicated** | **bool** | Whether or not the user that created this job was notified of its final state. | 
**chunk_execution_count** | **int** | The number of times an attempt to create a chunk of coupons was made during the processing of the job. | 
**chunk_size** | **int** | The number of coupons that will be created in a single transactions. Coupons will be created in chunks until arriving at the requested amount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


