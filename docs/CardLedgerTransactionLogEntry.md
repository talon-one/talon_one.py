# CardLedgerTransactionLogEntry

Log entry for a given loyalty card transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Date and time the loyalty card transaction occurred. | 
**program_id** | **int** | ID of the loyalty program. | 
**card_identifier** | **str** | Identifier of the loyalty card. | 
**application_id** | **int** | The ID of the Application that owns this entity. | [optional] 
**session_id** | **int** | The **internal** ID of the session.  | [optional] 
**customer_session_id** | **str** | ID of the customer session where the transaction occurred. | 
**type** | **str** | Type of transaction. Possible values are:   - &#x60;addition&#x60;: Points were added.   - &#x60;subtraction&#x60;: Points were subtracted.  | 
**name** | **str** | Name or reason of the loyalty ledger transaction. | 
**start_date** | **str** | Date when points become active. Possible values are:   - &#x60;immediate&#x60;: Points are active immediately.   - &#x60;timestamp value&#x60;: Points become active from the given date.  | 
**expiry_date** | **str** | Date when points expire. Possible values are:   - &#x60;unlimited&#x60;: Points have no expiration date.   - &#x60;timestamp value&#x60;: Points become active from the given date.  | 
**subledger_id** | **str** | ID of the subledger. | 
**amount** | **float** | Amount of loyalty points added or deducted in the transaction. | 
**id** | **int** | ID of the loyalty ledger entry. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


