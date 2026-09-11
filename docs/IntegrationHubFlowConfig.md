# IntegrationHubFlowConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | 
**worker_count** | **int** | Number of IntegrationHub workers to run in parallel for this flow (maximum 500). | [optional] [default to 10]
**max_events_per_message** | **int** | Maximum number of events to send in a single message to IntegrationHub. | [optional] [default to 1000]
**max_retries** | **int** | Maximum number of retries for a IntegrationHub event before it is ignored. | [optional] [default to 10]
**instance_name** | **str** | Name of the Prismatic instance that registered this flow. | [optional] 
**integration_name** | **str** | Name of the Prismatic integration that registered this flow. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


