# Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**modified** | **datetime** | The time this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**campaign_group_id** | **int** | The ID of the [Campaign Group](https://docs.talon.one/docs/product/account/managing-campaign-groups) this role was created for.  | [optional] 
**name** | **str** | Name of the role. | 
**description** | **str** | Description of the role. | [optional] 
**members** | **list[int]** | A list of user identifiers assigned to this role. | [optional] 
**acl** | [**object**](.md) | The &#x60;Access Control List&#x60; json defining the role of the user. This represents the access control on the user level. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


