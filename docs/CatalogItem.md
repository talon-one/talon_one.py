# CatalogItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**sku** | **str** | The stock keeping unit of the item. | 
**price** | **float** | Price of the item. | [optional] 
**catalogid** | **int** | The ID of the catalog the item belongs to. | 
**version** | **int** | The version of the catalog item. | 
**attributes** | [**list[ItemAttribute]**](ItemAttribute.md) |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


