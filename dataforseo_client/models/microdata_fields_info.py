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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.message_info import MessageInfo
from typing import Optional, Set
from typing_extensions import Self

class MicrodataFieldsInfo(BaseModel):
    """
    MicrodataFieldsInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="field name name of the data field")
    types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="list of microdata types")
    value: Optional[StrictStr] = Field(default=None, description="microdata value microdata value specified on a target web page")
    test_results: Optional[List[MessageInfo]] = Field(default=None, description="list of microdata types")
    fields: Optional[List[MicrodataFieldsInfo]] = Field(default=None, description="microdata fields an array of objects containing data fields related to the certain microdata type")
    __properties: ClassVar[List[str]] = ["name", "types", "value", "test_results", "fields"]

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
        """Create an instance of MicrodataFieldsInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in test_results (list)
        _items = []
        if self.test_results:
            for _item in self.test_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['test_results'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if test_results (nullable) is None
        # and model_fields_set contains the field
        if self.test_results is None and "test_results" in self.model_fields_set:
            _dict['test_results'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MicrodataFieldsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "types": obj.get("types"),
            "value": obj.get("value"),
            "test_results": [MessageInfo.from_dict(_item) for _item in obj["test_results"]] if obj.get("test_results") is not None else None,
            "fields": [MicrodataFieldsInfo.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
MicrodataFieldsInfo.model_rebuild(raise_errors=False)

