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

class DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo
    """ # noqa: E501
    technology_paths: Optional[List[StrictStr]] = Field(default=None, description="target technology paths required field if you don’t specify groups, technologies and categories each technology path should be specified as a separate object containing “path” and “name”, where “path” is specified as “$group_id.$category_id” and “name” – as the name of the target technology; each object with a technology path should be separated with a comma you can find the full list of technology group ids, category ids and technology names on this page note: you can specify up to 10 technology paths in this array example: [{\"path\": \"content.cms\",\"name\": \"wordpress\"}, {\"path\": \"marketing.crm\",\"name\": \"salesforce\"}]")
    groups: Optional[List[StrictStr]] = Field(default=None, description="ids of the target technology groups required field if you don’t specify technologies, technology_paths or categories you can find the full list of technology group ids on this page note: you can specify up to 10 technology groups in this array example: [\"sales\", \"marketing\"]")
    categories: Optional[List[StrictStr]] = Field(default=None, description="ids of the target technology categories required field if you don’t specify groups, technology_paths or technologies you can find the full list of technology category ids on this page note: you can specify up to 10 technology categories in this array example: [\"payment_processors\",\"crm\"]")
    technologies: Optional[List[StrictStr]] = Field(default=None, description="target technologies required field if you don’t specify groups, technology_paths or categories you can find the full list of technologies you can specify here on this page note: you can specify up to 10 technologies in this array example: [\"Google Pay\",\"Salesforce\"]")
    keywords: Optional[List[StrictStr]] = Field(default=None, description="target keywords in the domain’s title, description or meta keywords optional field UTF-8 encoding each keyword should be at least 3 characters long example: [\"seo\",\"software\"]")
    mode: Optional[StrictStr] = Field(default=None, description="search mode optional field possible search mode types: as_is – search for results exactly matching the specified group ids, category ids, or technology names entry – search for results matching a part of the specified group ids, category ids, or technology names default value: as_is")
    filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: <, <=, >, >=, =, <>, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\"country_iso_code\",\"=\",\"US\"] [[\"country_iso_code\",\"=\",\"US\"], \"and\", [\"domain_rank\",\">\",100]] [[\"domain_rank\",\">\",100], \"and\", [[\"country_iso_code\",\"=\",\"US\"],\"or\",[\"country_iso_code\",\"=\",\"CA\"]]] for more information about filters, please refer to Domain Analytics Technologies API – Filters")
    order_by: Optional[List[StrictStr]] = Field(default=None, description="results sorting rules optional field available fields: domain_rank, domain, last_visited, country_iso_code, language_code, content_language_code possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\"last_visited,desc\"] default rule: [\"domain_rank,desc\"] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\"last_visited,desc\",\"domain_rank,desc\"]")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains optional field default value: 100 maximum value: 10000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains; Note: the maximum value is 9999, the sum of limit and offset must not exceed 10000; use the offset_token if you would like to offset more results")
    offset_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request")
    __properties: ClassVar[List[str]] = ["technology_paths", "groups", "categories", "technologies", "keywords", "mode", "filters", "order_by", "limit", "offset", "offset_token"]

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
        """Create an instance of DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo from a JSON string"""
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

        # set to None if order_by (nullable) is None
        # and model_fields_set contains the field
        if self.order_by is None and "order_by" in self.model_fields_set:
            _dict['order_by'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if offset_token (nullable) is None
        # and model_fields_set contains the field
        if self.offset_token is None and "offset_token" in self.model_fields_set:
            _dict['offset_token'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo from a dict"""
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
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token")
        })
        return _obj


