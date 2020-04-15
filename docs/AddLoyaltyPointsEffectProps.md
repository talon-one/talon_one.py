# AddLoyaltyPointsEffectProps

The properties specific to the \"addLoyaltyPoints\" effect. This gets triggered whenever a validated rule contained an \"add loyalty\" effect. These points are automatically stored and managed inside Talon.One.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name/description of this loyalty point addition | 
**program_id** | **int** | The ID of the loyalty program where these points were added | 
**sub_ledger_id** | **str** | The ID of the subledger within the loyalty program where these points were added | 
**value** | **float** | The amount of points that were added | 
**recipient_integration_id** | **str** | The user for whom these points were added | 
**expiry_condition** | **str** | The amount of time (in days) these points are valid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


