# Effect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | The ID of the campaign that triggered this effect. | 
**ruleset_id** | **int** | The ID of the ruleset that was active in the campaign when this effect was triggered. | 
**rule_index** | **int** | The position of the rule that triggered this effect within the ruleset. | 
**rule_name** | **str** | The name of the rule that triggered this effect. | 
**effect_type** | **str** | The type of effect that was triggered. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects). | 
**triggered_by_coupon** | **int** | The ID of the coupon that was being evaluated when this effect was triggered. | [optional] 
**triggered_for_catalog_item** | **int** | The ID of the catalog item that was being evaluated when this effect was triggered. | [optional] 
**condition_index** | **int** | The index of the condition that was triggered. | [optional] 
**props** | [**object**](.md) | The properties of the effect. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


