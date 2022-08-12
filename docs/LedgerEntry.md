# LedgerEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**profile_id** | **str** | ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known &#x60;profileId&#x60;, we recommend you use a guest &#x60;profileId&#x60;.  | 
**account_id** | **int** | The ID of the Talon.One account that owns this profile. | 
**loyalty_program_id** | **int** | ID of the ledger. | 
**event_id** | **int** | ID of the related event. | 
**amount** | **int** | Amount of loyalty points. | 
**reason** | **str** | reason for awarding/deducting points. | 
**expiry_date** | **datetime** | Expiry date of the points. | 
**reference_id** | **int** | The ID of the balancing ledgerEntry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


