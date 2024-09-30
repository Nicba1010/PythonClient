# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.appendix_app_data_limits_rates_data_info import AppendixAppDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_appendixs_rates_data_info import AppendixAppendixsRatesDataInfo
from dataforseo_client.models.appendix_backlinks_day_statistics_rates_data import AppendixBacklinksDayStatisticsRatesData
from dataforseo_client.models.appendix_business_data_limits_rates_data_info import AppendixBusinessDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_content_analysis_limits_rates_data_info import AppendixContentAnalysisLimitsRatesDataInfo
from dataforseo_client.models.appendix_content_generation_limits_rates_data_info import AppendixContentGenerationLimitsRatesDataInfo
from dataforseo_client.models.appendix_dataforseo_labs_limits_rates_data_info import AppendixDataforseoLabsLimitsRatesDataInfo
from dataforseo_client.models.appendix_domain_analytics_limits_rates_data_info import AppendixDomainAnalyticsLimitsRatesDataInfo
from dataforseo_client.models.appendix_keywords_datas_rates_data_info import AppendixKeywordsDatasRatesDataInfo
from dataforseo_client.models.appendix_merchant_limits_rates_data_info import AppendixMerchantLimitsRatesDataInfo
from dataforseo_client.models.appendix_on_page_limits_rates_data_info import AppendixOnPageLimitsRatesDataInfo
from dataforseo_client.models.appendix_serp_limits_rates_data_info import AppendixSerpLimitsRatesDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixMinuteStatisticsMoneyData(BaseModel):
    """
    AppendixMinuteStatisticsMoneyData
    """ # noqa: E501
    serp: Optional[AppendixSerpLimitsRatesDataInfo] = None
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total amount of money deposited to your account")
    total_serp: Optional[Union[StrictFloat, StrictInt]] = None
    keywords_data: Optional[AppendixKeywordsDatasRatesDataInfo] = None
    total_keywords_data: Optional[Union[StrictFloat, StrictInt]] = None
    appendix: Optional[AppendixAppendixsRatesDataInfo] = None
    total_appendix: Optional[Union[StrictFloat, StrictInt]] = None
    dataforseo_labs: Optional[AppendixDataforseoLabsLimitsRatesDataInfo] = None
    total_dataforseo_labs: Optional[Union[StrictFloat, StrictInt]] = None
    domain_analytics: Optional[AppendixDomainAnalyticsLimitsRatesDataInfo] = None
    total_domain_analytics: Optional[Union[StrictFloat, StrictInt]] = None
    merchant: Optional[AppendixMerchantLimitsRatesDataInfo] = None
    total_merchant: Optional[Union[StrictFloat, StrictInt]] = None
    on_page: Optional[AppendixOnPageLimitsRatesDataInfo] = None
    total_on_page: Optional[Union[StrictFloat, StrictInt]] = None
    business_data: Optional[AppendixBusinessDataLimitsRatesDataInfo] = None
    total_business_data: Optional[Union[StrictFloat, StrictInt]] = None
    backlinks: Optional[AppendixBacklinksDayStatisticsRatesData] = None
    total_backlinks: Optional[Union[StrictFloat, StrictInt]] = None
    app_data: Optional[AppendixAppDataLimitsRatesDataInfo] = None
    total_app_data: Optional[Union[StrictFloat, StrictInt]] = None
    content_analysis: Optional[AppendixContentAnalysisLimitsRatesDataInfo] = None
    total_content_analysis: Optional[Union[StrictFloat, StrictInt]] = None
    content_generation: Optional[AppendixContentGenerationLimitsRatesDataInfo] = None
    total_content_generation: Optional[Union[StrictFloat, StrictInt]] = None
    value: Optional[StrictStr] = Field(default=None, description="time period for grouping day in the yyyy-MM-dd format minute in the yyyy-MM-dd HH:mm format")
    __properties: ClassVar[List[str]] = ["serp", "total", "total_serp", "keywords_data", "total_keywords_data", "appendix", "total_appendix", "dataforseo_labs", "total_dataforseo_labs", "domain_analytics", "total_domain_analytics", "merchant", "total_merchant", "on_page", "total_on_page", "business_data", "total_business_data", "backlinks", "total_backlinks", "app_data", "total_app_data", "content_analysis", "total_content_analysis", "content_generation", "total_content_generation", "value"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppendixMinuteStatisticsMoneyData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of serp
        if self.serp:
            _dict['serp'] = self.serp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_data
        if self.keywords_data:
            _dict['keywords_data'] = self.keywords_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of appendix
        if self.appendix:
            _dict['appendix'] = self.appendix.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dataforseo_labs
        if self.dataforseo_labs:
            _dict['dataforseo_labs'] = self.dataforseo_labs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_analytics
        if self.domain_analytics:
            _dict['domain_analytics'] = self.domain_analytics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict['merchant'] = self.merchant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of on_page
        if self.on_page:
            _dict['on_page'] = self.on_page.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_data
        if self.business_data:
            _dict['business_data'] = self.business_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backlinks
        if self.backlinks:
            _dict['backlinks'] = self.backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_data
        if self.app_data:
            _dict['app_data'] = self.app_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content_analysis
        if self.content_analysis:
            _dict['content_analysis'] = self.content_analysis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content_generation
        if self.content_generation:
            _dict['content_generation'] = self.content_generation.to_dict()
        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if total_serp (nullable) is None
        # and model_fields_set contains the field
        if self.total_serp is None and "total_serp" in self.model_fields_set:
            _dict['total_serp'] = None

        # set to None if total_keywords_data (nullable) is None
        # and model_fields_set contains the field
        if self.total_keywords_data is None and "total_keywords_data" in self.model_fields_set:
            _dict['total_keywords_data'] = None

        # set to None if total_appendix (nullable) is None
        # and model_fields_set contains the field
        if self.total_appendix is None and "total_appendix" in self.model_fields_set:
            _dict['total_appendix'] = None

        # set to None if total_dataforseo_labs (nullable) is None
        # and model_fields_set contains the field
        if self.total_dataforseo_labs is None and "total_dataforseo_labs" in self.model_fields_set:
            _dict['total_dataforseo_labs'] = None

        # set to None if total_domain_analytics (nullable) is None
        # and model_fields_set contains the field
        if self.total_domain_analytics is None and "total_domain_analytics" in self.model_fields_set:
            _dict['total_domain_analytics'] = None

        # set to None if total_merchant (nullable) is None
        # and model_fields_set contains the field
        if self.total_merchant is None and "total_merchant" in self.model_fields_set:
            _dict['total_merchant'] = None

        # set to None if total_on_page (nullable) is None
        # and model_fields_set contains the field
        if self.total_on_page is None and "total_on_page" in self.model_fields_set:
            _dict['total_on_page'] = None

        # set to None if total_business_data (nullable) is None
        # and model_fields_set contains the field
        if self.total_business_data is None and "total_business_data" in self.model_fields_set:
            _dict['total_business_data'] = None

        # set to None if total_backlinks (nullable) is None
        # and model_fields_set contains the field
        if self.total_backlinks is None and "total_backlinks" in self.model_fields_set:
            _dict['total_backlinks'] = None

        # set to None if total_app_data (nullable) is None
        # and model_fields_set contains the field
        if self.total_app_data is None and "total_app_data" in self.model_fields_set:
            _dict['total_app_data'] = None

        # set to None if total_content_analysis (nullable) is None
        # and model_fields_set contains the field
        if self.total_content_analysis is None and "total_content_analysis" in self.model_fields_set:
            _dict['total_content_analysis'] = None

        # set to None if total_content_generation (nullable) is None
        # and model_fields_set contains the field
        if self.total_content_generation is None and "total_content_generation" in self.model_fields_set:
            _dict['total_content_generation'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixMinuteStatisticsMoneyData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serp": AppendixSerpLimitsRatesDataInfo.from_dict(obj["serp"]) if obj.get("serp") is not None else None,
            "total": obj.get("total"),
            "total_serp": obj.get("total_serp"),
            "keywords_data": AppendixKeywordsDatasRatesDataInfo.from_dict(obj["keywords_data"]) if obj.get("keywords_data") is not None else None,
            "total_keywords_data": obj.get("total_keywords_data"),
            "appendix": AppendixAppendixsRatesDataInfo.from_dict(obj["appendix"]) if obj.get("appendix") is not None else None,
            "total_appendix": obj.get("total_appendix"),
            "dataforseo_labs": AppendixDataforseoLabsLimitsRatesDataInfo.from_dict(obj["dataforseo_labs"]) if obj.get("dataforseo_labs") is not None else None,
            "total_dataforseo_labs": obj.get("total_dataforseo_labs"),
            "domain_analytics": AppendixDomainAnalyticsLimitsRatesDataInfo.from_dict(obj["domain_analytics"]) if obj.get("domain_analytics") is not None else None,
            "total_domain_analytics": obj.get("total_domain_analytics"),
            "merchant": AppendixMerchantLimitsRatesDataInfo.from_dict(obj["merchant"]) if obj.get("merchant") is not None else None,
            "total_merchant": obj.get("total_merchant"),
            "on_page": AppendixOnPageLimitsRatesDataInfo.from_dict(obj["on_page"]) if obj.get("on_page") is not None else None,
            "total_on_page": obj.get("total_on_page"),
            "business_data": AppendixBusinessDataLimitsRatesDataInfo.from_dict(obj["business_data"]) if obj.get("business_data") is not None else None,
            "total_business_data": obj.get("total_business_data"),
            "backlinks": AppendixBacklinksDayStatisticsRatesData.from_dict(obj["backlinks"]) if obj.get("backlinks") is not None else None,
            "total_backlinks": obj.get("total_backlinks"),
            "app_data": AppendixAppDataLimitsRatesDataInfo.from_dict(obj["app_data"]) if obj.get("app_data") is not None else None,
            "total_app_data": obj.get("total_app_data"),
            "content_analysis": AppendixContentAnalysisLimitsRatesDataInfo.from_dict(obj["content_analysis"]) if obj.get("content_analysis") is not None else None,
            "total_content_analysis": obj.get("total_content_analysis"),
            "content_generation": AppendixContentGenerationLimitsRatesDataInfo.from_dict(obj["content_generation"]) if obj.get("content_generation") is not None else None,
            "total_content_generation": obj.get("total_content_generation"),
            "value": obj.get("value")
        })
        return _obj


