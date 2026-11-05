# ExpiringCardPointsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **date** | The expiration date of loyalty points. | 
**loyalty_program_id** | **int** | The ID of the loyalty program. | 
**amount_of_expiring_points** | **float** | The amount of loyalty points that will be expired soon. | 
**subledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added. | 
**card_identifier** | **str** | The identifier of the loyalty card, &#x60;which must match the regular expression &#x60;^[A-Za-z0-9._%+@-]+$&#x60;.  | 
**users_per_card_limit** | **int** | The maximum number of customer profiles with which a card can be shared. This can be set to &#x60;0&#x60; for no limit.  | 
**profiles** | **list[str]** | The integration IDs of the customer profiles linked to the card. | 
**created** | **datetime** | The timestamp when the loyalty transaction occurred. | [optional] 
**awaits_activation** | **bool** | Indicates whether the points have an action-based start date. This property is returned only for point transactions with an action-based start date. | [optional] 
**validity_duration** | **str** | The duration for which the points remain active, relative to the activation date.  **Note**: This only applies to points for which &#x60;AwaitsActivation&#x60; is &#x60;true&#x60; and &#x60;ExpiryDate&#x60; is not set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


