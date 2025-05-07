# Campaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**user_id** | **int** | The ID of the user associated with this entity. | 
**name** | **str** | A user-facing name for this campaign. | 
**description** | **str** | A detailed description of the campaign. | 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp when the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**state** | **str** | A disabled or archived campaign is not evaluated for rules or coupons.  | [default to 'enabled']
**active_ruleset_id** | **int** | [ID of Ruleset](https://docs.talon.one/management-api#operation/getRulesets) this campaign applies on customer session evaluation.  | [optional] 
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | The features enabled in this campaign. | 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | The set of [budget limits](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets) for this campaign.  | 
**campaign_groups** | **list[int]** | The IDs of the [campaign groups](https://docs.talon.one/docs/product/account/managing-campaign-groups) this campaign belongs to.  | [optional] 
**type** | **str** | The campaign type. Possible type values:   - &#x60;cartItem&#x60;: Type of campaign that can apply effects only to cart items.   - &#x60;advanced&#x60;: Type of campaign that can apply effects to customer sessions and cart items.  | [default to 'advanced']
**linked_store_ids** | **list[int]** | A list of store IDs that you want to link to the campaign.  **Note:** Campaigns with linked store IDs will only be evaluated when there is a [customer session update](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/updateCustomerSessionV2) that references a linked store.  | [optional] 
**budgets** | [**list[CampaignBudget]**](CampaignBudget.md) | A list of all the budgets that are defined by this campaign and their usage.  **Note:** Budgets that are not defined do not appear in this list and their usage is not counted until they are defined.  | [optional] 
**coupon_redemption_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Number of coupons redeemed in the campaign.  | [optional] 
**referral_redemption_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Number of referral codes redeemed in the campaign.  | [optional] 
**discount_count** | **float** | This property is **deprecated**. The count should be available under *budgets* property. Total amount of discounts redeemed in the campaign.  | [optional] 
**discount_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of times discounts were redeemed in this campaign.  | [optional] 
**coupon_creation_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of coupons created by rules in this campaign.  | [optional] 
**custom_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of custom effects triggered by rules in this campaign.  | [optional] 
**referral_creation_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of referrals created by rules in this campaign.  | [optional] 
**add_free_item_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of times the [add free item effect](https://docs.talon.one/docs/dev/integration-api/api-effects#addfreeitem) can be triggered in this campaign.  | [optional] 
**awarded_giveaways_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of giveaways awarded by rules in this campaign.  | [optional] 
**created_loyalty_points_count** | **float** | This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty points created by rules in this campaign.  | [optional] 
**created_loyalty_points_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty point creation effects triggered by rules in this campaign.  | [optional] 
**redeemed_loyalty_points_count** | **float** | This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty points redeemed by rules in this campaign.  | [optional] 
**redeemed_loyalty_points_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty point redemption effects triggered by rules in this campaign.  | [optional] 
**call_api_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of webhooks triggered by rules in this campaign.  | [optional] 
**reservecoupon_effect_count** | **int** | This property is **deprecated**. The count should be available under *budgets* property. Total number of reserve coupon effects triggered by rules in this campaign.  | [optional] 
**last_activity** | **datetime** | Timestamp of the most recent event received by this campaign. | [optional] 
**updated** | **datetime** | Timestamp of the most recent update to the campaign&#39;s property. Updates to external entities used in this campaign are **not** registered by this property, such as collection or coupon updates.  | [optional] 
**created_by** | **str** | Name of the user who created this campaign if available. | [optional] 
**updated_by** | **str** | Name of the user who last updated this campaign if available. | [optional] 
**template_id** | **int** | The ID of the Campaign Template this Campaign was created from. | [optional] 
**frontend_state** | **str** | The campaign state displayed in the Campaign Manager. | 
**stores_imported** | **bool** | Indicates whether the linked stores were imported via a CSV file. | 
**value_maps_ids** | **list[int]** | A list of value map IDs for the campaign. | [optional] 
**revision_frontend_state** | **str** | The campaign revision state displayed in the Campaign Manager. | [optional] 
**active_revision_id** | **int** | ID of the revision that was last activated on this campaign.  | [optional] 
**active_revision_version_id** | **int** | ID of the revision version that is active on the campaign.  | [optional] 
**version** | **int** | Incrementing number representing how many revisions have been activated on this campaign, starts from 0 for a new campaign.  | [optional] 
**current_revision_id** | **int** | ID of the revision currently being modified for the campaign.  | [optional] 
**current_revision_version_id** | **int** | ID of the latest version applied on the current revision.  | [optional] 
**stage_revision** | **bool** | Flag for determining whether we use current revision when sending requests with staging API key.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


