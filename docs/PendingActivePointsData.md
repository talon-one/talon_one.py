# PendingActivePointsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loyalty_program_id** | **int** | The ID of the loyalty program. | 
**subledger_id** | **str** | The ID of the subledger, when applicable. If this field is empty, the main ledger is used. | [default to '']
**customer_profile_id** | **str** | The integration ID of the customer profile whose loyalty points are becoming active. | 
**points** | **float** | The amount of pending loyalty points becoming active. | 
**active_on** | **datetime** | The date and time the loyalty points become active. | [optional] 
**expire_on** | **datetime** | The date and time the loyalty points expire. | [optional] 
**session_integration_id** | **str** | The integration ID of the session through which the points were earned. | [optional] 
**created** | **datetime** | The timestamp when the loyalty transaction occurred. | [optional] 
**awaits_activation** | **bool** | Indicates whether the points have an action-based start date. This property is returned only for point transactions with an action-based start date. | [optional] 
**validity_duration** | **str** | The duration for which the points remain active, relative to the activation date.  **Note**: This only applies to points for which &#x60;AwaitsActivation&#x60; is &#x60;true&#x60; and &#x60;ExpireOn&#x60; is not set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


