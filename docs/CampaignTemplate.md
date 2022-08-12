# CampaignTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**user_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The campaign template name. | 
**description** | **str** | Customer-facing text that explains the objective of the template. | 
**instructions** | **str** | Customer-facing text that explains how to use the template. For example, you can use this property to explain the available attributes of this template, and how they can be modified when a user uses this template to create a new campaign. | 
**campaign_attributes** | [**object**](.md) | The Campaign Attributes that Campaigns created from this template will have by default. | [optional] 
**coupon_attributes** | [**object**](.md) | The Campaign Attributes that Coupons created from this template will have by default. | [optional] 
**state** | **str** | Only Campaign Templates in &#39;available&#39; state may be used to create Campaigns. | 
**active_ruleset_id** | **int** | The ID of the Ruleset this Campaign Template will use. | [optional] 
**tags** | **list[str]** | A list of tags for the campaign template. | [optional] 
**features** | **list[str]** | A list of features for the campaign template. | [optional] 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[TemplateLimitConfig]**](TemplateLimitConfig.md) | The set of limits that will operate for this campaign template. | [optional] 
**template_params** | [**list[CampaignTemplateParams]**](CampaignTemplateParams.md) | Template parameters are fields which can be used to replace values in a rule. | [optional] 
**applications_ids** | **list[int]** | A list of the IDs of the applications that are subscribed to this campaign template. A list of the IDs of the applications that are subscribed to this campaign template. | 
**campaign_collections** | [**list[CampaignTemplateCollection]**](CampaignTemplateCollection.md) | The campaign collections from the blueprint campaign for the template. | [optional] 
**default_campaign_group_id** | **int** | The default campaignGroupId. | [optional] 
**updated** | **datetime** | Timestamp of the most recent update to the campaign template or any of its elements. | [optional] 
**updated_by** | **str** | Name of the user who last updated this campaign template if available. | [optional] 
**valid_application_ids** | **list[int]** | The IDs of the applications that are related to this entity. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


