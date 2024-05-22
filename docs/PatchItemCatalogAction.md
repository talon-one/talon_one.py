# PatchItemCatalogAction

The specific properties of the \"PATCH\" catalog sync action.  **Note:**   - If you do not provide a new `price` value, the existing `price` value is retained.   - If you do not provide a new `product` value, the `product` value is set to `null`. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | The unique SKU of the item to patch. | 
**price** | **float** | Price of the item. | [optional] 
**attributes** | [**object**](.md) | The attributes of the item to patch. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**create_if_not_exists** | **bool** | Indicates whether to create an item if the SKU does not exist. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


