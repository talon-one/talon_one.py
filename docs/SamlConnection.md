# SamlConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created** | **datetime** | Unix timestamp indicating when the session was first created. | 
**account_id** | **int** | The ID of the account that owns this SAML Service. | 
**assertion_consumer_service_url** | **str** | The location where the SAML assertion is sent with a HTTP POST. | 
**name** | **str** | ID of the SAML service. | 
**enabled** | **bool** | Determines if this SAML connection active. | 
**issuer** | **str** | Identity Provider Entity ID. | 
**sign_on_url** | **str** | Single Sign-On URL. | 
**sign_out_url** | **str** | Single Sign-Out URL. | [optional] 
**metadata_url** | **str** | Metadata URL. | [optional] 
**x509certificate** | **str** | X.509 Certificate. | 
**audience** | **str** | The application-defined unique identifier that is the intended audience of the SAML assertion.  This is most often the SP Entity ID of your application. When not specified, the ACS URL will be used.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


