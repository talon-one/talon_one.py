# PatchManyItemsCatalogAction

The specific properties of the \"PATCH_MANY\" catalog sync action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | Price of the item. | [optional] 
**filters** | [**list[CatalogActionFilter]**](CatalogActionFilter.md) | The list of filters used to select the items to patch, joined by &#x60;AND&#x60;.  **Note:** Every item in the catalog will be modified if there are no filters.  | [optional] 
**attributes** | [**object**](.md) | The attributes of the items to patch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


