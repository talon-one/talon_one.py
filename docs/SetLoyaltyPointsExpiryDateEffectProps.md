# SetLoyaltyPointsExpiryDateEffectProps

This effect updates the expiry date of all active, pending, and unlimited point transactions to a specific date. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **int** | ID of the loyalty program that contains these points. | 
**sub_ledger_id** | **str** | API name of the loyalty program subledger that contains these points. | 
**new_expiry_date** | **datetime** | The specified expiry date and time for all active and pending point transactions in the loyalty program subledger. | 
**affected_transactions** | [**list[LoyaltyLedgerEntryExpiryDateChange]**](LoyaltyLedgerEntryExpiryDateChange.md) | List of transactions affected by the expiry date update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


