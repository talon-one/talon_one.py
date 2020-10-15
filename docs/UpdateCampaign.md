# UpdateCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A friendly name for this campaign. | 
**description** | **str** | A detailed description of the campaign. | [optional] 
**start_time** | **datetime** | Datetime when the campaign will become active. | [optional] 
**end_time** | **datetime** | Datetime when the campaign will become in-active. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign | [optional] 
**state** | **str** | A disabled or archived campaign is not evaluated for rules or coupons.  | [optional] [default to 'enabled']
**active_ruleset_id** | **int** | ID of Ruleset this campaign applies on customer session evaluation. | [optional] 
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | A list of features for the campaign. | 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | The set of limits that will operate for this campaign | 
**campaign_groups** | **list[int]** | The IDs of the campaign groups that own this entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


