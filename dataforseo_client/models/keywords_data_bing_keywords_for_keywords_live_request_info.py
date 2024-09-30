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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataBingKeywordsForKeywordsLiveRequestInfo(BaseModel):
    """
    KeywordsDataBingKeywordsForKeywordsLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[StrictStr]] = Field(default=None, description="keywords required field you can specify the maximum of 200 keywords with each keyword containing no more than 100 characters; the specified keywords will be converted to lowercase, data will be provided in a separate array learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the data will be provided for the country the specified coordinates belong to example: 52.6178549,-155.352142")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code supported languages: English, French, German")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name supported languages: en, fr, de")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters optional field Use these parameters to sort the results by search_volume, cpc, competition or relevance in the descending order default value: relevance")
    keywords_negative: Optional[List[StrictStr]] = Field(default=None, description="keywords negative array optional field These keywords will be ignored in the results array; You can specify a maximum of 200 terms that you want to exclude from the results; the specified keywords will be converted to lowercase format")
    device: Optional[StrictStr] = Field(default=None, description="device type optional field specify this field if you want to get the data for a particular device type; possible values: all, mobile, desktop, tablet default value: all")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range optional field you can specify a date from the past 24 months if you don’t specify this field, data will be provided for the last 12 months date format: \"yyyy-mm-dd\" example: \"2020-01-01\" Note: we do not recommend using a custom time range for the past year’s dates")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range optional field if you don’t specify this field, data will be provided for the last 12 months; minimum value: two years back from today’s date; maximum value: one month from today’s date; date format: \"yyyy-mm-dd\" example: \"2020-03-15\" Note: we do not recommend using a custom time range for the past year’s dates")
    search_partners: Optional[StrictBool] = Field(default=None, description="Bing search partners type optional field if you specify true, the results will be delivered for owned, operated, and syndicated networks across Bing, Yahoo, AOL and partner sites that host Bing, AOL, and Yahoo search. default value: false – results are returned for Bing, AOL, and Yahoo search networks")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["keywords", "location_name", "location_code", "location_coordinate", "language_name", "language_code", "sort_by", "keywords_negative", "device", "date_from", "date_to", "search_partners", "tag"]

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
        """Create an instance of KeywordsDataBingKeywordsForKeywordsLiveRequestInfo from a JSON string"""
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
        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if location_coordinate (nullable) is None
        # and model_fields_set contains the field
        if self.location_coordinate is None and "location_coordinate" in self.model_fields_set:
            _dict['location_coordinate'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['sort_by'] = None

        # set to None if keywords_negative (nullable) is None
        # and model_fields_set contains the field
        if self.keywords_negative is None and "keywords_negative" in self.model_fields_set:
            _dict['keywords_negative'] = None

        # set to None if device (nullable) is None
        # and model_fields_set contains the field
        if self.device is None and "device" in self.model_fields_set:
            _dict['device'] = None

        # set to None if date_from (nullable) is None
        # and model_fields_set contains the field
        if self.date_from is None and "date_from" in self.model_fields_set:
            _dict['date_from'] = None

        # set to None if date_to (nullable) is None
        # and model_fields_set contains the field
        if self.date_to is None and "date_to" in self.model_fields_set:
            _dict['date_to'] = None

        # set to None if search_partners (nullable) is None
        # and model_fields_set contains the field
        if self.search_partners is None and "search_partners" in self.model_fields_set:
            _dict['search_partners'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataBingKeywordsForKeywordsLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords": obj.get("keywords"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "sort_by": obj.get("sort_by"),
            "keywords_negative": obj.get("keywords_negative"),
            "device": obj.get("device"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "search_partners": obj.get("search_partners"),
            "tag": obj.get("tag")
        })
        return _obj


