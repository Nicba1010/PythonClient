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
from dataforseo_client.models.appendix_business_listings_business_data_limits_rates_data_info import AppendixBusinessListingsBusinessDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_serp_limits_rates_data_info import AppendixSerpLimitsRatesDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixAppDataStatisticsRatesDataInfo(BaseModel):
    """
    AppendixAppDataStatisticsRatesDataInfo
    """ # noqa: E501
    app_info: Optional[AppendixSerpLimitsRatesDataInfo] = None
    app_list: Optional[AppendixSerpLimitsRatesDataInfo] = None
    app_reviews: Optional[AppendixSerpLimitsRatesDataInfo] = None
    app_searches: Optional[AppendixSerpLimitsRatesDataInfo] = None
    errors: Optional[Union[StrictFloat, StrictInt]] = None
    languages: Optional[Union[StrictFloat, StrictInt]] = None
    locations: Optional[Union[StrictFloat, StrictInt]] = None
    categories: Optional[Union[StrictFloat, StrictInt]] = None
    tasks_ready: Optional[Union[StrictFloat, StrictInt]] = None
    app_listings: Optional[AppendixBusinessListingsBusinessDataLimitsRatesDataInfo] = None
    id_list: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["app_info", "app_list", "app_reviews", "app_searches", "errors", "languages", "locations", "categories", "tasks_ready", "app_listings", "id_list"]

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
        """Create an instance of AppendixAppDataStatisticsRatesDataInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_info
        if self.app_info:
            _dict['app_info'] = self.app_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_list
        if self.app_list:
            _dict['app_list'] = self.app_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_reviews
        if self.app_reviews:
            _dict['app_reviews'] = self.app_reviews.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_searches
        if self.app_searches:
            _dict['app_searches'] = self.app_searches.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_listings
        if self.app_listings:
            _dict['app_listings'] = self.app_listings.to_dict()
        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if locations (nullable) is None
        # and model_fields_set contains the field
        if self.locations is None and "locations" in self.model_fields_set:
            _dict['locations'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if tasks_ready (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_ready is None and "tasks_ready" in self.model_fields_set:
            _dict['tasks_ready'] = None

        # set to None if id_list (nullable) is None
        # and model_fields_set contains the field
        if self.id_list is None and "id_list" in self.model_fields_set:
            _dict['id_list'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixAppDataStatisticsRatesDataInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_info": AppendixSerpLimitsRatesDataInfo.from_dict(obj["app_info"]) if obj.get("app_info") is not None else None,
            "app_list": AppendixSerpLimitsRatesDataInfo.from_dict(obj["app_list"]) if obj.get("app_list") is not None else None,
            "app_reviews": AppendixSerpLimitsRatesDataInfo.from_dict(obj["app_reviews"]) if obj.get("app_reviews") is not None else None,
            "app_searches": AppendixSerpLimitsRatesDataInfo.from_dict(obj["app_searches"]) if obj.get("app_searches") is not None else None,
            "errors": obj.get("errors"),
            "languages": obj.get("languages"),
            "locations": obj.get("locations"),
            "categories": obj.get("categories"),
            "tasks_ready": obj.get("tasks_ready"),
            "app_listings": AppendixBusinessListingsBusinessDataLimitsRatesDataInfo.from_dict(obj["app_listings"]) if obj.get("app_listings") is not None else None,
            "id_list": obj.get("id_list")
        })
        return _obj

