# RedeemLoyaltyPointsBlock

A block that deducts a specified amount of points from a customer's loyalty program balance, optionally from a named subledger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**program** | [**RedeemLoyaltyPointsBlockProgram**](RedeemLoyaltyPointsBlockProgram.md) |  | 
**subledger** | **str** | The name of the subledger to deduct points from. Can be empty if this block deducts from the loyalty program&#39;s main ledger instead of a subledger. | 
**value** | [**object**](.md) | Number of points to deduct. Either a numeric scalar or a &#x60;{{expression}}&#x60; string that resolves to a number at evaluation time. | 
**name** | **str** | A custom description recorded as the reason for the point deduction. | [optional] 
**on_failure** | **list[object]** | Promotion blocks evaluated when this block fails or returns false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


