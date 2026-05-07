# ExperimentVerdict

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**winner_variant_name** | **str** | The name of the winning variant. If no variant shows a statistically significant advantage on key business metrics, return &#39;Inconclusive&#39;. | 
**verdict_summary** | **str** | A one-sentence summary of the outcome, including the key metric and confidence level that led to the decision. | 
**key_findings** | **list[str]** | A bullet point stating the most important finding, including the metric, the percentage change, and the confidence. | 
**ai_confidence_level** | **str** | Your confidence in this overall verdict, from 0 to 100. | 
**recommendation** | **str** | A short, actionable recommendation based on the findings. If inconclusive, suggest running the test longer. If there is a clear winner, recommend promoting it. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


