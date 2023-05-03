# NewReferralsForMultipleAdvocates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Timestamp at which point the referral code becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiration date of the referral code. Referral never expires if this is omitted, zero, or negative. | [optional] 
**usage_limit** | **int** | The number of times a referral code can be used. &#x60;0&#x60; means no limit but any campaign usage limits will still apply.  | 
**campaign_id** | **int** | The ID of the campaign from which the referral received the referral code. | 
**advocate_profile_integration_ids** | **list[str]** | An array containing all the respective advocate profiles. | 
**attributes** | [**object**](.md) | Arbitrary properties associated with this referral code. | [optional] 
**valid_characters** | **list[str]** | List of characters used to generate the random parts of a code. By default, the list of characters is equivalent to the &#x60;[A-Z, 0-9]&#x60; regular expression.  | [optional] 
**referral_pattern** | **str** | The pattern used to generate referrals. The character &#x60;#&#x60; is a placeholder and is replaced by a random character from the &#x60;validCharacters&#x60; set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


