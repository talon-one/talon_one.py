# LoyaltyCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**program_id** | **int** | The ID of the loyalty program that owns this entity. | 
**status** | **str** | Status of the loyalty card. Can be one of: [&#39;active&#39;, &#39;disabled&#39;]  | 
**identifier** | **str** | The alphanumeric identifier of the loyalty card. | 
**users_per_card_limit** | **int** | The max amount of user profiles a card can be shared with. 0 means unlimited.  | 
**profiles** | [**list[LoyaltyCardProfileRegistration]**](LoyaltyCardProfileRegistration.md) | Integration IDs of the customers associated with the card. | [optional] 
**ledger** | [**LedgerInfo**](LedgerInfo.md) |  | [optional] 
**subledgers** | [**dict(str, LedgerInfo)**](LedgerInfo.md) | Displays point balances of the card in the subledgers of the loyalty program. | [optional] 
**modified** | **datetime** | Timestamp of the most recent update of the loyalty card. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


