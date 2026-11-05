# RollbackTierBoostEffectProps

This effect indicates that a loyalty tier boost was rolled back.  The Rule Engine triggers this effect when you cancel a customer session that previously triggered the [boostLoyaltyTier](https://docs.talon.one/docs/dev/integration-api/api-effects#boostloyaltytier) API effect. The tier boost is voided and the customer returns to the tier determined by their points balance.  This effect only applies to full session cancellations. Partially returned sessions do not trigger a tier boost rollback.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **int** | The ID of the loyalty program. | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program. | 
**tier_name** | **str** | The name of the boosted tier that was rolled back. | 
**boost_uuid** | **str** | The unique identifier of the tier boost that was rolled back. Matches the &#x60;boostUuid&#x60; of the original &#x60;boostLoyaltyTier&#x60; effect. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


