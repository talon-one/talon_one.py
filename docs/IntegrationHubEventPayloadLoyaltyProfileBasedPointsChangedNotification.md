# IntegrationHubEventPayloadLoyaltyProfileBasedPointsChangedNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | The ID of the integration hub event. Return this value in the delivery-status callback to mark the event delivered or failed. | 
**profile_integration_id** | **str** |  | 
**loyalty_program_id** | **int** |  | 
**loyalty_program_name** | **str** | The name of the loyalty program. | 
**subledger_id** | **str** |  | 
**source_of_event** | **str** |  | 
**current_tier** | **str** | The name of the customer&#39;s current tier. | 
**session_integration_id** | **str** | The integration ID of the session through which the points were earned or lost. Only set when the change results from a rule engine execution; empty otherwise. | [optional] 
**employee_name** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**current_points** | **float** |  | 
**actions** | [**list[IntegrationHubEventPayloadLoyaltyProfileBasedPointsChangedNotificationAction]**](IntegrationHubEventPayloadLoyaltyProfileBasedPointsChangedNotificationAction.md) |  | [optional] 
**published_at** | **datetime** | Timestamp when the event was published. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


