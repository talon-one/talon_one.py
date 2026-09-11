# NewExperiment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_variant_assignment_external** | **bool** | The source of the assignment. - false - The variant assignment is handled internally by Talon.One. - true - The variant assignment is handled externally.  | 
**campaign** | [**NewCampaign**](NewCampaign.md) |  | 
**goal_type** | **str** | The goal of the experiment. Determines which single metric is used to decide the winning variant. When set to &#x60;other&#x60;, multiple metrics are used.  | [default to 'other']
**goal_description** | **str** | A description of the experiment goal. Provides context for the AI summary and helps it interpret the outcome of the experiment against the stated goal.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


