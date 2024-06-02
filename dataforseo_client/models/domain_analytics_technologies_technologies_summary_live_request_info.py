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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo
    """ # noqa: E501
    technology_paths: Optional[List[StrictStr]] = Field(default=None, description="target technology paths required field if you don’t specify groups, technologies and categories each technology path should be specified as a separate object containing “path” and “name”, where “path” is specified as “$group_id.$category_id” and “name” – as the name of the target technology; each object with a technology path should be separated with a comma you can find the full list of technology group ids, category ids and technology names on this page note: you can specify up to 10 technology paths in this array example: [{\"path\": \"content.cms\",\"name\": \"wordpress\"}, {\"path\": \"marketing.crm\",\"name\": \"salesforce\"}]")
    groups: Optional[List[StrictStr]] = Field(default=None, description="ids of the target technology groups required field if you don’t specify technologies, technology_paths or categories you can find the full list of technology group ids on this page note: you can specify up to 10 technology groups in this array example: [\"sales\", \"marketing\"]")
    categories: Optional[List[StrictStr]] = Field(default=None, description="ids of the target technology categories required field if you don’t specify groups, technology_paths or technologies you can find the full list of technology category ids on this page note: you can specify up to 10 technology categories in this array example: [\"payment_processors\",\"crm\"]")
    technologies: Optional[List[StrictStr]] = Field(default=None, description="target technologies required field if you don’t specify groups, technology_paths or categories you can find the full list of technologies you can specify here on this page note: you can specify up to 10 technologies in this array example: [\"Google Pay\",\"Salesforce\"]")
    keywords: Optional[List[StrictStr]] = Field(default=None, description="target keywords in the domain’s title, description or meta keywords optional field UTF-8 encoding each keyword should be at least 3 characters long example: [\"seo\",\"software\"]")
    mode: Optional[StrictStr] = Field(default=None, description="search mode optional field possible search mode types: as_is – search for results exactly matching the specified group ids, category ids, or technology names entry – search for results matching a part of the specified group ids, category ids, or technology names default value: as_is")
    filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: <, <=, >, >=, =, <>, in, not_in, like,not_like you can use the % operator with like and not_like to match any string of zero or more characters you can use the following parameters to filter the results: domain_rank, last_visited, country_iso_code, language_code, content_language_code example: [[\"country_iso_code\",\"=\",\"US\"], \"and\", [\"domain_rank\",\">\",800]] for more information about filters, please refer to Domain Analytics Technologies API – Filters")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: countries, languages, content_languages, keywords default value: 10 maximum value: 10000")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["technology_paths", "groups", "categories", "technologies", "keywords", "mode", "filters", "internal_list_limit", "tag"]

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
        """Create an instance of DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo from a JSON string"""
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
        # set to None if technology_paths (nullable) is None
        # and model_fields_set contains the field
        if self.technology_paths is None and "technology_paths" in self.model_fields_set:
            _dict['technology_paths'] = None

        # set to None if groups (nullable) is None
        # and model_fields_set contains the field
        if self.groups is None and "groups" in self.model_fields_set:
            _dict['groups'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if technologies (nullable) is None
        # and model_fields_set contains the field
        if self.technologies is None and "technologies" in self.model_fields_set:
            _dict['technologies'] = None

        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict['keywords'] = None

        # set to None if mode (nullable) is None
        # and model_fields_set contains the field
        if self.mode is None and "mode" in self.model_fields_set:
            _dict['mode'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if internal_list_limit (nullable) is None
        # and model_fields_set contains the field
        if self.internal_list_limit is None and "internal_list_limit" in self.model_fields_set:
            _dict['internal_list_limit'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "technology_paths": obj.get("technology_paths"),
            "groups": obj.get("groups"),
            "categories": obj.get("categories"),
            "technologies": obj.get("technologies"),
            "keywords": obj.get("keywords"),
            "mode": obj.get("mode"),
            "filters": obj.get("filters"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "tag": obj.get("tag")
        })
        return _obj


