# MessageLogEntry

Message Log.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the message. | 
**service** | **str** | Name of the service that generated the log entry. | 
**change_type** | **str** | Type of change that triggered the notification. | [optional] 
**notification_id** | **int** | ID of the notification. | [optional] 
**notification_name** | **str** | The name of the notification. | [optional] 
**webhook_id** | **int** | ID of the webhook. | [optional] 
**webhook_name** | **str** | The name of the webhook. | [optional] 
**request** | [**MessageLogRequest**](MessageLogRequest.md) |  | [optional] 
**response** | [**MessageLogResponse**](MessageLogResponse.md) |  | [optional] 
**created_at** | **datetime** | Timestamp when the log entry was created. | 
**entity_type** | **str** | The entity type the log is related to.  | 
**url** | **str** | The target URL of the request. | [optional] 
**application_id** | **int** | Identifier of the Application. | [optional] 
**loyalty_program_id** | **int** | Identifier of the loyalty program. | [optional] 
**campaign_id** | **int** | Identifier of the campaign. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


