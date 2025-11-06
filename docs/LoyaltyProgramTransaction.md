# LoyaltyProgramTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the loyalty ledger transaction. | 
**transaction_uuid** | **str** | Unique identifier of the transaction in the UUID format. | 
**program_id** | **int** | ID of the loyalty program. | 
**campaign_id** | **int** | ID of the campaign. | [optional] 
**created** | **datetime** | Date and time the loyalty transaction occurred. | 
**type** | **str** | Type of transaction. Possible values:   - &#x60;addition&#x60;: Signifies added points.   - &#x60;subtraction&#x60;: Signifies deducted points.  | 
**amount** | **float** | Amount of loyalty points added or deducted in the transaction. | 
**name** | **str** | Name or reason for the loyalty ledger transaction. | 
**start_date** | **str** | When points become active. Possible values:   - &#x60;immediate&#x60;: Points are immediately active.   - a timestamp value: Points become active at a given date and time.  | 
**expiry_date** | **str** | When points expire. Possible values:   - &#x60;unlimited&#x60;: Points have no expiration date.   - a timestamp value: Points expire at a given date and time.  | 
**customer_profile_id** | **str** | Customer profile integration ID used in the loyalty program. | [optional] 
**card_identifier** | **str** | The alphanumeric identifier of the loyalty card.  | [optional] 
**subledger_id** | **str** | ID of the subledger. | 
**customer_session_id** | **str** | ID of the customer session where the transaction occurred. | [optional] 
**import_id** | **int** | ID of the import where the transaction occurred. | [optional] 
**user_id** | **int** | ID of the user who manually added or deducted points. Applies only to manual transactions. | [optional] 
**user_email** | **str** | The email of the Campaign Manager account that manually added or deducted points. Applies only to manual transactions. | [optional] 
**ruleset_id** | **int** | ID of the ruleset containing the rule that triggered the effect. Applies only for transactions that resulted from a customer session. | [optional] 
**rule_name** | **str** | Name of the rule that triggered the effect. Applies only for transactions that resulted from a customer session. | [optional] 
**flags** | [**LoyaltyLedgerEntryFlags**](LoyaltyLedgerEntryFlags.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


