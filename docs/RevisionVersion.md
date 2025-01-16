# RevisionVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**account_id** | **int** |  | 
**application_id** | **int** |  | 
**campaign_id** | **int** |  | 
**created** | **datetime** |  | 
**created_by** | **int** |  | 
**revision_id** | **int** |  | 
**version** | **int** |  | 
**name** | **str** | A user-facing name for this campaign. | [optional] 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp when the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**description** | **str** | A detailed description of the campaign. | [optional] 
**active_ruleset_id** | **int** | The ID of the ruleset this campaign template will use. | [optional] 
**tags** | **list[str]** | A list of tags for the campaign template. | [optional] 
**coupon_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**referral_settings** | [**CodeGeneratorSettings**](CodeGeneratorSettings.md) |  | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | The set of limits that will operate for this campaign version. | [optional] 
**features** | **list[str]** | A list of features for the campaign template. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


