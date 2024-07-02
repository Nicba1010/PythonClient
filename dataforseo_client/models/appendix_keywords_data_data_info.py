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

from pydantic import BaseModel, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.appendix_bing_keywords_data_limits_rates_data_info import AppendixBingKeywordsDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_dataforseo_trends_keywords_data_limits_rates_data_info import AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_google_ads_keywords_data_limits_rates_data_info import AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_info import AppendixInfo
from dataforseo_client.models.appendix_naver_keywords_data_data_info import AppendixNaverKeywordsDataDataInfo
from dataforseo_client.models.appendix_serp_limits_rates_data_info import AppendixSerpLimitsRatesDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixKeywordsDataDataInfo(BaseModel):
    """
    AppendixKeywordsDataDataInfo
    """ # noqa: E501
    keywords_for_keywords: Optional[AppendixInfo] = None
    keywords_for_site: Optional[AppendixInfo] = None
    search_volume: Optional[AppendixInfo] = None
    ad_traffic_by_keywords: Optional[AppendixInfo] = None
    languages: Optional[Union[StrictFloat, StrictInt]] = None
    locations: Optional[Union[StrictFloat, StrictInt]] = None
    tasks_ready: Optional[Union[StrictFloat, StrictInt]] = None
    explore: Optional[AppendixInfo] = None
    categories: Optional[Union[StrictFloat, StrictInt]] = None
    errors: Optional[Union[StrictFloat, StrictInt]] = None
    bing: Optional[AppendixBingKeywordsDataLimitsRatesDataInfo] = None
    keyword_performance: Optional[AppendixInfo] = None
    locations_and_languages: Optional[Union[StrictFloat, StrictInt]] = None
    search_volume_history: Optional[AppendixInfo] = None
    google_ads: Optional[AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo] = None
    dataforseo_trends: Optional[AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo] = None
    naver: Optional[AppendixNaverKeywordsDataDataInfo] = None
    google: Optional[AppendixBingKeywordsDataLimitsRatesDataInfo] = None
    keyword_ideas_ads_api: Optional[AppendixSerpLimitsRatesDataInfo] = None
    __properties: ClassVar[List[str]] = ["keywords_for_keywords", "keywords_for_site", "search_volume", "ad_traffic_by_keywords", "languages", "locations", "tasks_ready", "explore", "categories", "errors", "bing", "keyword_performance", "locations_and_languages", "search_volume_history", "google_ads", "dataforseo_trends", "naver", "google", "keyword_ideas_ads_api"]

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
        """Create an instance of AppendixKeywordsDataDataInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of keywords_for_keywords
        if self.keywords_for_keywords:
            _dict['keywords_for_keywords'] = self.keywords_for_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_site
        if self.keywords_for_site:
            _dict['keywords_for_site'] = self.keywords_for_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_volume
        if self.search_volume:
            _dict['search_volume'] = self.search_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ad_traffic_by_keywords
        if self.ad_traffic_by_keywords:
            _dict['ad_traffic_by_keywords'] = self.ad_traffic_by_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of explore
        if self.explore:
            _dict['explore'] = self.explore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bing
        if self.bing:
            _dict['bing'] = self.bing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_performance
        if self.keyword_performance:
            _dict['keyword_performance'] = self.keyword_performance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_volume_history
        if self.search_volume_history:
            _dict['search_volume_history'] = self.search_volume_history.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google_ads
        if self.google_ads:
            _dict['google_ads'] = self.google_ads.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dataforseo_trends
        if self.dataforseo_trends:
            _dict['dataforseo_trends'] = self.dataforseo_trends.to_dict()
        # override the default output from pydantic by calling `to_dict()` of naver
        if self.naver:
            _dict['naver'] = self.naver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_ideas_ads_api
        if self.keyword_ideas_ads_api:
            _dict['keyword_ideas_ads_api'] = self.keyword_ideas_ads_api.to_dict()
        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if locations (nullable) is None
        # and model_fields_set contains the field
        if self.locations is None and "locations" in self.model_fields_set:
            _dict['locations'] = None

        # set to None if tasks_ready (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_ready is None and "tasks_ready" in self.model_fields_set:
            _dict['tasks_ready'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if locations_and_languages (nullable) is None
        # and model_fields_set contains the field
        if self.locations_and_languages is None and "locations_and_languages" in self.model_fields_set:
            _dict['locations_and_languages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixKeywordsDataDataInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords_for_keywords": AppendixInfo.from_dict(obj["keywords_for_keywords"]) if obj.get("keywords_for_keywords") is not None else None,
            "keywords_for_site": AppendixInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "search_volume": AppendixInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
            "ad_traffic_by_keywords": AppendixInfo.from_dict(obj["ad_traffic_by_keywords"]) if obj.get("ad_traffic_by_keywords") is not None else None,
            "languages": obj.get("languages"),
            "locations": obj.get("locations"),
            "tasks_ready": obj.get("tasks_ready"),
            "explore": AppendixInfo.from_dict(obj["explore"]) if obj.get("explore") is not None else None,
            "categories": obj.get("categories"),
            "errors": obj.get("errors"),
            "bing": AppendixBingKeywordsDataLimitsRatesDataInfo.from_dict(obj["bing"]) if obj.get("bing") is not None else None,
            "keyword_performance": AppendixInfo.from_dict(obj["keyword_performance"]) if obj.get("keyword_performance") is not None else None,
            "locations_and_languages": obj.get("locations_and_languages"),
            "search_volume_history": AppendixInfo.from_dict(obj["search_volume_history"]) if obj.get("search_volume_history") is not None else None,
            "google_ads": AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo.from_dict(obj["google_ads"]) if obj.get("google_ads") is not None else None,
            "dataforseo_trends": AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo.from_dict(obj["dataforseo_trends"]) if obj.get("dataforseo_trends") is not None else None,
            "naver": AppendixNaverKeywordsDataDataInfo.from_dict(obj["naver"]) if obj.get("naver") is not None else None,
            "google": AppendixBingKeywordsDataLimitsRatesDataInfo.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "keyword_ideas_ads_api": AppendixSerpLimitsRatesDataInfo.from_dict(obj["keyword_ideas_ads_api"]) if obj.get("keyword_ideas_ads_api") is not None else None
        })
        return _obj


