# LoyaltyCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**program_id** | **int** | The ID of the loyalty program that owns this entity. | 
**status** | **str** | Status of the loyalty card. Can be &#x60;active&#x60; or &#x60;inactive&#x60;.  | 
**block_reason** | **str** | Reason for transferring and blocking the loyalty card.  | [optional] 
**identifier** | **str** | The alphanumeric identifier of the loyalty card.  | 
**users_per_card_limit** | **int** | The max amount of customer profiles that can be linked to the card. 0 means unlimited.  | 
**profiles** | [**list[LoyaltyCardProfileRegistration]**](LoyaltyCardProfileRegistration.md) | Integration IDs of the customers profiles linked to the card. | [optional] 
**ledger** | [**LedgerInfo**](LedgerInfo.md) |  | [optional] 
**subledgers** | [**dict(str, LedgerInfo)**](LedgerInfo.md) | Displays point balances of the card in the subledgers of the loyalty program. | [optional] 
**modified** | **datetime** | Timestamp of the most recent update of the loyalty card. | [optional] 
**old_card_identifier** | **str** | The alphanumeric identifier of the loyalty card.  | [optional] 
**new_card_identifier** | **str** | The alphanumeric identifier of the loyalty card.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


