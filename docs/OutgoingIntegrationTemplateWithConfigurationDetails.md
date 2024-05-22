# OutgoingIntegrationTemplateWithConfigurationDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**integration_type** | **int** | Unique ID of outgoing integration type. | 
**title** | **str** | The title of the integration template. | 
**description** | **str** | The description of the specific outgoing integration template. | 
**payload** | **str** | The API payload (supports templating using parameters) for this integration template. | 
**method** | **str** | API method for this webhook. | 
**relative_url** | **str** | The relative URL corresponding to each integration template. | 
**headers** | **list[str]** | The list of HTTP headers for this integration template. | 
**policy** | [**object**](.md) | The outgoing integration policy specific to each integration type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


