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
**policy** | [**object**](.md) | User ACL Policy | 
**latest_feed_timestamp** | **datetime** | Latest timestamp the user has been notified for feed. | [optional] 
**roles** | **list[int]** | Contains a list of all roles the user is a member of | [optional] 
**application_notification_subscriptions** | [**object**](.md) |  | [optional] 
**auth_method** | **str** | The Authentication method for this user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


