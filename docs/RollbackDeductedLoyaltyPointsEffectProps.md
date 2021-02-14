# RollbackDeductedLoyaltyPointsEffectProps

The properties specific to the \"rollbackDeductedLoyaltyPoints\" effect. This effect is triggered whenever a previously closed session is cancelled and a deductLoyaltyPoints effect was revoked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **int** | The ID of the loyalty program where these points were reimbursed | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program where these points were reimbursed | 
**value** | **float** | The amount of reimbursed points that were added | 
**recipient_integration_id** | **str** | The user for whom these points were reimbursed | 
**start_date** | **datetime** | Date after which the reimbursed points will be valid | [optional] 
**expiry_date** | **datetime** | Date after which the reimbursed points will expire | [optional] 
**transaction_uuid** | **str** | The identifier of &#39;addition&#39; entries added to the ledger as the &#x60;deductLoyaltyPoints&#x60; effect is rolled back | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


