# NewWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **list[int]** | The IDs of the Applications in which this webhook is available. An empty array means the webhook is available in &#x60;All Applications&#x60;.  | 
**title** | **str** | Name or title for this webhook. | 
**description** | **str** | A description of the webhook. | [optional] 
**verb** | **str** | API method for this webhook. | 
**url** | **str** | API URL (supports templating using parameters) for this webhook. | 
**headers** | **list[str]** | List of API HTTP headers for this webhook. | 
**payload** | **str** | API payload (supports templating using parameters) for this webhook. | [optional] 
**params** | [**list[TemplateArgDef]**](TemplateArgDef.md) | Array of template argument definitions. | 
**enabled** | **bool** | Enables or disables webhook from showing in the Rule Builder. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


