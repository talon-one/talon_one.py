# ApplicationCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. The time this entity was created. The time this entity was created. The time this entity was created. | 
**integration_id** | **str** | The integration ID set by your integration layer. The integration ID set by your integration layer. | 
**attributes** | [**object**](.md) | Arbitrary properties associated with this item. | 
**account_id** | **int** | The ID of the Talon.One account that owns this profile. The ID of the Talon.One account that owns this profile. | 
**closed_sessions** | **int** | The total amount of closed sessions by a customer. A closed session is a successful purchase. | 
**total_sales** | **float** | The total amount of money spent by the customer **before** discounts are applied.  The total sales amount excludes the following: - Cancelled or reopened sessions. - Returned items.  | 
**loyalty_memberships** | [**list[LoyaltyMembership]**](LoyaltyMembership.md) | **DEPRECATED** A list of loyalty programs joined by the customer.  | [optional] 
**audience_memberships** | [**list[AudienceMembership]**](AudienceMembership.md) | The audiences the customer belongs to. | [optional] 
**last_activity** | **datetime** | Timestamp of the most recent event received from this customer. This field is updated on calls that trigger the rule-engine and that are not [dry requests](https://docs.talon.one/docs/dev/integration-api/dry-requests/#overlay).  For example, [reserving a coupon](https://docs.talon.one/integration-api#operation/createCouponReservation) for a customer doesn&#39;t impact this field.  | 
**sandbox** | **bool** | Shows whether the customer is part of a sandbox or live Application. See the [docs](https://docs.talon.one/docs/product/applications/overview#application-environments).  | [optional] 
**advocate_integration_id** | **str** | The Integration ID of the Customer Profile that referred this Customer in the Application. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


