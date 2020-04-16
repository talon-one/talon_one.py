# ApplicationSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. The exact moment this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**profile_id** | **int** | The globally unique Talon.One ID of the customer that created this entity. | [optional] 
**integration_id** | **str** | The ID used for this entity in the application system. | 
**profileintegrationid** | **str** | Integration ID of the customer for the session. | [optional] 
**coupon** | **str** | Any coupon code entered. | 
**referral** | **str** | Any referral code entered. | 
**state** | **str** | Indicating if the customer session is in progress (\&quot;open\&quot;), \&quot;closed\&quot;, or \&quot;cancelled\&quot;. | 
**cart_items** | [**list[CartItem]**](CartItem.md) | Serialized JSON representation. | 
**discounts** | **dict(str, float)** | A map of labelled discount values, in the same currency as the session. | 
**total** | **float** | The total sum of the session before any discounts applied. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


