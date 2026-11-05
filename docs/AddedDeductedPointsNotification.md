# AddedDeductedPointsNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_name** | **str** | The name of the employee who added or deducted points. | 
**loyalty_program_id** | **int** | The ID of the loyalty program. | 
**notification_type** | **str** | The type of notification. | 
**profile_integration_id** | **str** | The integration ID of the customer profile to whom points were added or deducted. | 
**session_integration_id** | **str** | The integration ID of the session through which the points were earned or lost. | 
**subledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added. | 
**type_of_change** | **str** | The notification source, that is, it indicates whether the points were added or deducted via one of the following routes:  - [The Campaign Manager](/docs/product/getting-started)  - [Management API](/management-api#tag/Loyalty)  - [Rule Engine](/docs/product/applications/evaluation-order-for-rules-and-filters)  | 
**user_id** | **int** | The ID of the employee who added or deducted points. | 
**amount** | **float** | The amount of added or deducted loyalty points. | 
**expiry_date** | **datetime** | The expiration date for loyalty points. | [optional] 
**operation** | **str** | The action (addition or subtraction) made with loyalty points. | 
**reason** | **str** | The reason for the points addition or deduction. | 
**start_date** | **datetime** | The start date for loyalty points. | [optional] 
**transaction_uuid** | **str** | The identifier of the transaction in the loyalty ledger. | 
**created** | **datetime** | The timestamp when the loyalty transaction occurred. | [optional] 
**awaits_activation** | **bool** | Indicates whether the points have an action-based start date. This property is returned only for point transactions with an action-based start date. | [optional] 
**validity_duration** | **str** | The duration for which the points remain active, relative to the activation date.  **Note**: This only applies to points for which &#x60;AwaitsActivation&#x60; is &#x60;true&#x60; and &#x60;ExpiryDate&#x60; is not set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


