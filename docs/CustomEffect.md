# CustomEffect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**name** | **str** | The name of this effect. | 
**title** | **str** | The title of this effect. | 
**payload** | **str** | The JSON payload of this effect. | 
**description** | **str** | The description of this effect. | [optional] 
**enabled** | **bool** | Determines if this effect is active. | 
**subscribed_applications_ids** | **list[int]** | A list of the IDs of the applications that this effect is enabled for | [optional] 
**params** | [**list[TemplateArgDef]**](TemplateArgDef.md) | Array of template argument definitions | [optional] 
**modified_by** | **int** | ID of the user who last updated this effect if available. | [optional] 
**created_by** | **int** | ID of the user who created this effect. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


