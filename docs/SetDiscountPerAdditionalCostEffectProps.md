# SetDiscountPerAdditionalCostEffectProps

This effect indicates that a discount that should be applied on a specific additional cost. It is triggered whenever a rule containing a **Discount additional cost** effect is validated.  Enabling [partial rewards](https://docs.talon.one/docs/product/applications/manage-general-settings#partial-rewards) allows a rule that would fail because of insufficient budget to pass. The rule still fails when the budget reaches 0. Use the `desiredValue` property to identify the original amount of loyalty points.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the discount. | 
**additional_cost_id** | **int** | The identifier of the additional cost. | 
**additional_cost** | **str** | The API name of the additional cost. | 
**value** | **float** | The monetary value of the discount to apply. | 
**desired_value** | **float** | _(Partial discounts enabled only)_ The monetary value of the discount to be applied without considering budget limitations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


