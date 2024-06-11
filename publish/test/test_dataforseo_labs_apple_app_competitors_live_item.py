# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.dataforseo_labs_apple_app_competitors_live_item import DataforseoLabsAppleAppCompetitorsLiveItem

class TestDataforseoLabsAppleAppCompetitorsLiveItem(unittest.TestCase):
    """DataforseoLabsAppleAppCompetitorsLiveItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataforseoLabsAppleAppCompetitorsLiveItem:
        """Test DataforseoLabsAppleAppCompetitorsLiveItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataforseoLabsAppleAppCompetitorsLiveItem`
        """
        model = DataforseoLabsAppleAppCompetitorsLiveItem()
        if include_optional:
            return DataforseoLabsAppleAppCompetitorsLiveItem(
                se_type = '',
                app_id = '',
                avg_position = 1.337,
                sum_position = 56,
                intersections = 56,
                competitor_metrics = dataforseo_client.models.app_store_metrics_bundle_info.AppStoreMetricsBundleInfo(
                    app_store_search_organic = dataforseo_client.models.app_metrics_info.AppMetricsInfo(
                        pos_1 = 56, 
                        pos_2_3 = 56, 
                        pos_4_10 = 56, 
                        pos_11_100 = 56, 
                        count = 56, 
                        search_volume = 56, ), ),
                full_metrics = dataforseo_client.models.app_store_metrics_bundle_info.AppStoreMetricsBundleInfo(
                    app_store_search_organic = dataforseo_client.models.app_metrics_info.AppMetricsInfo(
                        pos_1 = 56, 
                        pos_2_3 = 56, 
                        pos_4_10 = 56, 
                        pos_11_100 = 56, 
                        count = 56, 
                        search_volume = 56, ), )
            )
        else:
            return DataforseoLabsAppleAppCompetitorsLiveItem(
        )
        """

    def testDataforseoLabsAppleAppCompetitorsLiveItem(self):
        """Test DataforseoLabsAppleAppCompetitorsLiveItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()