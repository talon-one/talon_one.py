# IntegrationHubEventPayloadLoyaltyProfileBasedTierDowngradeNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | The ID of the integration hub event. Return this value in the delivery-status callback to mark the event delivered or failed. | 
**profile_integration_id** | **str** |  | 
**loyalty_program_id** | **int** |  | 
**loyalty_program_name** | **str** | The name of the loyalty program. | 
**subledger_id** | **str** |  | 
**source_of_event** | **str** |  | 
**current_tier** | **str** | The name of the customer&#39;s current tier, or null if the customer was downgraded below all tiers. | [optional] 
**current_points** | **float** |  | 
**old_tier** | **str** |  | [optional] 
**tier_expiration_date** | **datetime** |  | [optional] 
**timestamp_of_tier_change** | **datetime** |  | [optional] 
**published_at** | **datetime** | Timestamp when the event was published. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


