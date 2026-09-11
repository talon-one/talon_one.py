# CheckLoyaltyBalanceBlock

A block that checks a specific loyalty program's ledger or subledger balance against a numeric value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**operator** | **str** | An indicator of how the block compares the balance to the value. | 
**program** | [**CheckLoyaltyBalanceBlockProgram**](CheckLoyaltyBalanceBlockProgram.md) |  | 
**subledger** | **str** | The name of the subledger to check the balance of. Can be empty if this block checks the loyalty program&#39;s main ledger balance instead of a subledger. | 
**balance** | **str** | The type of balance to check:  - &#x60;current&#x60; is the sum of currently active points  - &#x60;pending&#x60; is the sum of pending points.  - &#x60;negative&#x60; is the sum of negative points.  - &#x60;tentativeCurrent&#x60; is the tentative points balance within the current open customer session. | 
**value** | **float** | The numeric value to compare the balance against. | 
**on_failure** | **list[object]** | Promotion blocks evaluated when this block fails or returns false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


