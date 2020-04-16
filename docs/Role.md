# Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the role corresponding to the DB row | 
**account_id** | **int** | The ID of the Talon.One account that owns this role. | 
**name** | **str** | Name of the role | [optional] 
**description** | **str** | Description of the role | [optional] 
**members** | **list[int]** | A list of user identifiers assigned to this role | [optional] 
**acl** | **str** | Role Policy this should be a stringified blob of json | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


