# ScimServiceProviderConfigResponseBulk

Configuration related to bulk operations, which allow multiple SCIM requests to be processed in a single HTTP request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_operations** | **int** | The maximum number of individual operations that can be included in a single bulk request. | [optional] 
**max_payload_size** | **int** | The maximum size, in bytes, of the entire payload for a bulk operation request. | [optional] 
**supported** | **bool** | Indicates whether the SCIM service provider supports bulk operations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


