# IntegrationHubFlowResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the integration hub flow. | 
**integration_name** | **str** | Name of the integration. | [optional] 
**instance_name** | **str** | Name of the integration instance. | [optional] 
**created_at** | **datetime** | Timestamp when the flow was created. | 
**disabled_until** | **datetime** | Timestamp until which the flow is disabled. Null when the flow is active. | [optional] 
**application_id** | **int** | ID of the application the flow is registered for. | [optional] 
**loyalty_program_id** | **int** | ID of the loyalty program the flow is registered for. | [optional] 
**event_type** | **str** | The event type we want to register a flow for. | 
**config** | [**IntegrationHubFlowConfigResponse**](IntegrationHubFlowConfigResponse.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


