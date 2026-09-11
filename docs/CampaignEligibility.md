# CampaignEligibility

A list of campaigns and their evaluation status for the current customer session.  For experiment campaigns, the experiment and variant assigned to the customer profile are returned through the `experiment` field. Customer profiles with no variant assignment are not included.  **Note**:  - This response can **only** be included if the `dry` parameter in the query is set to `true`.  - Do not include `triggeredCampaigns` or `ruleFailureReasons` in `responseContent` to avoid duplicate results. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **int** | The ID of the Application that owns this entity. | 
**id** | **int** | Unique ID of Campaign. | 
**name** | **str** | The name of the campaign. | 
**description** | **str** | A detailed description of the campaign. | [optional] 
**start_time** | **datetime** | Timestamp when the campaign will become active. | [optional] 
**end_time** | **datetime** | Timestamp when the campaign will become inactive. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 
**state** | **str** | The state of the campaign.  | [default to 'enabled']
**tags** | **list[str]** | A list of tags for the campaign. | 
**features** | **list[str]** | The features enabled in this campaign. | 
**eligibility** | [**list[CampaignEligibilityDetails]**](CampaignEligibilityDetails.md) | The customer&#39;s eligibility for each campaign in the current customer session. | 
**rules** | [**list[RuleMetadataEligibility]**](RuleMetadataEligibility.md) | A list of rules containing customer-facing details of the rewards defined in the campaign. | 
**experiment** | [**CampaignEligibilityExperiment**](CampaignEligibilityExperiment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


