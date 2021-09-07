# NewReferral

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Timestamp at which point the referral code becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiry date of the referral code. Referral never expires if this is omitted, zero, or negative. | [optional] 
**usage_limit** | **int** | The number of times a referral code can be used. This can be set to 0 for no limit, but any campaign usage limits will still apply.  | [optional] 
**campaign_id** | **int** | ID of the campaign from which the referral received the referral code. | 
**advocate_profile_integration_id** | **str** | The Integration ID of the Advocate&#39;s Profile. | 
**friend_profile_integration_id** | **str** | An optional Integration ID of the Friend&#39;s Profile | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


