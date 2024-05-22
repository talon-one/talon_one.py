# RollbackDiscountEffectProps

The properties specific to the \"rollbackDiscount\" effect. This gets triggered whenever previously closed session is now cancelled or partially returned and a setDiscount effect was cancelled on our internal discount limit counters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the \&quot;setDiscount\&quot; effect that was rolled back. | 
**value** | **float** | The value of the discount that was rolled back. | 
**cart_item_position** | **float** | The index of the item in the cart items for which the discount was rolled back. | [optional] 
**cart_item_sub_position** | **float** | For cart items with &#x60;quantity&#x60; &gt; 1, the subposition returns the index of the item unit in its line item.  | [optional] 
**additional_cost_id** | **int** | The ID of the additional cost that was rolled back. | [optional] 
**additional_cost** | **str** | The name of the additional cost that was rolled back. | [optional] 
**scope** | **str** | The scope of the rolled back discount - For a discount per session, it can be one of &#x60;cartItems&#x60;, &#x60;additionalCosts&#x60; or &#x60;sessionTotal&#x60; - For a discount per item, it can be one of &#x60;price&#x60;, &#x60;additionalCosts&#x60; or &#x60;itemTotal&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


