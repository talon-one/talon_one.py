# CustomerActivityReport

A summary report of customer activity for a given time range.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The integration ID set by your integration layer. | 
**created** | **datetime** | The time this entity was created. | 
**name** | **str** | The name for this customer profile. | 
**customer_id** | **int** | The internal Talon.One ID of the customer. | 
**last_activity** | **datetime** | The last activity of the customer. | [optional] 
**coupon_redemptions** | **int** | Number of coupon redemptions in all customer campaigns. | 
**coupon_use_attempts** | **int** | Number of coupon use attempts in all customer campaigns. | 
**coupon_failed_attempts** | **int** | Number of failed coupon use attempts in all customer campaigns. | 
**accrued_discounts** | **float** | Number of accrued discounts in all customer campaigns. | 
**accrued_revenue** | **float** | Amount of accrued revenue in all customer campaigns. | 
**total_orders** | **int** | Number of orders in all customer campaigns. | 
**total_orders_no_coupon** | **int** | Number of orders without coupon used in all customer campaigns. | 
**campaign_name** | **str** | The name of the campaign this customer belongs to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


