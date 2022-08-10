# CustomEffect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**application_ids** | **list[int]** | The IDs of the applications that are related to this entity. | 
**name** | **str** | The name of this effect. | 
**title** | **str** | The title of this effect. | 
**payload** | **str** | The JSON payload of this effect. | 
**description** | **str** | The description of this effect. | [optional] 
**enabled** | **bool** | Determines if this effect is active. | 
**params** | [**list[TemplateArgDef]**](TemplateArgDef.md) | Array of template argument definitions. | [optional] 
**modified_by** | **int** | ID of the user who last updated this effect if available. | [optional] 
**created_by** | **int** | ID of the user who created this effect. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


