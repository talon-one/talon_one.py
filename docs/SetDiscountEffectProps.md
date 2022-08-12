# SetDiscountEffectProps

The properties specific to the \"setDiscount\" effect. This gets triggered whenever a validated rule contained a \"set discount\" effect. This is a discount that should be applied on the scope of defined with it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name/description of this discount. | 
**value** | **float** | The total monetary value of the discount. | 
**scope** | **str** | The scope which the discount was applied on, can be one of (cartItems,additionalCosts,sessionTotal). | [optional] 
**desired_value** | **float** | The original value of the discount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


