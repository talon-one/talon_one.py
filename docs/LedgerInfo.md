# LedgerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_balance** | **float** | Sum of currently active points. | 
**pending_balance** | **float** | Sum of pending points. | 
**expired_balance** | **float** | **DEPRECATED** Value is shown as 0.  | 
**spent_balance** | **float** | **DEPRECATED** Value is shown as 0.  | 
**tentative_current_balance** | **float** | Sum of the tentative active points (including additions and deductions) inside the currently open session. The &#x60;currentBalance&#x60; is updated to this value when you close the session, and the effects are applied. | 
**tentative_pending_balance** | **float** | Sum of pending points (including additions and deductions) inside the currently open session. The &#x60;pendingBalance&#x60; is updated to this value when you close the session, and the effects are applied. | [optional] 
**current_tier** | [**Tier**](Tier.md) |  | [optional] 
**points_to_next_tier** | **float** | Points required to move up a tier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


