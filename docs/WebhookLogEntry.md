# WebhookLogEntry

Log of webhook API calls.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID reference of the webhook request. | 
**integration_request_uuid** | **str** | UUID reference of the integration request linked to this webhook request. | 
**webhook_id** | **int** | ID of the webhook that triggered the request. | 
**application_id** | **int** | ID of the application that triggered the webhook. | [optional] 
**url** | **str** | Target url of request | 
**request** | **str** | Request message | 
**response** | **str** | Response message | [optional] 
**status** | **int** | HTTP status code of response. | [optional] 
**request_time** | **datetime** | Timestamp of request | 
**response_time** | **datetime** | Timestamp of response | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


