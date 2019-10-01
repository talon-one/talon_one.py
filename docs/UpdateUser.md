# UpdateUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address associated with your account. | 
**name** | **str** | Your name. | [optional] 
**password** | **str** | Your old password. | [optional] 
**new_password** | **str** | Your new password. | [optional] 
**policy** | **str** | a blob of acl json | [optional] 
**state** | **str** | New state (\&quot;deactivated\&quot; or \&quot;active\&quot;) for the user. Only usable by admins for the user. | [optional] 
**release_update** | **bool** | Update the user via email | [optional] 
**latest_feature** | **str** | The latest feature you&#39;ve been notified. | [optional] 
**roles** | **list[int]** | Update | [optional] 
**application_notification_subscriptions** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


