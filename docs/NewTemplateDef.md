# NewTemplateDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Campaigner-friendly name for the template that will be shown in the rule editor. | 
**description** | **str** | A short description of the template that will be shown in the rule editor. | [optional] 
**help** | **str** | Extended help text for the template. | [optional] 
**category** | **str** | Used for grouping templates in the rule editor sidebar. | 
**expr** | **list[object]** | A Talang expression that contains variable bindings referring to args. | 
**args** | [**list[TemplateArgDef]**](TemplateArgDef.md) | An array of argument definitions. | 
**expose** | **bool** | A flag to control exposure in Rule Builder. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


