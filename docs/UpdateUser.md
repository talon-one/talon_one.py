# UpdateUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the user. | [optional] 
**state** | **str** | The state of the user.   - &#x60;deactivated&#x60;: The user has been deactivated.   - &#x60;active&#x60;: The user is active.  **Note**: Only &#x60;admin&#x60; users can update the state of another user.  | [optional] 
**is_admin** | **bool** | Indicates whether the user is an &#x60;admin&#x60;. | [optional] 
**policy** | **str** | Indicates the access level of the user. | [optional] 
**roles** | **list[int]** | A list of the IDs of the roles assigned to the user.  **Note**: Use the [List roles](https://docs.talon.one/management-api#tag/Roles/operation/getAllRoles) endpoint to find the ID of a role.  | [optional] 
**application_notification_subscriptions** | [**object**](.md) | Application notifications that the user is subscribed to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


