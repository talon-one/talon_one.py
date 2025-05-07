# ManagementKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for management key. | 
**expiry_date** | **datetime** | The date the management key expires. | 
**endpoints** | [**list[Endpoint]**](Endpoint.md) | The list of endpoints that can be accessed with the key | 
**allowed_application_ids** | **list[int]** | A list of Application IDs that you can access with the management key. An empty or missing list means the management key can be used for all Applications in the account.  | [optional] 
**id** | **int** | ID of the management key. | 
**created_by** | **int** | ID of the user who created it. | 
**account_id** | **int** | ID of account the key is used for. | 
**created** | **datetime** | The date the management key was created. | 
**disabled** | **bool** | The management key is disabled (this property is set to &#x60;true&#x60;) when the user who created the key is disabled or deleted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


