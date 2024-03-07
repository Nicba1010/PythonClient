[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpGoogleLocalFinderTaskGetAdvancedTaskInfo

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
**result** | [**List[SerpGoogleLocalFinderTaskGetAdvancedResultInfo]**](SerpGoogleLocalFinderTaskGetAdvancedResultInfo.md) | array of results | [optional]

## Example

```python
from dataforseo_client.models.serp_google_local_finder_task_get_advanced_task_info import SerpGoogleLocalFinderTaskGetAdvancedTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleLocalFinderTaskGetAdvancedTaskInfo from a JSON string
serp_google_local_finder_task_get_advanced_task_info_instance = SerpGoogleLocalFinderTaskGetAdvancedTaskInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleLocalFinderTaskGetAdvancedTaskInfo.to_json()

# convert the object into a dict
serp_google_local_finder_task_get_advanced_task_info_dict = serp_google_local_finder_task_get_advanced_task_info_instance.to_dict()
# create an instance of SerpGoogleLocalFinderTaskGetAdvancedTaskInfo from a dict
serp_google_local_finder_task_get_advanced_task_info_form_dict = serp_google_local_finder_task_get_advanced_task_info.from_dict(serp_google_local_finder_task_get_advanced_task_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")