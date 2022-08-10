# CreateTemplateCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A user-facing name for this campaign. | 
**description** | **str** | A detailed description of the campaign. | [optional] 
**template_id** | **int** | The ID of the Campaign Template which will be used in order to create the Campaign. | 
**campaign_attributes_overrides** | [**object**](.md) | Custom Campaign Attributes. If the Campaign Template defines the same values, they will be overridden. | [optional] 
**template_param_values** | [**list[Binding]**](Binding.md) | Actual values to replace the template placeholder values in the Ruleset bindings. Values for all Template Parameters must be provided. | [optional] 
**limit_overrides** | [**list[LimitConfig]**](LimitConfig.md) | Limits for this Campaign. If the Campaign Template or Application define default values for the same limits, they will be overridden. | [optional] 
**campaign_groups** | **list[int]** | The IDs of the [campaign groups](https://docs.talon.one/docs/product/account/managing-campaign-groups/) this campaign belongs to.  | [optional] 
**tags** | **list[str]** | A list of tags for the campaign. If the campaign template has tags, they will be overridden by this list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


