# RoleV2RolesGroup

A map of target entities to their permission sets.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**dict(str, RoleV2ApplicationDetails)**](RoleV2ApplicationDetails.md) | A map of the link between the Application, campaign, or draft campaign-related permission set and the Application ID the permissions apply to. | [optional] 
**loyalty_programs** | **dict(str, str)** | A map of the link between the loyalty program-related permission set and the loyalty program ID the permissions apply to. | [optional] 
**campaign_access_groups** | **dict(str, str)** | A map of the link between the campaign access group-related permission set and the campaign access group ID the permissions apply to. | [optional] 
**account** | **str** | Name of the account-level permission set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


