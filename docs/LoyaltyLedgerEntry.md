# LoyaltyLedgerEntry

A single row of the ledger, describing one addition or deduction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | 
**program_id** | **int** |  | 
**customer_profile_id** | **str** |  | [optional] 
**card_id** | **int** |  | [optional] 
**customer_session_id** | **str** |  | [optional] 
**event_id** | **int** |  | [optional] 
**type** | **str** | The type of the ledger transaction. Possible values are: - &#x60;addition&#x60; - &#x60;subtraction&#x60; - &#x60;expire&#x60; - &#x60;expiring&#x60; (for expiring points ledgers)  | 
**amount** | **float** |  | 
**start_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**name** | **str** | A name referencing the condition or effect that added this entry, or the specific name provided in an API call. | 
**sub_ledger_id** | **str** | This specifies if we are adding loyalty points to the main ledger or a subledger. | 
**user_id** | **int** | This is the ID of the user who created this entry, if the addition or subtraction was done manually. | [optional] 
**archived** | **bool** | Indicates if the entry belongs to the archived session. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


