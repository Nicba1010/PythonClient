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

from pydantic import Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_serp_element_item import BaseSerpElementItem
from typing import Optional, Set
from typing_extensions import Self

class SerpAutocompleteSerpElementItem(BaseSerpElementItem):
    """
    SerpAutocompleteSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    relevance: Optional[StrictInt] = Field(default=None, description="relevance of suggested keyword represents the relevant of the autocomplete suggestion to the target keyword can take values from 500 to 2000 the higher the value, the more relevant is the suggestion Note: only available for the following client: chrome/chrome-omni")
    suggestion: Optional[StrictStr] = Field(default=None, description="google autocomplete keyword suggestion")
    suggestion_type: Optional[StrictStr] = Field(default=None, description="google autocomplete suggestion type Note: only available for the following client: chrome/chrome-omni")
    search_query_url: Optional[StrictStr] = Field(default=None, description="url to search results url to search results relevant to the google autocomplete suggestion")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="url of the thumbnail image url of the thumbnail image of the google autocomplete suggestion Note: only available for the following client: gws-wiz gws-wiz-serp")
    highlighted: Optional[List[Optional[StrictStr]]] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "relevance", "suggestion", "suggestion_type", "search_query_url", "thumbnail_url", "highlighted"]

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
        """Create an instance of SerpAutocompleteSerpElementItem from a JSON string"""
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
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if relevance (nullable) is None
        # and model_fields_set contains the field
        if self.relevance is None and "relevance" in self.model_fields_set:
            _dict['relevance'] = None

        # set to None if suggestion (nullable) is None
        # and model_fields_set contains the field
        if self.suggestion is None and "suggestion" in self.model_fields_set:
            _dict['suggestion'] = None

        # set to None if suggestion_type (nullable) is None
        # and model_fields_set contains the field
        if self.suggestion_type is None and "suggestion_type" in self.model_fields_set:
            _dict['suggestion_type'] = None

        # set to None if search_query_url (nullable) is None
        # and model_fields_set contains the field
        if self.search_query_url is None and "search_query_url" in self.model_fields_set:
            _dict['search_query_url'] = None

        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnail_url'] = None

        # set to None if highlighted (nullable) is None
        # and model_fields_set contains the field
        if self.highlighted is None and "highlighted" in self.model_fields_set:
            _dict['highlighted'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpAutocompleteSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "relevance": obj.get("relevance"),
            "suggestion": obj.get("suggestion"),
            "suggestion_type": obj.get("suggestion_type"),
            "search_query_url": obj.get("search_query_url"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "highlighted": obj.get("highlighted")
        })
        return _obj


