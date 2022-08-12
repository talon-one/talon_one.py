# SetDiscountPerAdditionalCostPerItemEffectProps

The properties specific to the \"setDiscountPerAdditionalCostPerItem\" effect. This gets triggered whenever a validated rule contained a \"set discount per additional cost per item\" effect. This is a discount that should be applied on a specific additional cost in a specific item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name/description of this discount. | 
**additional_cost_id** | **int** | The ID of the additional cost. | 
**value** | **float** | The total monetary value of the discount. | 
**position** | **float** | The index of the item in the cart item list containing the additional cost to be discounted. | 
**sub_position** | **float** | Only used when [cart item flattening](https://docs.talon.one/docs/product/campaigns/campaign-evaluation/#flattened-cart-items) is enabled. Indicates which item the discount applies to for cart items with &#x60;quantity&#x60; &gt; 1.  | [optional] 
**additional_cost** | **str** | The name of the additional cost. | 
**desired_value** | **float** | Only with [partial discounts enabled](https://docs.talon.one/docs/product/campaigns/campaign-evaluation/#partial-discounts). Represents the monetary value of the discount to be applied to additional discount without considering budget limitations.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


