# ShowNotificationBlock

A block that displays a notification to the customer with a configurable type, title, and optional body message.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this block. | [optional] [readonly] 
**type** | **str** | Identifies the block variant and determines which additional properties are present in it. | 
**tags** | **list[str]** | Semantic labels attached to this block. | [optional] [readonly] 
**notification_type** | **str** | The type of notification to display. | 
**title** | **str** | The notification heading shown to the customer. | 
**body** | **str** | The notification body text. Supports template placeholders (e.g. \&quot;{{$Session.Total}}\&quot;) evaluated at rule execution time. | [optional] 
**on_failure** | **list[object]** | Blocks evaluated when this block fails or returns false. | [optional] 
**on_error** | **dict(str, list[object])** | Named error handlers evaluated when a specific error occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


