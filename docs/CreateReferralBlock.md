# CreateReferralBlock

A block that creates a referral code.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**campaign_id** | [**object**](.md) | The ID of the campaign in which the referral code is created. Either a numeric scalar or a &#x60;{{expression}}&#x60; string that resolves to a number at evaluation time. | 
**friend_id** | **str** | An optional integration ID of the friend&#39;s profile. | 
**store_in_session** | **bool** | When &#x60;true&#x60;, the referral code is stored in the session. | 
**usage_limit** | [**object**](.md) | The number of times the referral code code can be redeemed. &#x60;0&#x60; means unlimited redemptions, but any campaign usage limits still apply. Either a numeric scalar or a &#x60;{{expression}}&#x60; string that resolves to a number at evaluation time.  | [optional] 
**start_date** | [**object**](.md) | Timestamp at which point the referral code becomes valid. | [optional] 
**expiry_date** | [**object**](.md) | Expiration date of the referral code. Referral code never expires if this is omitted. | [optional] 
**attributes** | [**object**](.md) | Custom attributes associated with this referral code. | [optional] 
**valid_characters** | **str** | Characters used to generate the random parts of a code. | [optional] 
**pattern** | **str** | The pattern used to generate codes, such as coupon codes, referral codes, and loyalty cards. The character &#x60;#&#x60; is a placeholder and is replaced by a random character from the &#x60;validCharacters&#x60; set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


