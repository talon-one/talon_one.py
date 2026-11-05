# NewExperiment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | **str** | Controls how customers are assigned to experiment variants. Either &#x60;assignmentType&#x60; or &#x60;isVariantAssignmentExternal&#x60; must be provided; &#x60;assignmentType&#x60; takes priority when both are present. - &#x60;random&#x60;: Talon.One assigns customers randomly based on variant weights. - &#x60;external&#x60;: Variant assignment is handled externally. - &#x60;audience&#x60;: Each variant targets a specific audience; customers are   assigned based on audience membership.  | [optional] 
**is_variant_assignment_external** | **bool** | Deprecated. Use &#x60;assignmentType&#x60; instead. Either &#x60;assignmentType&#x60; or &#x60;isVariantAssignmentExternal&#x60; must be provided. - false - The variant assignment is handled internally by Talon.One. - true - The variant assignment is handled externally.  | [optional] 
**campaign** | [**NewCampaign**](NewCampaign.md) |  | 
**goal_type** | **str** | The goal of the experiment. Determines which single metric is used to decide the winning variant. When set to &#x60;other&#x60;, multiple metrics are used.  | [default to 'other']
**goal_description** | **str** | A description of the experiment goal. Provides context for the AI summary and helps it interpret the outcome of the experiment against the stated goal.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


