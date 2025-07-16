# SamlConnection

A SAML 2.0 connection.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assertion_consumer_service_url** | **str** | The location where the SAML assertion is sent with a HTTP POST. | 
**account_id** | **int** | The ID of the account that owns this entity. | 
**name** | **str** | ID of the SAML service. | 
**enabled** | **bool** | Determines if this SAML connection active. | 
**issuer** | **str** | Identity Provider Entity ID. | 
**sign_on_url** | **str** | Single Sign-On URL. | 
**sign_out_url** | **str** | Single Sign-Out URL. | [optional] 
**metadata_url** | **str** | Metadata URL. | [optional] 
**audience_uri** | **str** | The application-defined unique identifier that is the intended audience of the SAML assertion. This is most often the SP Entity ID of your application. When not specified, the ACS URL will be used.  | 
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


