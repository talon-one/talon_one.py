# IntegrationRequest

The body of a V2 integration API request (customer session update). Next to the customer session details, this contains an optional listing of extra properties that should be returned in the response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_session** | [**NewCustomerSessionV2**](NewCustomerSessionV2.md) |  | 
**response_content** | **list[str]** | Optional list of requested information to be present on the response related to the customer session update. Currently supported: \&quot;customerSession\&quot;, \&quot;customerProfile\&quot;, \&quot;coupons\&quot;, \&quot;triggeredCampaigns\&quot;, \&quot;referral\&quot;, \&quot;loyalty\&quot; and \&quot;event\&quot;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


