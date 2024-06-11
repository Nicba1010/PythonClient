# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.stocks_box_dataforseo_labs_serp_element_item import StocksBoxDataforseoLabsSerpElementItem

class TestStocksBoxDataforseoLabsSerpElementItem(unittest.TestCase):
    """StocksBoxDataforseoLabsSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StocksBoxDataforseoLabsSerpElementItem:
        """Test StocksBoxDataforseoLabsSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StocksBoxDataforseoLabsSerpElementItem`
        """
        model = StocksBoxDataforseoLabsSerpElementItem()
        if include_optional:
            return StocksBoxDataforseoLabsSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                title = '',
                source = '',
                snippet = '',
                price = dataforseo_client.models.price_info.PriceInfo(
                    current = 1.337, 
                    regular = 1.337, 
                    max_value = 1.337, 
                    currency = '', 
                    is_price_range = True, 
                    displayed_price = '', ),
                url = '',
                domain = '',
                table = dataforseo_client.models.table.Table(
                    table_element = '', 
                    table_header = [
                        ''
                        ], 
                    table_content = [
                        [
                            ''
                            ]
                        ], ),
                graph = dataforseo_client.models.graph.Graph(
                    items = [
                        dataforseo_client.models.graph_element.GraphElement(
                            type = '', 
                            date = '', 
                            value = 56, )
                        ], 
                    previous_items = [
                        dataforseo_client.models.graph_element.GraphElement(
                            type = '', 
                            date = '', 
                            value = 56, )
                        ], )
            )
        else:
            return StocksBoxDataforseoLabsSerpElementItem(
        )
        """

    def testStocksBoxDataforseoLabsSerpElementItem(self):
        """Test StocksBoxDataforseoLabsSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()