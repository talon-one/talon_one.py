# Giveaway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. | 
**created** | **datetime** | The exact moment this entity was created. | 
**code** | **str** | The code value of this giveaway. | 
**pool_id** | **int** | The ID of the pool to return giveaway codes from. | 
**start_date** | **datetime** | Timestamp at which point the giveaway becomes valid. | [optional] 
**end_date** | **datetime** | Timestamp at which point the giveaway becomes invalid. | [optional] 
**attributes** | [**object**](.md) | Arbitrary properties associated with this giveaway. | [optional] 
**used** | **bool** | Flag indicating whether this giveaway code was given before. | [optional] 
**import_id** | **int** | The ID of the Import which created this giveaway. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


