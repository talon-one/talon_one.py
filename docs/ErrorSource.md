# ErrorSource

The source of the current error, exactly one of `pointer`, `parameter` or `line` will be defined. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pointer** | **str** | Pointer to the path in the payload that caused this error. | [optional] 
**parameter** | **str** | Query parameter that caused this error. | [optional] 
**line** | **str** | Line number in uploaded multipart file that caused this error. &#39;N/A&#39; if unknown. | [optional] 
**resource** | **str** | Pointer to the resource that caused this error. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


