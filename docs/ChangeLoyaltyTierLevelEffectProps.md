# ChangeLoyaltyTierLevelEffectProps

This effect indicates that a customer's loyalty tier has been upgraded.  This effect is generated only when the [Add loyalty points](https://docs.talon.one/docs/product/rules/effects/use-effects#add-loyalty-points) and the [Add loyalty points per cart item](https://docs.talon.one/docs/product/rules/effects/use-effects#add-loyalty-points-per-cart-item) effects are triggered for a particular customer, and, as a result, the customer's loyalty tier is upgraded.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_title** | **str** | The title of the rule that triggered the tier upgrade. | 
**program_id** | **int** | The ID of the loyalty program where the points were added. | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program where the points were added. | 
**previous_tier_name** | **str** | The name of the tier from which the user was upgraded. | [optional] 
**new_tier_name** | **str** | The name of the tier to which the user has been upgraded. | 
**expiry_date** | **datetime** | The expiration date of the new tier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


