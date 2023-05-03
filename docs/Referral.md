# Referral


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**start_date** | **datetime** | Timestamp at which point the referral code becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiration date of the referral code. Referral never expires if this is omitted, zero, or negative. | [optional] 
**usage_limit** | **int** | The number of times a referral code can be used. &#x60;0&#x60; means no limit but any campaign usage limits will still apply.  | 
**campaign_id** | **int** | ID of the campaign from which the referral received the referral code. | 
**advocate_profile_integration_id** | **str** | The Integration ID of the Advocate&#39;s Profile. | 
**friend_profile_integration_id** | **str** | An optional Integration ID of the Friend&#39;s Profile. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this item. | [optional] 
**import_id** | **int** | The ID of the Import which created this referral. | [optional] 
**code** | **str** | The referral code. | 
**usage_counter** | **int** | The number of times this referral code has been successfully used. | 
**batch_id** | **str** | The ID of the batch the referrals belong to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


