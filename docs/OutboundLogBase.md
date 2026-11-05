# OutboundLogBase

Shared details of an outbound notification or webhook message.
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
**request** | [**OutboundLogRequest**](OutboundLogRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


