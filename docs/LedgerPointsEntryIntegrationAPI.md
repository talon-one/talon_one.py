# LedgerPointsEntryIntegrationAPI

Loyalty profile points with start and expiry dates.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the transaction that adds loyalty points. | 
**created** | **datetime** | Date and time the loyalty points were added. | 
**program_id** | **int** | ID of the loyalty program. | 
**customer_session_id** | **str** | ID of the customer session where points were added. | [optional] 
**name** | **str** | Name or reason of the transaction that adds loyalty points. | 
**start_date** | **str** | When points become active. Possible values:   - &#x60;immediate&#x60;: Points are active immediately.   - &#x60;timestamp value&#x60;: Points become active at a given date and time.  | 
**expiry_date** | **str** | Date when points expire. Possible values are:   - &#x60;unlimited&#x60;: Points have no expiration date.   - &#x60;timestamp value&#x60;: Points expire on the given date and time.  | 
**subledger_id** | **str** | ID of the subledger. | 
**amount** | **float** | Amount of loyalty points added in the transaction. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


