# CartItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of item. | [optional] 
**sku** | **str** | Stock keeping unit of item. | 
**quantity** | **int** | Number of units of this item. Due to [cart item flattening](https://docs.talon.one/docs/product/rules/understanding-cart-item-flattening), if you provide a quantity greater than 1, the item will be split in as many items as the provided quantity. This will impact the number of **per-item** effects triggered from your campaigns.  | 
**returned_quantity** | **int** | Number of returned items, calculated internally based on returns of this item. | [optional] 
**remaining_quantity** | **int** | Remaining quantity of the item, calculated internally based on returns of this item. | [optional] 
**price** | **float** | Price of the item in the currency defined by your Application. This field is required if this item is not part of a [catalog](https://docs.talon.one/docs/product/account/dev-tools/managing-cart-item-catalogs). If it is part of a catalog, setting a price here overrides the price from the catalog.  | [optional] 
**category** | **str** | Type, group or model of the item. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**weight** | **float** | Weight of item in grams. | [optional] 
**height** | **float** | Height of item in mm. | [optional] 
**width** | **float** | Width of item in mm. | [optional] 
**length** | **float** | Length of item in mm. | [optional] 
**position** | **float** | Position of the Cart Item in the Cart (calculated internally). | [optional] 
**attributes** | [**object**](.md) | Use this property to set a value for the attributes of your choice. [Attributes](https://docs.talon.one/docs/dev/concepts/attributes) represent any information to attach to this cart item.  Custom _cart item_ attributes must be created in the Campaign Manager before you set them with this property.  **Note:** Any previously defined attributes that you do not include in the array will be removed.  | [optional] 
**additional_costs** | [**dict(str, AdditionalCost)**](AdditionalCost.md) | Use this property to set a value for the additional costs of this item, such as a shipping cost. They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).  | [optional] 
**catalog_item_id** | **int** | The [catalog item ID](https://docs.talon.one/docs/product/account/dev-tools/managing-cart-item-catalogs/#synchronizing-a-cart-item-catalog). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


