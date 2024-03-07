[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_technologies** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**domains_by_technology** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**languages** | **float** |  | [optional]
**locations** | **float** |  | [optional]
**technologies** | **float** |  | [optional]
**aggregation_technologies** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**technologies_summary** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**domains_by_html_terms** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**technology_stats** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_technologies_domain_analytics_limits_rates_data_info import AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo from a JSON string
appendix_technologies_domain_analytics_limits_rates_data_info_instance = AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_technologies_domain_analytics_limits_rates_data_info_dict = appendix_technologies_domain_analytics_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo from a dict
appendix_technologies_domain_analytics_limits_rates_data_info_form_dict = appendix_technologies_domain_analytics_limits_rates_data_info.from_dict(appendix_technologies_domain_analytics_limits_rates_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")