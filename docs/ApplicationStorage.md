# ApplicationStorage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**name** | **str** | Identifier for the information to be saved, e.g. \&quot;Loyalty points for SKU\&quot;. | 
**datatype** | **object** | A JSON Schema describing the information to be saved in the storage | 
**description** | **str** | Description of the application store | [optional] 
**used_at** | **list[str]** | array of rulesets where the application storage is used | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


