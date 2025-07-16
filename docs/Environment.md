# Environment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**application_id** | **int** | The ID of the Application that owns this entity. | 
**slots** | [**list[SlotDef]**](SlotDef.md) | The slots defined for this application. | 
**functions** | [**list[FunctionDef]**](FunctionDef.md) | The functions defined for this application. | 
**templates** | [**list[TemplateDef]**](TemplateDef.md) | The templates defined for this application. | 
**variables** | **str** | A stringified version of the environment&#39;s Talang variables scope. | 
**giveaways_pools** | [**list[GiveawaysPool]**](GiveawaysPool.md) | The giveaways pools that the application is subscribed to. | [optional] 
**loyalty_programs** | [**list[LoyaltyProgram]**](LoyaltyProgram.md) | The loyalty programs that the application is subscribed to. | [optional] 
**achievements** | [**list[Achievement]**](Achievement.md) | The achievements, linked to the campaigns, belonging to the application. | [optional] 
**attributes** | [**list[Attribute]**](Attribute.md) | The attributes that the application is subscribed to. | [optional] 
**additional_costs** | [**list[AccountAdditionalCost]**](AccountAdditionalCost.md) | The additional costs that the application is subscribed to. | [optional] 
**audiences** | [**list[Audience]**](Audience.md) | The audiences contained in the account which the application belongs to. | [optional] 
**collections** | [**list[Collection]**](Collection.md) | The account-level collections that the application is subscribed to. | [optional] 
**application_cart_item_filters** | [**list[ApplicationCIF]**](ApplicationCIF.md) | The cart item filters belonging to the Application. | [optional] 
**price_types** | [**list[PriceType]**](PriceType.md) | The price types that this Application can use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


