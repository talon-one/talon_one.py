# LoyaltyPoints

Points to add or deduct.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **float** | Amount of loyalty points. | 
**name** | **str** | Allows to specify a name/reason for the point addition or deduction. | [optional] 
**validity_duration** | **str** | Indicates the duration after which the added loyalty points should expire. The format is a number followed by one letter indicating the time unit, like &#39;1h&#39; or &#39;40m&#39; (defined by Go time package). | [optional] 
**pending_duration** | **str** | Indicates the amount of time before the points are considered valid. The format is a number followed by one letter indicating the time unit, like &#39;1h&#39; or &#39;40m&#39; (defined by Go time package). | [optional] 
**sub_ledger_id** | **str** | This specifies if we are adding loyalty points to the main ledger or a subledger. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


