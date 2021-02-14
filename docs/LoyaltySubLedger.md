# LoyaltySubLedger

Ledger of Balance in Loyalty Program for a Customer
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | ⚠️ Deprecated: Use &#39;totalActivePoints&#39; property instead. Total amount of currently active and available points in the customer&#39;s balance  | 
**total_active_points** | **float** | Total amount of currently active and available points in the customer&#39;s balance | 
**total_pending_points** | **float** | Total amount of pending points, which are not active yet but will become active in the future | 
**total_spent_points** | **float** | Total amount of points already spent by this customer | 
**total_expired_points** | **float** | Total amount of points, that expired without ever being spent | 
**transactions** | [**list[LoyaltyLedgerEntry]**](LoyaltyLedgerEntry.md) | List of all events that have happened such as additions, subtractions and expiries | [optional] 
**expiring_points** | [**list[LoyaltyLedgerEntry]**](LoyaltyLedgerEntry.md) | List of all points that will expire | [optional] 
**active_points** | [**list[LoyaltyLedgerEntry]**](LoyaltyLedgerEntry.md) | List of all currently active points | [optional] 
**pending_points** | [**list[LoyaltyLedgerEntry]**](LoyaltyLedgerEntry.md) | List of all points pending activation | [optional] 
**expired_points** | [**list[LoyaltyLedgerEntry]**](LoyaltyLedgerEntry.md) | List of expired points | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


