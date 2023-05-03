# CardLedgerTransactionLogEntryIntegrationAPI

Log entry for a given loyalty card transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Date and time the loyalty card transaction occurred. | 
**program_id** | **int** | ID of the loyalty program. | 
**card_identifier** | **str** | The alphanumeric identifier of the loyalty card.  | 
**customer_session_id** | **str** | ID of the customer session where the transaction occurred. | [optional] 
**type** | **str** | Type of transaction. Possible values:   - &#x60;addition&#x60;: Signifies added points.   - &#x60;subtraction&#x60;: Signifies deducted points.  | 
**name** | **str** | Name or reason of the loyalty ledger transaction. | 
**start_date** | **str** | When points become active. Possible values:   - &#x60;immediate&#x60;: Points are active immediately.   - a timestamp value: Points become active at a given date and time.  | 
**expiry_date** | **str** | Date when points expire. Possible values are:   - &#x60;unlimited&#x60;: Points have no expiration date.   - &#x60;timestamp value&#x60;: Points expire on the given date.  | 
**subledger_id** | **str** | ID of the subledger. | 
**amount** | **float** | Amount of loyalty points added or deducted in the transaction. | 
**id** | **int** | ID of the loyalty ledger transaction. | 
**ruleset_id** | **int** | The ID of the ruleset containing the rule that triggered this effect. | [optional] 
**rule_name** | **str** | The name of the rule that triggered this effect. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


