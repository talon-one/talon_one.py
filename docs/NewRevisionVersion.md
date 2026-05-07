# NewRevisionVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A user-facing name for this campaign. | [optional] 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp when the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**description** | **str** | A detailed description of the campaign. | [optional] 
**active_ruleset_id** | **int** | The ID of the ruleset this campaign will use. | [optional] 
**tags** | **list[str]** | A list of tags for the campaign. | [optional] 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | The set of limits that will operate for this campaign version. | [optional] 
**reevaluate_on_return** | **bool** | Indicates whether this campaign should be reevaluated when a customer returns an item. | [optional] 
**features** | **list[str]** | A list of features for the campaign. | [optional] 
**coupon_attributes** | [**object**](.md) | Arbitrary properties associated with coupons in this campaign. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


