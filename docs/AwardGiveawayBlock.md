# AwardGiveawayBlock

A block that awards a giveaway item from a configured giveaway pool to the specified customer profile.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**giveaway_pool** | [**GiveawayPoolReference**](GiveawayPoolReference.md) |  | 
**profile** | **str** | The customer profile to award the giveaway to. &#x60;Current&#x60; targets the customer in the current session; &#x60;Advocate&#x60; targets the person who invited their friend via referral program. | 
**on_failure** | **list[object]** | Blocks evaluated when this block fails or returns false. | [optional] 
**on_error** | **dict(str, list[object])** | Named error handlers evaluated when a specific error occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


