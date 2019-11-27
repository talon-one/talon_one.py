# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**modified** | **datetime** | The exact moment this entity was last modified. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | The name of this application. | 
**description** | **str** | A longer description of the application. | [optional] 
**timezone** | **str** | A string containing an IANA timezone descriptor. | 
**currency** | **str** | A string describing a default currency for new customer sessions. | 
**case_sensitivity** | **str** | A string indicating how should campaigns in this application deal with case sensitivity on coupon codes. | [optional] 
**attributes** | **object** | Arbitrary properties associated with this campaign | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Default limits for campaigns created in this application | [optional] 
**key** | **str** | Hex key for HMAC-signing API calls as coming from this application (16 hex digits) | 
**loyalty_programs** | [**list[LoyaltyProgram]**](LoyaltyProgram.md) | An array containing all the loyalty programs to which this application is subscribed | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


