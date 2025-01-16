# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**modified** | **datetime** | The time this entity was last modified. | 
**email** | **str** | The email address associated with the user profile. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | Name of the user. | 
**state** | **str** | State of the user. | 
**invite_token** | **str** | Invitation token of the user.  **Note**: If the user has already accepted their invitation, this is &#x60;null&#x60;.  | 
**is_admin** | **bool** | Indicates whether the user is an &#x60;admin&#x60;. | [optional] 
**policy** | [**object**](.md) | Access level of the user. | 
**roles** | **list[int]** | A list of the IDs of the roles assigned to the user. | [optional] 
**auth_method** | **str** | Authentication method for this user. | [optional] 
**application_notification_subscriptions** | [**object**](.md) | Application notifications that the user is subscribed to. | [optional] 
**last_signed_in** | **datetime** | Timestamp when the user last signed in to Talon.One. | [optional] 
**last_accessed** | **datetime** | Timestamp of the user&#39;s last activity after signing in to Talon.One. | [optional] 
**latest_feed_timestamp** | **datetime** | Timestamp when the user was notified for feed. | [optional] 
**additional_attributes** | [**object**](.md) | Additional user attributes, created and used by external identity providers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


