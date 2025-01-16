# NewAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | The name of the entity that can have this attribute. When creating or updating the entities of a given type, you can include an &#x60;attributes&#x60; object with keys corresponding to the &#x60;name&#x60; of the custom attributes for that type. | 
**event_type** | **str** |  | [optional] 
**name** | **str** | The attribute name that will be used in API requests and Talang. E.g. if &#x60;name &#x3D;&#x3D; \&quot;region\&quot;&#x60; then you would set the region attribute by including an &#x60;attributes.region&#x60; property in your request payload. | 
**title** | **str** | The human-readable name for the attribute that will be shown in the Campaign Manager. Like &#x60;name&#x60;, the combination of entity and title must also be unique. | 
**type** | **str** | The data type of the attribute, a &#x60;time&#x60; attribute must be sent as a string that conforms to the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp format. | 
**description** | **str** | A description of this attribute. | 
**suggestions** | **list[str]** | A list of suggestions for the attribute. | 
**has_allowed_list** | **bool** | Whether or not this attribute has an allowed list of values associated with it. | [optional] [default to False]
**restricted_by_suggestions** | **bool** | Whether or not this attribute&#39;s value is restricted by suggestions (&#x60;suggestions&#x60; property) or by an allowed list of value (&#x60;hasAllowedList&#x60; property).  | [optional] [default to False]
**editable** | **bool** | Whether or not this attribute can be edited. | 
**subscribed_applications_ids** | **list[int]** | A list of the IDs of the applications where this attribute is available. | [optional] 
**subscribed_catalogs_ids** | **list[int]** | A list of the IDs of the catalogs where this attribute is available. | [optional] 
**allowed_subscriptions** | **list[str]** | A list of allowed subscription types for this attribute.  **Note:** This only applies to attributes associated with the &#x60;CartItem&#x60; entity.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


