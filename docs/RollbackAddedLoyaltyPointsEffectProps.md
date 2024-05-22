# RollbackAddedLoyaltyPointsEffectProps

The properties specific to the \"rollbackAddedLoyaltyPoints\" effect. This gets triggered whenever previously a closed session with an addLoyaltyPoints effect is cancelled.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **int** | The ID of the loyalty program where the points were originally added. | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program where these points were originally added. | 
**value** | **float** | The amount of points that were rolled back. | 
**recipient_integration_id** | **str** | The user for whom these points were originally added. | 
**transaction_uuid** | **str** | The identifier of &#39;deduction&#39; entry added to the ledger as the &#x60;addLoyaltyPoints&#x60; effect is rolled back. | 
**cart_item_position** | **float** | The index of the item in the cart items for which the loyalty points were rolled back. | [optional] 
**cart_item_sub_position** | **float** | For cart items with &#x60;quantity&#x60; &gt; 1, the sub-position indicates to which item the loyalty points were rolled back.  | [optional] 
**card_identifier** | **str** | The alphanumeric identifier of the loyalty card.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


