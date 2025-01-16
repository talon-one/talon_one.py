# ScimNewUser

Payload for users that are created using the SCIM provisioning protocol with an identity provider, for example, Microsoft Entra ID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Status of the user. | [optional] 
**display_name** | **str** | Display name of the user. | [optional] 
**user_name** | **str** | Unique identifier of the user. This is usually an email address. | 
**name** | [**ScimBaseUserName**](ScimBaseUserName.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


