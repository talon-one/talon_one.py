# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**email** | **str** | The email address associated with your account. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**invite_token** | **str** | Invite token, empty if the user as already accepted their invite. | 
**state** | **str** | Current user state. | 
**name** | **str** | Full name | 
**policy** | **str** | A blob of ACL JSON | 
**release_update** | **bool** | Update the user via email | 
**latest_feature** | **str** | Latest feature the user has been notified. | [optional] 
**roles** | **list[int]** | Contains a list of all roles a user is a memeber of | [optional] 
**application_notification_subscriptions** | **object** |  | [optional] 
**auth_method** | **str** | The Authentication method for this user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


