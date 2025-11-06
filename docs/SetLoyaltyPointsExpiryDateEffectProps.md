# SetLoyaltyPointsExpiryDateEffectProps

The properties specific to the \"setLoyaltyPointsExpiryDate\" effect. This gets triggered when a validated rule contains the \"set expiry date\" effect. The current expiry date gets set to the date given in the effect. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **int** | ID of the loyalty program that contains these points. | 
**sub_ledger_id** | **str** | API name of the loyalty program subledger that contains these points. | 
**new_expiry_date** | **datetime** | The specified expiry date and time for all active and pending point transactions in the loyalty program subledger. | 
**affected_transactions** | [**list[LoyaltyLedgerEntryExpiryDateChange]**](LoyaltyLedgerEntryExpiryDateChange.md) | List of transactions affected by the expiry date update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


