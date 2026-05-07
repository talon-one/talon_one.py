# IntegrationHubEventPayloadLoyaltyProfileBasedNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_integration_id** | **str** |  | 
**loyalty_program_id** | **int** |  | 
**subledger_id** | **str** |  | 
**source_of_event** | **str** |  | 
**employee_name** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**current_points** | **float** |  | 
**actions** | [**list[IntegrationHubEventPayloadLoyaltyProfileBasedPointsChangedNotificationAction]**](IntegrationHubEventPayloadLoyaltyProfileBasedPointsChangedNotificationAction.md) |  | [optional] 
**published_at** | **datetime** | Timestamp when the event was published. | 
**current_tier** | **str** |  | [optional] 
**old_tier** | **str** |  | [optional] 
**tier_expiration_date** | **datetime** |  | [optional] 
**timestamp_of_tier_change** | **datetime** |  | [optional] 
**points_required_to_the_next_tier** | **float** |  | [optional] 
**next_tier** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


