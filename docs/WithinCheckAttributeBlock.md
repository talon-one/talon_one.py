# WithinCheckAttributeBlock

Variant of `CheckAttributeBlock` for the `within` and `not(within)` operators, which require both a start and end value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | The range comparison operator. Must be &#x60;within&#x60; or &#x60;not(within)&#x60;. | [optional] 
**start** | [**object**](.md) | The start value for the &#x60;within&#x60; operator. | 
**end** | [**object**](.md) | The end value for the &#x60;within&#x60; operator. | 
**start_inclusive** | **bool** | When &#x60;true&#x60;, the &#x60;start&#x60; value is included in the range for the &#x60;within&#x60; operator. | [optional] 
**end_inclusive** | **bool** | When &#x60;true&#x60;, the &#x60;end&#x60; value is included in the range for the &#x60;within&#x60; operator. | [optional] 
**timezone_insensitive** | **bool** | Indicates whether the &#x60;within&#x60; operator ignores time zones and compares the wall-clock time only. When &#x60;false&#x60;, time zones are taken into account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


