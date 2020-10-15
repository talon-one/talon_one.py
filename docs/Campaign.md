# Campaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**user_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | A friendly name for this campaign. | 
**description** | **str** | A detailed description of the campaign. | 
**start_time** | **datetime** | Datetime when the campaign will become active. | [optional] 
**end_time** | **datetime** | Datetime when the campaign will become in-active. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign | [optional] 
**state** | **str** | A disabled or archived campaign is not evaluated for rules or coupons.  | [default to 'enabled']
**active_ruleset_id** | **int** | ID of Ruleset this campaign applies on customer session evaluation. | [optional] 
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | A list of features for the campaign. | 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | The set of limits that will operate for this campaign | 
**campaign_groups** | **list[int]** | The IDs of the campaign groups that own this entity. | [optional] 
**coupon_redemption_count** | **int** | Number of coupons redeemed in the campaign. | [optional] 
**referral_redemption_count** | **int** | Number of referral codes redeemed in the campaign. | [optional] 
**discount_count** | **int** | Total amount of discounts redeemed in the campaign. | [optional] 
**discount_effect_count** | **int** | Total number of times discounts were redeemed in this campaign. | [optional] 
**coupon_creation_count** | **int** | Total number of coupons created by rules in this campaign. | [optional] 
**last_activity** | **datetime** | Timestamp of the most recent event received by this campaign. | [optional] 
**updated** | **datetime** | Timestamp of the most recent update to the campaign or any of its elements. | [optional] 
**created_by** | **str** | Name of the user who created this campaign if available. | [optional] 
**updated_by** | **str** | Name of the user who last updated this campaign if available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


