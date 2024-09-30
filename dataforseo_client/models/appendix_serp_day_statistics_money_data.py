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
from dataforseo_client.models.appendix_function_type_info import AppendixFunctionTypeInfo
from dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info import AppendixJobsSerpLimitsRatesDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixSerpDayStatisticsMoneyData(BaseModel):
    """
    AppendixSerpDayStatisticsMoneyData
    """ # noqa: E501
    task_post: Optional[Union[StrictFloat, StrictInt]] = None
    task_get: Optional[AppendixFunctionTypeInfo] = None
    tasks_ready: Optional[Union[StrictFloat, StrictInt]] = None
    locations: Optional[Union[StrictFloat, StrictInt]] = None
    languages: Optional[Union[StrictFloat, StrictInt]] = None
    live: Optional[AppendixFunctionTypeInfo] = None
    errors: Optional[Union[StrictFloat, StrictInt]] = None
    tasks_fixed: Optional[Union[StrictFloat, StrictInt]] = None
    jobs: Optional[AppendixJobsSerpLimitsRatesDataInfo] = None
    screenshot: Optional[Union[StrictFloat, StrictInt]] = None
    refund_money: Optional[Union[StrictFloat, StrictInt]] = None
    ai_summary: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["task_post", "task_get", "tasks_ready", "locations", "languages", "live", "errors", "tasks_fixed", "jobs", "screenshot", "refund_money", "ai_summary"]

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
        """Create an instance of AppendixSerpDayStatisticsMoneyData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of task_get
        if self.task_get:
            _dict['task_get'] = self.task_get.to_dict()
        # override the default output from pydantic by calling `to_dict()` of live
        if self.live:
            _dict['live'] = self.live.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jobs
        if self.jobs:
            _dict['jobs'] = self.jobs.to_dict()
        # set to None if task_post (nullable) is None
        # and model_fields_set contains the field
        if self.task_post is None and "task_post" in self.model_fields_set:
            _dict['task_post'] = None

        # set to None if tasks_ready (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_ready is None and "tasks_ready" in self.model_fields_set:
            _dict['tasks_ready'] = None

        # set to None if locations (nullable) is None
        # and model_fields_set contains the field
        if self.locations is None and "locations" in self.model_fields_set:
            _dict['locations'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if tasks_fixed (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_fixed is None and "tasks_fixed" in self.model_fields_set:
            _dict['tasks_fixed'] = None

        # set to None if screenshot (nullable) is None
        # and model_fields_set contains the field
        if self.screenshot is None and "screenshot" in self.model_fields_set:
            _dict['screenshot'] = None

        # set to None if refund_money (nullable) is None
        # and model_fields_set contains the field
        if self.refund_money is None and "refund_money" in self.model_fields_set:
            _dict['refund_money'] = None

        # set to None if ai_summary (nullable) is None
        # and model_fields_set contains the field
        if self.ai_summary is None and "ai_summary" in self.model_fields_set:
            _dict['ai_summary'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixSerpDayStatisticsMoneyData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_post": obj.get("task_post"),
            "task_get": AppendixFunctionTypeInfo.from_dict(obj["task_get"]) if obj.get("task_get") is not None else None,
            "tasks_ready": obj.get("tasks_ready"),
            "locations": obj.get("locations"),
            "languages": obj.get("languages"),
            "live": AppendixFunctionTypeInfo.from_dict(obj["live"]) if obj.get("live") is not None else None,
            "errors": obj.get("errors"),
            "tasks_fixed": obj.get("tasks_fixed"),
            "jobs": AppendixJobsSerpLimitsRatesDataInfo.from_dict(obj["jobs"]) if obj.get("jobs") is not None else None,
            "screenshot": obj.get("screenshot"),
            "refund_money": obj.get("refund_money"),
            "ai_summary": obj.get("ai_summary")
        })
        return _obj


