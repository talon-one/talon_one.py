# BoostLoyaltyTierEffectProps

This effect indicates that the customer was temporarily placed in a higher loyalty tier for a specified period, without any change to their points balance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **int** | The ID of the loyalty program. | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program. | 
**tier_name** | **str** | The name of the tier to which the customer is temporarily boosted. | 
**reason** | **str** | A reason for the tier boost. | [optional] 
**expiry_date** | **datetime** | The date when the tier boost expires. | 
**boost_uuid** | **str** | The unique identifier of the tier boost. Used to match the boost to its rollback effect when a session is cancelled. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


