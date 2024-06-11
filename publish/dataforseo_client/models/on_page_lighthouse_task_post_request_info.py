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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OnPageLighthouseTaskPostRequestInfo(BaseModel):
    """
    OnPageLighthouseTaskPostRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="target URL required field target page should be specified with its absolute URL (including http:// or https://) example: https://dataforseo.com/")
    for_mobile: Optional[StrictBool] = Field(default=None, description="applies mobile emulation optional field if set to true, Lighthouse will use mobile device and screen emulation to test the page against mobile environment if set to false, the results will be provided for desktop default value: false")
    categories: Optional[List[StrictStr]] = Field(default=None, description="categories of Lighthouse audits optional field each category is a collection of audits and audit groups that applies weighting and scoring to the section (see official definition) if you ignore this field, we will return data for all categories unless you specify audits use this field to get data for specific categories you indicate here possible values: seo, pwa, performance, best_practices, accessibility")
    audits: Optional[List[StrictStr]] = Field(default=None, description="Lighthouse audits optional field audits are individual tests Lighthouse runs for each specific feature/optimization/metric to produce a numeric score (see official definition)   if you ignore this field, we will return data for all audits use this field to get data for specific audits you indicate here note that some audits do not belong to a specific category and are stand-alone page quality measurements in general, there can be several use cases: 1. if you ignore categories, you can use this field to get data for the specified audits only for example, if you ignore \"categories\" and specify \"audits\": [\"metrics/cumulative-layout-shift\",\"metrics/largest-contentful-paint\",\"metrics/total-blocking-time\"], you will get data only for these audits 2. if you specify a category, you can use this field to additionally receive audits that do not belong to the category(-ies) you specified for example, if you specify \"categories\": [\"seo\"] and \"audits\": [\"metrics/cumulative-layout-shift\",\"metrics/largest-contentful-paint\",\"metrics/total-blocking-time\"], you will get only these audits under “performance” and all audits under “seo” you can get the full list of possible audits here")
    version: Optional[StrictStr] = Field(default=None, description="lighthouse version optional field you can obtain the results specific to a certain Lighthouse version by specifying its number the list of available versions is available through the Lighthouse Versions endpoint")
    language_name: Optional[StrictStr] = Field(default=None, description="lighthouse language name optional field you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languages default value: English")
    language_code: Optional[StrictStr] = Field(default=None, description="lighthouse language code optional field you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languages default value: en")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id=$id http://your-server.com/pingscript?id=$id&tag=$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/postbackscript?id=$id http://your-server.com/postbackscript?id=$id&tag=$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23")
    __properties: ClassVar[List[str]] = ["url", "for_mobile", "categories", "audits", "version", "language_name", "language_code", "tag", "pingback_url", "postback_url"]

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
        """Create an instance of OnPageLighthouseTaskPostRequestInfo from a JSON string"""
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
        # set to None if for_mobile (nullable) is None
        # and model_fields_set contains the field
        if self.for_mobile is None and "for_mobile" in self.model_fields_set:
            _dict['for_mobile'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if audits (nullable) is None
        # and model_fields_set contains the field
        if self.audits is None and "audits" in self.model_fields_set:
            _dict['audits'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if pingback_url (nullable) is None
        # and model_fields_set contains the field
        if self.pingback_url is None and "pingback_url" in self.model_fields_set:
            _dict['pingback_url'] = None

        # set to None if postback_url (nullable) is None
        # and model_fields_set contains the field
        if self.postback_url is None and "postback_url" in self.model_fields_set:
            _dict['postback_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OnPageLighthouseTaskPostRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "for_mobile": obj.get("for_mobile"),
            "categories": obj.get("categories"),
            "audits": obj.get("audits"),
            "version": obj.get("version"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "tag": obj.get("tag"),
            "pingback_url": obj.get("pingback_url"),
            "postback_url": obj.get("postback_url")
        })
        return _obj

