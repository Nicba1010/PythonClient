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
from dataforseo_client.models.base_business_data_serp_element_item import BaseBusinessDataSerpElementItem
from dataforseo_client.models.link_element import LinkElement
from typing import Optional, Set
from typing_extensions import Self

class GoogleBusinessPostBusinessDataSerpElementItem(BaseBusinessDataSerpElementItem):
    """
    GoogleBusinessPostBusinessDataSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed updates absolute position among all present elements")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    author: Optional[StrictStr] = Field(default=None, description="author of the post")
    snippet: Optional[StrictStr] = Field(default=None, description="additional content of a post")
    post_text: Optional[StrictStr] = Field(default=None, description="main content of a post")
    url: Optional[StrictStr] = Field(default=None, description="url of a post")
    images_url: Optional[StrictStr] = Field(default=None, description="url of an image included in the post")
    post_date: Optional[StrictStr] = Field(default=None, description="date when a post was published in the following format: \"mm/dd/yyyy hh:mm:ss\"")
    timestamp: Optional[StrictStr] = Field(default=None, description="time when a post was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    links: Optional[List[LinkElement]] = Field(default=None, description="links included in the post")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "author", "snippet", "post_text", "url", "images_url", "post_date", "timestamp", "links"]

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
        """Create an instance of GoogleBusinessPostBusinessDataSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
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

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if author (nullable) is None
        # and model_fields_set contains the field
        if self.author is None and "author" in self.model_fields_set:
            _dict['author'] = None

        # set to None if snippet (nullable) is None
        # and model_fields_set contains the field
        if self.snippet is None and "snippet" in self.model_fields_set:
            _dict['snippet'] = None

        # set to None if post_text (nullable) is None
        # and model_fields_set contains the field
        if self.post_text is None and "post_text" in self.model_fields_set:
            _dict['post_text'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if images_url (nullable) is None
        # and model_fields_set contains the field
        if self.images_url is None and "images_url" in self.model_fields_set:
            _dict['images_url'] = None

        # set to None if post_date (nullable) is None
        # and model_fields_set contains the field
        if self.post_date is None and "post_date" in self.model_fields_set:
            _dict['post_date'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleBusinessPostBusinessDataSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "author": obj.get("author"),
            "snippet": obj.get("snippet"),
            "post_text": obj.get("post_text"),
            "url": obj.get("url"),
            "images_url": obj.get("images_url"),
            "post_date": obj.get("post_date"),
            "timestamp": obj.get("timestamp"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj

