# TierDowngradeData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_profile_id** | **str** | The integration ID of the customer profile whose tier was downgraded. | 
**loyalty_program_id** | **int** | The ID of the loyalty program. | 
**subledger_id** | **str** | The ID of the subledger, when applicable. If this field is empty, the main ledger is used. | [default to '']
**current_tier** | **str** | The name of the customer&#39;s current tier. | [optional] 
**current_points** | **float** | The number of points the customer had at the time of tier downgrade. | 
**old_tier** | **str** | The name of the customer&#39;s previous tier. | 
**tier_expiration_date** | **datetime** | The exact date and time the tier expires. | [optional] 
**timestamp_of_tier_change** | **datetime** | The exact date and time the tier was changed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


