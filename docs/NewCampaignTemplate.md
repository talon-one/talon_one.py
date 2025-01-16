# NewCampaignTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The campaign template name. | 
**description** | **str** | Customer-facing text that explains the objective of the template. | 
**instructions** | **str** | Customer-facing text that explains how to use the template. For example, you can use this property to explain the available attributes of this template, and how they can be modified when a user uses this template to create a new campaign. | 
**campaign_attributes** | [**object**](.md) | The campaign attributes that campaigns created from this template will have by default. | [optional] 
**coupon_attributes** | [**object**](.md) | The campaign attributes that coupons created from this template will have by default. | [optional] 
**state** | **str** | Only Campaign Templates in &#39;available&#39; state may be used to create Campaigns. | 
**tags** | **list[str]** | A list of tags for the campaign template. | [optional] 
**features** | **list[str]** | A list of features for the campaign template. | [optional] 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**coupon_reservation_settings** | [**CampaignTemplateCouponReservationSettings**](CampaignTemplateCouponReservationSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[TemplateLimitConfig]**](TemplateLimitConfig.md) | The set of limits that will operate for this campaign template. | [optional] 
**template_params** | [**list[CampaignTemplateParams]**](CampaignTemplateParams.md) | Fields which can be used to replace values in a rule. | [optional] 
**campaign_collections** | [**list[CampaignTemplateCollection]**](CampaignTemplateCollection.md) | The campaign collections from the blueprint campaign for the template. | [optional] 
**default_campaign_group_id** | **int** | The default campaign group ID. | [optional] 
**campaign_type** | **str** | The campaign type. Possible type values:   - &#x60;cartItem&#x60;: Type of campaign that can apply effects only to cart items.   - &#x60;advanced&#x60;: Type of campaign that can apply effects to customer sessions and cart items.  | [default to 'advanced']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


