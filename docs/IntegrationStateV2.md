# IntegrationStateV2

Contains all entities that might interest Talon.One integrations. This is the response type returned by the V2 PUT customer_session endpoint 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_session** | [**CustomerSessionV2**](CustomerSessionV2.md) |  | [optional] 
**customer_profile** | [**CustomerProfile**](CustomerProfile.md) |  | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 
**loyalty** | [**Loyalty**](Loyalty.md) |  | [optional] 
**referral** | [**Referral**](Referral.md) |  | [optional] 
**coupons** | [**list[Coupon]**](Coupon.md) |  | [optional] 
**triggered_campaigns** | [**list[Campaign]**](Campaign.md) |  | [optional] 
**effects** | [**list[Effect]**](Effect.md) |  | 
**created_coupons** | [**list[Coupon]**](Coupon.md) |  | 
**created_referrals** | [**list[Referral]**](Referral.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


