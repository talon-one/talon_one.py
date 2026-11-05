# IntegrationHubEventPayloadLoyaltyProfileBasedPointsChangedNotificationAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**reason** | **str** |  | [optional] 
**operation** | **str** |  | 
**start_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**transaction_uuid** | **str** | The identifier of the transaction in the loyalty ledger. | 
**created** | **datetime** | The timestamp when the loyalty transaction occurred. | [optional] 
**awaits_activation** | **bool** | Indicates whether the points have an action-based start date. This property is returned only for point transactions with an action-based start date. | [optional] 
**validity_duration** | **str** | The duration for which the points remain active, relative to the activation date.  **Note**: This only applies to points for which &#x60;AwaitsActivation&#x60; is &#x60;true&#x60; and &#x60;ExpiryDate&#x60; is not set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


