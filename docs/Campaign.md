# Campaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**user_id** | **int** | The ID of the user associated with this entity. | 
**name** | **str** | A user-facing name for this campaign. | 
**description** | **str** | A detailed description of the campaign. | 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**state** | **str** | A disabled or archived campaign is not evaluated for rules or coupons.  | [default to 'enabled']
**active_ruleset_id** | **int** | [ID of Ruleset](https://docs.talon.one/management-api#operation/getRulesets) this campaign applies on customer session evaluation.  | [optional] 
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | The features enabled in this campaign. | 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | The set of [budget limits](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets) for this campaign.  | 
**campaign_groups** | **list[int]** | The IDs of the [campaign groups](https://docs.talon.one/docs/product/account/managing-campaign-groups) this campaign belongs to.  | [optional] 
**coupon_redemption_count** | **int** | Number of coupons redeemed in the campaign. | [optional] 
**referral_redemption_count** | **int** | Number of referral codes redeemed in the campaign. | [optional] 
**discount_count** | **float** | Total amount of discounts redeemed in the campaign. | [optional] 
**discount_effect_count** | **int** | Total number of times discounts were redeemed in this campaign. | [optional] 
**coupon_creation_count** | **int** | Total number of coupons created by rules in this campaign. | [optional] 
**custom_effect_count** | **int** | Total number of custom effects triggered by rules in this campaign. | [optional] 
**referral_creation_count** | **int** | Total number of referrals created by rules in this campaign. | [optional] 
**add_free_item_effect_count** | **int** | Total number of times triggering add free item effext is allowed in this campaign. | [optional] 
**awarded_giveaways_count** | **int** | Total number of giveaways awarded by rules in this campaign. | [optional] 
**created_loyalty_points_count** | **float** | Total number of loyalty points created by rules in this campaign. | [optional] 
**created_loyalty_points_effect_count** | **int** | Total number of loyalty point creation effects triggered by rules in this campaign. | [optional] 
**redeemed_loyalty_points_count** | **float** | Total number of loyalty points redeemed by rules in this campaign. | [optional] 
**redeemed_loyalty_points_effect_count** | **int** | Total number of loyalty point redemption effects triggered by rules in this campaign. | [optional] 
**call_api_effect_count** | **int** | Total number of webhook triggered by rules in this campaign. | [optional] 
**reservecoupon_effect_count** | **int** | Total number of reserve coupon effects triggered by rules in this campaign. | [optional] 
**last_activity** | **datetime** | Timestamp of the most recent event received by this campaign. | [optional] 
**updated** | **datetime** | Timestamp of the most recent update to the campaign&#39;s property. Updates to external entities used in this campaign are **not** registered by this property, such as collection or coupon updates.  | [optional] 
**created_by** | **str** | Name of the user who created this campaign if available. | [optional] 
**updated_by** | **str** | Name of the user who last updated this campaign if available. | [optional] 
**template_id** | **int** | The ID of the Campaign Template this Campaign was created from. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


