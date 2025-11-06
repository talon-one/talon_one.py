# CardLedgerTransactionLogEntry

Log entry for a given loyalty card transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_uuid** | **str** | Unique identifier of the transaction in the UUID format. | 
**created** | **datetime** | Date and time the loyalty card transaction occurred. | 
**program_id** | **int** | ID of the loyalty program. | 
**card_identifier** | **str** | The alphanumeric identifier of the loyalty card.  | 
**application_id** | **int** | The ID of the Application that owns this entity. | [optional] 
**session_id** | **int** | The **internal** ID of the session.  | [optional] 
**customer_session_id** | **str** | ID of the customer session where the transaction occurred. | [optional] 
**type** | **str** | Type of transaction. Possible values:   - &#x60;addition&#x60;: Signifies added points.   - &#x60;subtraction&#x60;: Signifies deducted points.  | 
**name** | **str** | Name or reason of the loyalty ledger transaction. | 
**start_date** | **str** | When points become active. Possible values:   - &#x60;immediate&#x60;: Points are immediately active.   - a timestamp value: Points become active at a given date and time.  | 
**expiry_date** | **str** | Date when points expire. Possible values are:   - &#x60;unlimited&#x60;: Points have no expiration date.   - &#x60;timestamp value&#x60;: Points become active from the given date.  | 
**subledger_id** | **str** | ID of the subledger. | 
**amount** | **float** | Amount of loyalty points added or deducted in the transaction. | 
**id** | **int** | ID of the loyalty ledger entry. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


