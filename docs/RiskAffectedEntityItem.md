# RiskAffectedEntityItem

A single entity flagged as anomalous within a risk.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The integration ID of the affected entity. | 
**activity_value** | **float** | The observed value of the monitored activity metric for this entity. | 
**threshold** | **float** | The anomaly threshold computed for the entity&#39;s Application group. | 
**severity_ratio** | **float** | The ratio of the observed value to the threshold. | 
**criticality** | **str** | The critical classification bucket of this entity. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


