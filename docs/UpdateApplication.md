# UpdateApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this application. | 
**description** | **str** | A longer description of the application. | [optional] 
**timezone** | **str** | A string containing an IANA timezone descriptor. | 
**currency** | **str** | A string describing a default currency for new customer sessions. | 
**case_sensitivity** | **str** | A string indicating how should campaigns in this application deal with case sensitivity on coupon codes. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Default limits for campaigns created in this application | [optional] 
**attributes_settings** | [**AttributesSettings**](AttributesSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


