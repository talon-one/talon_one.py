# IntegrationRequest

The body of a V2 integration API request (customer session update). Next to the customer session details, this contains an optional listing of extra properties that should be returned in the response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_session** | [**NewCustomerSessionV2**](NewCustomerSessionV2.md) |  | 
**response_content** | **list[str]** | Extends the response with the chosen data entities. Use this property to get as much data as you need in one _Update customer session_ request instead of sending extra requests to other endpoints.  **Note:** To retrieve loyalty card details, your request must include a loyalty card ID.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


