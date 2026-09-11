# SetDiscountPerItemEffectProps

This effect schema is returned when you use the **Discount individual items**, **Discount individual items pro rata**, or **Discount individual item in bundles** effect in a rule.  It indicates that a discount per item should be applied on the specific item specified in the effect.  The properties it contains depends on:  - Whether you used a pro rata effect or not. - Whether you used an effect with bundles or not. - Whether the partial discount feature is enabled.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The description of this discount. &#x60;#number&#x60; is equal to the &#x60;position&#x60; property. | 
**value** | **float** | The monetary value of the effective discount applied to the item. | 
**position** | **float** | The index of the item in the &#x60;cartItem&#x60; object on which this discount should be applied. | 
**sub_position** | **float** | The index of the item unit in its line item. | [optional] 
**desired_value** | **float** | _(Partial discounts enabled only)_ The monetary value of the discount to be applied to the item without considering budget limitations. | [optional] 
**scope** | **str** | What the discount applies to. Possible values:  - &#x60;price&#x60;: discount on the price of the item. - &#x60;additionalCosts&#x60;: discount on the [additional cost](https://docs.talon.one/docs/product/account/dev-tools/manage-additional-costs) of the item. - &#x60;itemTotal&#x60;: discount on the sum of price + additional cost of the item. | [optional] 
**total_discount** | **float** | _(Pro rata discounts only)_ The monetary value of the total effective discount | [optional] 
**desired_total_discount** | **float** | _(Pro rata discounts only)_ The monetary value of the total discount to be applied without considering budget limitations | [optional] 
**bundle_index** | **int** | _(Discounts with bundles only)_ The position of the specific item bundle in the list of bundles created from the same bundle definition. | [optional] 
**bundle_name** | **str** | _(Discounts with bundles only)_ The name of the bundle definition. | [optional] 
**targeted_item_position** | **float** | _(Discounting individual item in bundles only)_ The index of the targeted bundle item on which the applied discount is based. | [optional] 
**targeted_item_sub_position** | **float** | _(Discounting individual item in bundles only)_ The sub-position of the targeted bundle item on which the applied discount is based. | [optional] 
**excluded_from_price_history** | **bool** | When set to &#x60;true&#x60;, the applied discount is excluded from the item&#39;s price history. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


