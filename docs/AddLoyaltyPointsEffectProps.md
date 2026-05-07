# AddLoyaltyPointsEffectProps

The properties specific to the \"addLoyaltyPoints\" effect. This gets triggered whenever a validated rule contained an \"add loyalty\" effect. These points are automatically stored and managed inside Talon.One. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name / description of this loyalty point addition. | 
**program_id** | **int** | The ID of the loyalty program where these points were added. | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added. | 
**value** | **float** | The amount of points that were added. | 
**desired_value** | **float** | The original amount of loyalty points to be awarded. | [optional] 
**recipient_integration_id** | **str** | The user for whom these points were added. | 
**start_date** | **datetime** | Date after which points will be valid. | [optional] 
**expiry_date** | **datetime** | Date after which points will expire. | [optional] 
**transaction_uuid** | **str** | The identifier of this addition in the loyalty ledger. | 
**cart_item_position** | **float** | The index of the item in the cart items list on which the loyal points addition should be applied. | [optional] 
**cart_item_sub_position** | **float** | For cart items with &#x60;quantity&#x60; &gt; 1, the sub position indicates to which item the loyalty points addition is applied.  | [optional] 
**card_identifier** | **str** | The identifier of the loyalty card, which must match the regular expression &#x60;^[A-Za-z0-9._%+@-]+$&#x60;.  | [optional] 
**bundle_index** | **int** | The position of the bundle in a list of item bundles created from the same bundle definition. | [optional] 
**bundle_name** | **str** | The name of the bundle definition. | [optional] 
**awaits_activation** | **bool** | If &#x60;true&#x60;, the loyalty points remain pending until a specific action is complete. The &#x60;startDate&#x60; parameter automatically sets to &#x60;on_action&#x60;.  | [optional] 
**validity_duration** | **str** | The duration for which the points remain active, calculated relative to the  activation date.    **Note**: This value is returned only if &#x60;awaitsActivation&#x60; is &#x60;true&#x60;  and &#x60;expiryDate&#x60; is not set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


