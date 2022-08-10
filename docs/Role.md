# Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**campaign_group_id** | **int** | The ID of the [Campaign Group](https://docs.talon.one/docs/product/account/managing-campaign-groups/) this role was created for.  | [optional] 
**name** | **str** | Name of the role. | 
**description** | **str** | Description of the role. | [optional] 
**members** | **list[int]** | A list of user identifiers assigned to this role. | [optional] 
**acl** | [**object**](.md) | Role ACL Policy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


