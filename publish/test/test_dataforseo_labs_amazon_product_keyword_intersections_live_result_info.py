# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.dataforseo_labs_amazon_product_keyword_intersections_live_result_info import DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo

class TestDataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo(unittest.TestCase):
    """DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo:
        """Test DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo`
        """
        model = DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo()
        if include_optional:
            return DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo(
                se_type = '',
                asins = {
                    'key' : ''
                    },
                location_code = 56,
                language_code = '',
                total_count = 56,
                items_count = 56,
                items = [
                    dataforseo_client.models.dataforseo_labs_amazon_product_keyword_intersections_live_item.DataforseoLabsAmazonProductKeywordIntersectionsLiveItem(
                        se_type = '', 
                        keyword_data = dataforseo_client.models.amazon_keyword_data.AmazonKeywordData(
                            se_type = '', 
                            keyword = '', 
                            location_code = 56, 
                            language_code = '', 
                            keyword_info = dataforseo_client.models.amazon_keyword_info.AmazonKeywordInfo(
                                se_type = '', 
                                last_updated_time = '', 
                                search_volume = 56, ), ), 
                        intersection_result = {
                            'key' : dataforseo_client.models.base_amazon_serp_element_item.BaseAmazonSerpElementItem()
                            }, )
                    ]
            )
        else:
            return DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo(
        )
        """

    def testDataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo(self):
        """Test DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()