# DeductLoyaltyPointsEffectProps

The properties specific to the \"deductLoyaltyPoints\" effect. This gets triggered whenever a validated rule contained a condition to only trigger when the given number of loyalty points could be deduced. These points are automatically stored and managed inside Talon.One.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_title** | **str** | The title of the rule that contained triggered this points deduction | 
**program_id** | **int** | The ID of the loyalty program where these points were added | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added | 
**value** | **float** | The amount of points that were deducted | 
**transaction_uuid** | **str** | The identifier of this deduction in the loyalty ledger | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


