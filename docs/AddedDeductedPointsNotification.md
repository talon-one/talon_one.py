# AddedDeductedPointsNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_integration_id** | **str** | The integration ID of the customer profile to whom points were added or deducted. | 
**loyalty_program_id** | **int** | The ID of the loyalty program. | 
**subledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added. | 
**amount** | **float** | The amount of added or deducted loyalty points. | 
**reason** | **str** | The reason for the points addition or deduction. | 
**type_of_change** | **str** | The notification source, that is, it indicates whether the points were added or deducted via one of the following routes:  - [The Campaign Manager](/docs/product/getting-started)  - [Management API](/management-api#tag/Loyalty)  - [Rule Engine](/docs/product/applications/evaluation-order-for-rules-and-filters)  | 
**employee_name** | **str** | The name of the employee who added or deducted points. | 
**user_id** | **int** | The ID of the employee who added or deducted points. | 
**operation** | **str** | The action (addition or deduction) made with loyalty points. | 
**start_date** | **datetime** | The start date for loyalty points. | [optional] 
**expiry_date** | **datetime** | The expiration date for loyalty points. | [optional] 
**session_integration_id** | **str** | The integration ID of the session through which the points were earned or lost. | 
**notification_type** | **str** | The type of notification. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


