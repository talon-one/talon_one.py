# RiskDetail

Details of a risk, including its most severely affected entities.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**notification_id** | **int** | The ID of the risk notification rule that flagged this risk. | 
**feature_date** | **date** | The date of the activity data in which this risk was detected. The anomaly detection pipeline scores complete 24-hour cycles, so this is always the day before the risk was reported, not the reporting date itself.  | 
**group_key** | **str** | The Application group this risk was detected in. Contains the Application ID, or &#x60;__GLOBAL__&#x60; for metrics that are not grouped by Application.  | 
**application_id** | **int** | The ID of the Application this risk belongs to. Absent for global metrics. | [optional] 
**status** | **str** | The triage lifecycle status of this risk. | 
**criticality** | **str** | The critical classification bucket of this risk. | 
**entity** | **str** | The entity type the risk was detected in. | 
**activity** | **str** | The activity metric the risk was detected in. | 
**time_frame** | **str** | The rolling time window of the risk evaluation. | 
**reported_date** | **datetime** | The time the ML service reported this risk. | 
**affected_entity_count** | **int** | The total number of entities affected by this risk. | 
**description** | **str** | Human-readable description of the detected anomaly. | [optional] 
**discard_reason** | **str** | The reason this risk was discarded. Only present on discarded risks. | [optional] 
**status_comment** | **str** | The free-text details of the latest reclassification action: the description for resolving confirmed risks, or the details for discarding risks.  | [optional] 
**status_changed_by** | **int** | The ID of the user who performed the latest reclassification action. | [optional] 
**status_changed_at** | **datetime** | The time of the latest reclassification action. | [optional] 
**modified** | **datetime** | Timestamp of the most recent update. | 
**affected_entities** | [**list[RiskAffectedEntityItem]**](RiskAffectedEntityItem.md) | The affected entities with the highest severity ratios, in descending order. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


