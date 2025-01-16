# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**modified** | **datetime** | The time this entity was last modified. | 
**company_name** | **str** |  | 
**domain_name** | **str** | Subdomain Name for yourcompany.talon.one. | 
**state** | **str** | State of the account (active, deactivated). | 
**billing_email** | **str** | The billing email address associated with your company account. | 
**plan_name** | **str** | The name of your booked plan. | [optional] 
**plan_expires** | **datetime** | The point in time at which your current plan expires. | [optional] 
**application_limit** | **int** | The maximum number of Applications covered by your plan. | [optional] 
**user_limit** | **int** | The maximum number of Campaign Manager Users covered by your plan. | [optional] 
**campaign_limit** | **int** | The maximum number of Campaigns covered by your plan. | [optional] 
**api_limit** | **int** | The maximum number of Integration API calls covered by your plan per billing period. | [optional] 
**application_count** | **int** | The current number of Applications in your account. | 
**user_count** | **int** | The current number of Campaign Manager Users in your account. | 
**campaigns_active_count** | **int** | The current number of active Campaigns in your account. | 
**campaigns_inactive_count** | **int** | The current number of inactive Campaigns in your account. | 
**attributes** | [**object**](.md) | Arbitrary properties associated with this campaign. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


