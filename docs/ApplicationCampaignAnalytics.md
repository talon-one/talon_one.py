# ApplicationCampaignAnalytics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | The start of the aggregation time frame in UTC. | [optional] 
**end_time** | **datetime** | The end of the aggregation time frame in UTC. | [optional] 
**campaign_id** | **int** | The ID of the campaign. | [optional] 
**campaign_name** | **str** | The name of the campaign. | [optional] 
**campaign_tags** | **list[str]** | A list of tags for the campaign. | [optional] 
**campaign_state** | **str** | The state of the campaign.  **Note:** A disabled or archived campaign is not evaluated for rules or coupons.  | [optional] [default to 'enabled']
**campaign_active_ruleset_id** | **int** | The [ID of the ruleset](https://docs.talon.one/management-api#operation/getRulesets) this campaign applies on customer session evaluation.  | [optional] 
**campaign_start_time** | **datetime** | Date and time when the campaign becomes active. | [optional] 
**campaign_end_time** | **datetime** | Date and time when the campaign becomes inactive. | [optional] 
**total_revenue** | [**ApplicationCampaignAnalyticsTotalRevenue**](ApplicationCampaignAnalyticsTotalRevenue.md) |  | [optional] 
**sessions_count** | [**ApplicationCampaignAnalyticsSessionsCount**](ApplicationCampaignAnalyticsSessionsCount.md) |  | [optional] 
**avg_items_per_session** | [**ApplicationCampaignAnalyticsAvgItemsPerSession**](ApplicationCampaignAnalyticsAvgItemsPerSession.md) |  | [optional] 
**avg_session_value** | [**ApplicationCampaignAnalyticsAvgSessionValue**](ApplicationCampaignAnalyticsAvgSessionValue.md) |  | [optional] 
**total_discounts** | [**ApplicationCampaignAnalyticsTotalDiscounts**](ApplicationCampaignAnalyticsTotalDiscounts.md) |  | [optional] 
**coupons_count** | [**ApplicationCampaignAnalyticsCouponsCount**](ApplicationCampaignAnalyticsCouponsCount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


