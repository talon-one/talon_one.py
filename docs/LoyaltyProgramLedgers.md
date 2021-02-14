# LoyaltyProgramLedgers

Customer specific information about loyalty points.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of loyalty program | 
**title** | **str** | Visible name of loyalty program | 
**name** | **str** | Internal name of loyalty program | 
**ledger** | [**LoyaltyProgramBalance**](LoyaltyProgramBalance.md) |  | 
**sub_ledgers** | [**dict(str, LoyaltyProgramBalance)**](LoyaltyProgramBalance.md) | A map containing a list of all loyalty subledger balances | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


