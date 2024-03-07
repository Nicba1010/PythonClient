[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksAvailableFiltersTaskInfo

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
**result** | [**List[BacklinksAvailableFiltersResultInfo]**](BacklinksAvailableFiltersResultInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.backlinks_available_filters_task_info import BacklinksAvailableFiltersTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksAvailableFiltersTaskInfo from a JSON string
backlinks_available_filters_task_info_instance = BacklinksAvailableFiltersTaskInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksAvailableFiltersTaskInfo.to_json()

# convert the object into a dict
backlinks_available_filters_task_info_dict = backlinks_available_filters_task_info_instance.to_dict()
# create an instance of BacklinksAvailableFiltersTaskInfo from a dict
backlinks_available_filters_task_info_form_dict = backlinks_available_filters_task_info.from_dict(backlinks_available_filters_task_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")