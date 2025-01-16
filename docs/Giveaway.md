# Giveaway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**code** | **str** | The code value of this giveaway. | 
**pool_id** | **int** | The ID of the pool to return giveaway codes from. | 
**start_date** | **datetime** | Timestamp at which point the giveaway becomes valid. | [optional] 
**end_date** | **datetime** | Timestamp at which point the giveaway becomes invalid. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this giveaway. | [optional] 
**used** | **bool** | Indicates whether this giveaway code was given before. | [optional] 
**import_id** | **int** | The ID of the Import which created this giveaway. | [optional] 
**profile_integration_id** | **str** | The third-party integration ID of the customer profile that was awarded the giveaway, if the giveaway was awarded. | [optional] 
**profile_id** | **int** | The internal ID of the customer profile that was awarded the giveaway, if the giveaway was awarded and an internal ID exists. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


