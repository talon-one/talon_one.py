# OutboundMessage

Outbound notification or webhook message with its shared request details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the outbound message. | 
**notification_id** | **int** | ID of the notification that produced the outbound request. | [optional] 
**notification_name** | **str** | Name of the notification that produced the outbound request. | [optional] 
**webhook_id** | **int** | ID of the webhook that produced the outbound request. | [optional] 
**webhook_name** | **str** | The name of the webhook that produced the outbound request. | [optional] 
**notification_type** | **str** | Type of notification that produced the outbound request. | 
**application_id** | **int** | ID of the Application associated with the outbound request. | [optional] 
**loyalty_program_id** | **int** | ID of the loyalty program associated with the outbound request. | [optional] 
**request** | [**OutboundLogRequest**](OutboundLogRequest.md) |  | 
**first_log_at** | **datetime** | Timestamp of the first log entry for this message. | 
**last_log_at** | **datetime** | Timestamp of the last log entry for this message. | 
**last_response_code** | **int** | HTTP status code from the latest response. | [optional] 
**status** | **str** |  | 
**retry_count** | **int** | Number of retries. | [optional] 
**responses** | [**list[OutboundMessageResponse]**](OutboundMessageResponse.md) | Log entries for this message. Omitted when &#x60;includeLogs&#x3D;false&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


