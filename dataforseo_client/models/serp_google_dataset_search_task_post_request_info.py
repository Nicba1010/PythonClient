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

class SerpGoogleDatasetSearchTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleDatasetSearchTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword required field you can specify up to 700 symbols in the keyword field all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”; if you need to use the “+” symbol for your keyword, please specify it as “%2B”. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    priority: Optional[StrictInt] = Field(default=None, description="task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth optional field number of results in SERP default value: 20 max value: 700 Note: your account will be billed per each SERP containing up to 20 results; thus, setting a depth above 20 may result in additional charges if the search engine returns more than 20 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language optional field if you use this field, you don’t need to specify language_code possible value: English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code optional field possible value: en")
    device: Optional[StrictStr] = Field(default=None, description="device type optional field possible value: desktop")
    os: Optional[StrictStr] = Field(default=None, description="device operating system optional field possible values: windows, macos default value: windows")
    last_updated: Optional[StrictStr] = Field(default=None, description="last time the dataset was updated optional field possible values: 1m, 1y, 3y")
    file_formats: Optional[List[StrictStr]] = Field(default=None, description="file formats of the dataset optional field possible values: other, archive, text, image, document, tabular")
    usage_rights: Optional[StrictStr] = Field(default=None, description="usage rights of the dataset optional field possible values: commercial, noncommercial")
    is_free: Optional[StrictBool] = Field(default=None, description="indicates whether displayed datasets are free optional field possible values: true, false")
    topics: Optional[List[StrictStr]] = Field(default=None, description="dataset topics optional field possible values: humanities, social_sciences, life_sciences, agriculture, natural_sciences, geo, computer, architecture_and_urban_planning, engineering")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/postbackscript?id=$id http://your-server.com/postbackscript?id=$id&tag=$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server only value: advanced")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id=$id http://your-server.com/pingscript?id=$id&tag=$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center")
    __properties: ClassVar[List[str]] = ["keyword", "priority", "depth", "language_name", "language_code", "device", "os", "last_updated", "file_formats", "usage_rights", "is_free", "topics", "tag", "postback_url", "postback_data", "pingback_url"]

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
        """Create an instance of SerpGoogleDatasetSearchTaskPostRequestInfo from a JSON string"""
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
        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if depth (nullable) is None
        # and model_fields_set contains the field
        if self.depth is None and "depth" in self.model_fields_set:
            _dict['depth'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if device (nullable) is None
        # and model_fields_set contains the field
        if self.device is None and "device" in self.model_fields_set:
            _dict['device'] = None

        # set to None if os (nullable) is None
        # and model_fields_set contains the field
        if self.os is None and "os" in self.model_fields_set:
            _dict['os'] = None

        # set to None if last_updated (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated is None and "last_updated" in self.model_fields_set:
            _dict['last_updated'] = None

        # set to None if file_formats (nullable) is None
        # and model_fields_set contains the field
        if self.file_formats is None and "file_formats" in self.model_fields_set:
            _dict['file_formats'] = None

        # set to None if usage_rights (nullable) is None
        # and model_fields_set contains the field
        if self.usage_rights is None and "usage_rights" in self.model_fields_set:
            _dict['usage_rights'] = None

        # set to None if is_free (nullable) is None
        # and model_fields_set contains the field
        if self.is_free is None and "is_free" in self.model_fields_set:
            _dict['is_free'] = None

        # set to None if topics (nullable) is None
        # and model_fields_set contains the field
        if self.topics is None and "topics" in self.model_fields_set:
            _dict['topics'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if postback_url (nullable) is None
        # and model_fields_set contains the field
        if self.postback_url is None and "postback_url" in self.model_fields_set:
            _dict['postback_url'] = None

        # set to None if postback_data (nullable) is None
        # and model_fields_set contains the field
        if self.postback_data is None and "postback_data" in self.model_fields_set:
            _dict['postback_data'] = None

        # set to None if pingback_url (nullable) is None
        # and model_fields_set contains the field
        if self.pingback_url is None and "pingback_url" in self.model_fields_set:
            _dict['pingback_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpGoogleDatasetSearchTaskPostRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "priority": obj.get("priority"),
            "depth": obj.get("depth"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "last_updated": obj.get("last_updated"),
            "file_formats": obj.get("file_formats"),
            "usage_rights": obj.get("usage_rights"),
            "is_free": obj.get("is_free"),
            "topics": obj.get("topics"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url")
        })
        return _obj


