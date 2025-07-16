# ModelReturn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**returned_cart_items** | [**list[ReturnedCartItem]**](ReturnedCartItem.md) | List of cart items to be returned. | 
**event_id** | **int** | The event ID of that was generated for this return. | 
**session_id** | **int** | The internal ID of the session this return was requested on. | 
**session_integration_id** | **str** | The integration ID of the session this return was requested on. | 
**profile_id** | **int** | The internal ID of the profile this return was requested on. | [optional] 
**profile_integration_id** | **str** | The integration ID of the profile this return was requested on. | [optional] 
**created_by** | **int** | ID of the user who requested this return. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


