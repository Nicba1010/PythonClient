# DataforseoLabsGoogleAvailableHistoryTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier unique task identifier in our system in the UUID format | [optional] 
**status_code** | **int** | status code of the task generated by DataForSEO, can be within the following range: 10000-60000 you can find the full list of the response codes here | [optional] 
**status_message** | **str** | informational message of the task you can find the full list of general informational messages here | [optional] 
**time** | **str** | execution time, seconds | [optional] 
**cost** | **float** | total tasks cost, USD | [optional] 
**result_count** | **int** | number of elements in the result array | [optional] 
**path** | **List[Optional[str]]** | URL path | [optional] 
**data** | **object** | contains the same parameters that you specified in the POST request | [optional] 
**result** | [**List[DataforseoLabsGoogleAvailableHistoryResultInfo]**](DataforseoLabsGoogleAvailableHistoryResultInfo.md) | array of objects containing results | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_available_history_task_info import DataforseoLabsGoogleAvailableHistoryTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleAvailableHistoryTaskInfo from a JSON string
dataforseo_labs_google_available_history_task_info_instance = DataforseoLabsGoogleAvailableHistoryTaskInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleAvailableHistoryTaskInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_available_history_task_info_dict = dataforseo_labs_google_available_history_task_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleAvailableHistoryTaskInfo from a dict
dataforseo_labs_google_available_history_task_info_form_dict = dataforseo_labs_google_available_history_task_info.from_dict(dataforseo_labs_google_available_history_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

