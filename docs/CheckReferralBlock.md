# CheckReferralBlock

A block that validates the referral code value and date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**redeem** | **bool** | When &#x60;true&#x60;, the referral code is redeemed. | 
**on_failure** | **list[object]** | Promotion blocks evaluated when this block fails or returns false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


