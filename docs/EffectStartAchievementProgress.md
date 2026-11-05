# EffectStartAchievementProgress

The `startAchievementProgress` effect and its properties. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **int** | The ID of the experiment that campaign belongs to. | [optional] 
**campaign_id** | **int** | The ID of the campaign that triggered this effect. | 
**ruleset_id** | **int** | The ID of the ruleset that was active in the campaign when this effect was triggered. | 
**rule_index** | **int** | The position of the rule that triggered this effect within the ruleset. | 
**rule_name** | **str** | The name of the rule that triggered this effect. | 
**effect_type** | **str** | An effect discriminator of type &#x60;startAchievementProgress&#x60;. | 
**triggered_by_coupon** | **int** | The ID of the coupon that was being evaluated when this effect was triggered. | [optional] 
**triggered_for_catalog_item** | **int** | The ID of the catalog item that was being evaluated when this effect was triggered. | [optional] 
**condition_index** | **int** | The index of the condition that was triggered. | [optional] 
**evaluation_group_id** | **int** | The ID of the evaluation group. For more information, see [Managing campaign evaluation](https://docs.talon.one/docs/product/applications/managing-campaign-evaluation). | [optional] 
**evaluation_group_mode** | **str** | The evaluation mode of the evaluation group. For more information, see [Managing campaign evaluation](https://docs.talon.one/docs/product/applications/managing-campaign-evaluation). | [optional] 
**campaign_revision_id** | **int** | The revision ID of the campaign that was used when triggering the effect. | [optional] 
**campaign_revision_version_id** | **int** | The revision version ID of the campaign that was used when triggering the effect. | [optional] 
**selected_price_type** | **str** | The selected price type for the SKU targeted by this effect. | [optional] 
**selected_price** | **float** | The value of the selected price type to apply to the SKU targeted by this effect, before any discounts are applied. | [optional] 
**adjustment_reference_id** | **str** | The reference identifier of the selected price adjustment for this SKU. This is only returned if the &#x60;selectedPrice&#x60; resulted from a price adjustment. | [optional] 
**reward_id** | **int** | The ID of the reward that was being evaluated when this effect was triggered. | [optional] 
**reward_integration_id** | **str** | The integration ID of the specific customer reward whose usage produced this effect. | [optional] 
**props** | [**StartAchievementProgressEffectProps**](StartAchievementProgressEffectProps.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


