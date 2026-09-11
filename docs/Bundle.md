# Bundle

A named bundle definition consisting of selector sources with matching constraints. Replaces `bundle` [bindings](https://docs.talon.one/management-api#tag/Campaigns/operation/getRuleset.responses.200.bindings) in V1 rulesets.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier derived from the bundle content. | 
**name** | **str** | The name of the bundle. | 
**type** | **str** | A binding of type &#x60;bundle&#x60;. | 
**sources** | **list[str]** | The selector sources of bundle items. Each source is expressed as a &#x60;{{$selectorName}}&#x60; reference. | 
**counts** | **list[int]** | The number of items to retrieve from each corresponding source in &#x60;sources&#x60;. | 
**matchers** | **list[str]** | Attribute names that the bundled items must share. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


