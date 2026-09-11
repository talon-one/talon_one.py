# IntegrationHubEventRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the event record. | 
**flow_id** | **int** | ID of the integration hub flow. | 
**integration_name** | **str** | Name of the integration. | [optional] 
**instance_name** | **str** | Name of the integration instance. | [optional] 
**event_type** | [**IntegrationHubEventType**](IntegrationHubEventType.md) |  | 
**published_at** | **datetime** | Timestamp when the event was published. | 
**processed_at** | **datetime** | Timestamp when the event was processed. | [optional] 
**delivered_at** | **datetime** | Timestamp when the event was delivered. | [optional] 
**scheduled_to** | **datetime** | Timestamp after which the event is scheduled to be processed. | 
**retry** | **int** | Number of delivery retries attempted. | 
**payload** | **str** | The event payload as a formatted JSON string. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


