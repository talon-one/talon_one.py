# NewDigitalPass

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loyalty_program_id** | **int** | The ID of the associated loyalty program. | 
**pass_template_id** | **str** | The ID of the digital pass template used to generate the pass.  | 
**profile_id** | **str** | The integration ID of the customer profile the pass is issued for. | 
**loyalty_card_id** | **str** | The identifier of the loyalty card the pass is issued for.  **Note**: Only applicable for card-based loyalty programs.  | [optional] 
**platform** | **str** | The wallet platform the pass is generated for. | 
**attributes** | **dict(str, str)** | A map of placeholder values that you provide to fill in the pass template. These values are not validated against the template.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


