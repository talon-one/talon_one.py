# UpdateLoyaltyProgram

Update Loyalty Program
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display title for the Loyalty Program. | [optional] 
**description** | **str** | Description of our Loyalty Program. | [optional] 
**subscribed_applications** | **list[int]** | A list containing the IDs of all applications that are subscribed to this Loyalty Program. | [optional] 
**default_validity** | **str** | Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like &#39;1h&#39; or &#39;40m&#39;. | [optional] 
**default_pending** | **str** | Indicates the default duration for the pending time, after which points will be valid. The format is a number followed by a duration unit, like &#39;1h&#39; or &#39;40m&#39;. | [optional] 
**allow_subledger** | **bool** | Indicates if this program supports subledgers inside the program | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


