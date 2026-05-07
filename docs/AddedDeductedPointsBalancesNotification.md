# AddedDeductedPointsBalancesNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_name** | **str** | The name of the employee who added or deducted points. | 
**loyalty_program_id** | **int** | The ID of the loyalty program. | 
**notification_type** | **str** | The type of notification. | 
**profile_integration_id** | **str** | The integration ID of the customer profile to whom points were added or deducted. | 
**session_integration_id** | **str** | The integration ID of the session through which the points were earned or lost. | 
**subledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added. | 
**type_of_change** | **str** | The notification source, that is, it indicates whether the points were added or deducted via one of the following routes: - [The Campaign Manager](/docs/product/getting-started) - [Management API](/management-api#tag/Loyalty) - [Rule Engine](/docs/product/applications/evaluation-order-for-rules-and-filters)  | 
**user_id** | **int** | The ID of the employee who added or deducted points. | 
**actions** | [**list[AddedDeductedPointsBalancesAction]**](AddedDeductedPointsBalancesAction.md) | The list of actions that have been triggered in the loyalty program. | 
**current_points** | **float** | The current points balance. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


