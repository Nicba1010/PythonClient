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

class BacklinksBulkNewLostReferringDomainsLiveItem(BaseModel):
    """
    BacklinksBulkNewLostReferringDomainsLiveItem
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain, subdomain or webpage from a POST array")
    new_referring_domains: Optional[StrictInt] = Field(default=None, description="number of new referring domains number of new referring domains pointing to the target")
    lost_referring_domains: Optional[StrictInt] = Field(default=None, description="number of lost referring domains number of lost referring domains of the target")
    new_referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of new referring main domains pointing to the target")
    lost_referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of lost referring main domains pointing to the target")
    __properties: ClassVar[List[str]] = ["target", "new_referring_domains", "lost_referring_domains", "new_referring_main_domains", "lost_referring_main_domains"]

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
        """Create an instance of BacklinksBulkNewLostReferringDomainsLiveItem from a JSON string"""
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
        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if new_referring_domains (nullable) is None
        # and model_fields_set contains the field
        if self.new_referring_domains is None and "new_referring_domains" in self.model_fields_set:
            _dict['new_referring_domains'] = None

        # set to None if lost_referring_domains (nullable) is None
        # and model_fields_set contains the field
        if self.lost_referring_domains is None and "lost_referring_domains" in self.model_fields_set:
            _dict['lost_referring_domains'] = None

        # set to None if new_referring_main_domains (nullable) is None
        # and model_fields_set contains the field
        if self.new_referring_main_domains is None and "new_referring_main_domains" in self.model_fields_set:
            _dict['new_referring_main_domains'] = None

        # set to None if lost_referring_main_domains (nullable) is None
        # and model_fields_set contains the field
        if self.lost_referring_main_domains is None and "lost_referring_main_domains" in self.model_fields_set:
            _dict['lost_referring_main_domains'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BacklinksBulkNewLostReferringDomainsLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "new_referring_domains": obj.get("new_referring_domains"),
            "lost_referring_domains": obj.get("lost_referring_domains"),
            "new_referring_main_domains": obj.get("new_referring_main_domains"),
            "lost_referring_main_domains": obj.get("lost_referring_main_domains")
        })
        return _obj

