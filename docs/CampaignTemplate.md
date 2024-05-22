# CampaignTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**user_id** | **int** | The ID of the user associated with this entity. | 
**name** | **str** | The campaign template name. | 
**description** | **str** | Customer-facing text that explains the objective of the template. | 
**instructions** | **str** | Customer-facing text that explains how to use the template. For example, you can use this property to explain the available attributes of this template, and how they can be modified when a user uses this template to create a new campaign. | 
**campaign_attributes** | [**object**](.md) | The campaign attributes that campaigns created from this template will have by default. | [optional] 
**coupon_attributes** | [**object**](.md) | The campaign attributes that coupons created from this template will have by default. | [optional] 
**state** | **str** | Only campaign templates in &#39;available&#39; state may be used to create campaigns. | 
**active_ruleset_id** | **int** | The ID of the ruleset this campaign template will use. | [optional] 
**tags** | **list[str]** | A list of tags for the campaign template. | [optional] 
**features** | **list[str]** | A list of features for the campaign template. | [optional] 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[TemplateLimitConfig]**](TemplateLimitConfig.md) | The set of limits that operate for this campaign template. | [optional] 
**template_params** | [**list[CampaignTemplateParams]**](CampaignTemplateParams.md) | Fields which can be used to replace values in a rule. | [optional] 
**applications_ids** | **list[int]** | A list of IDs of the Applications that are subscribed to this campaign template. | 
**campaign_collections** | [**list[CampaignTemplateCollection]**](CampaignTemplateCollection.md) | The campaign collections from the blueprint campaign for the template. | [optional] 
**default_campaign_group_id** | **int** | The default campaign group ID. | [optional] 
**campaign_type** | **str** | The campaign type. Possible type values:   - &#x60;cartItem&#x60;: Type of campaign that can apply effects only to cart items.   - &#x60;advanced&#x60;: Type of campaign that can apply effects to customer sessions and cart items.  | [default to 'advanced']
**updated** | **datetime** | Timestamp of the most recent update to the campaign template or any of its elements. | [optional] 
**updated_by** | **str** | Name of the user who last updated this campaign template, if available. | [optional] 
**valid_application_ids** | **list[int]** | The IDs of the Applications that are related to this entity. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


