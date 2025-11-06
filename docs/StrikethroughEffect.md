# StrikethroughEffect

The effect produced for the catalog item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** | The ID of the campaign that effect belongs to. | 
**ruleset_id** | **int** | The ID of the ruleset containing the rule that triggered this effect. | 
**rule_index** | **int** | The position of the rule that triggered this effect within the ruleset. | 
**rule_name** | **str** | The name of the rule that triggered this effect. | 
**type** | **str** | The type of this effect. | 
**props** | [**object**](.md) |  | 
**start_time** | **datetime** | The start of the time frame where the effect is active in UTC. | [optional] 
**end_time** | **datetime** | The end of the time frame where the effect is active in UTC. | [optional] 
**selected_price_type** | **str** | The selected price type for this cart item (e.g. the price for members only). | [optional] 
**selected_price** | **float** | The value of the selected price type to apply to the SKU targeted by this effect, before any discounts are applied. | [optional] 
**adjustment_reference_id** | **str** | The reference identifier of the selected price adjustment for this cart item. | [optional] 
**targets** | **list[object]** | A list of entities (e.g. audiences) targeted by this effect. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


