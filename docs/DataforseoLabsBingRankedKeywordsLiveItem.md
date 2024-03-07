[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsBingRankedKeywordsLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**keyword_data** | [**KeywordDataInfo**](KeywordDataInfo.md) |  | [optional]
**ranked_serp_element** | [**RankedSerpElement**](RankedSerpElement.md) |  | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_ranked_keywords_live_item import DataforseoLabsBingRankedKeywordsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingRankedKeywordsLiveItem from a JSON string
dataforseo_labs_bing_ranked_keywords_live_item_instance = DataforseoLabsBingRankedKeywordsLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingRankedKeywordsLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_bing_ranked_keywords_live_item_dict = dataforseo_labs_bing_ranked_keywords_live_item_instance.to_dict()
# create an instance of DataforseoLabsBingRankedKeywordsLiveItem from a dict
dataforseo_labs_bing_ranked_keywords_live_item_form_dict = dataforseo_labs_bing_ranked_keywords_live_item.from_dict(dataforseo_labs_bing_ranked_keywords_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")