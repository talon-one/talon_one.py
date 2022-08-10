# CampaignPrioritiesChangedNotification

Notification about an Application whose campaigns' priorities changed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | 
**old_priorities** | **dict(str, list[int])** | Campaign IDs for each priority. The priority can be one of: [&#39;universal&#39;, &#39;stackable&#39;, &#39;exclusive&#39;]  | [optional] 
**priorities** | **dict(str, list[int])** | Campaign IDs for each priority. The priority can be one of: [&#39;universal&#39;, &#39;stackable&#39;, &#39;exclusive&#39;]  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


