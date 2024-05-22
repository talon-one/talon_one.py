# LoyaltyProgramLedgers

Customer-specific information about loyalty points.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of loyalty program. | 
**title** | **str** | Visible name of loyalty program. | 
**name** | **str** | Internal name of loyalty program. | 
**join_date** | **datetime** | The date on which the customer joined the loyalty program in RFC3339.  **Note**: This is in the loyalty program&#39;s time zone.  | [optional] 
**ledger** | [**LedgerInfo**](LedgerInfo.md) |  | 
**sub_ledgers** | [**dict(str, LedgerInfo)**](LedgerInfo.md) | A map containing information about each loyalty subledger. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


