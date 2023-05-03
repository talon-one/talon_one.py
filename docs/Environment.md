# Environment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal ID of this entity. | 
**created** | **datetime** | The time this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**slots** | [**list[SlotDef]**](SlotDef.md) | The slots defined for this application. | 
**functions** | [**list[FunctionDef]**](FunctionDef.md) | The functions defined for this application. | 
**templates** | [**list[TemplateDef]**](TemplateDef.md) | The templates defined for this application. | 
**variables** | **str** | A stringified version of the environment&#39;s Talang variables scope. | 
**giveaways_pools** | [**list[GiveawaysPool]**](GiveawaysPool.md) | The giveaways pools that the application is subscribed to. | [optional] 
**loyalty_programs** | [**list[LoyaltyProgram]**](LoyaltyProgram.md) | The loyalty programs that the application is subscribed to. | [optional] 
**attributes** | [**list[Attribute]**](Attribute.md) | The attributes that the application is subscribed to. | [optional] 
**additional_costs** | [**list[AccountAdditionalCost]**](AccountAdditionalCost.md) | The additional costs that the application is subscribed to. | [optional] 
**audiences** | [**list[Audience]**](Audience.md) | The audiences contained in the account which the application belongs to. | [optional] 
**collections** | [**list[Collection]**](Collection.md) | The account-level collections that the application is subscribed to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


