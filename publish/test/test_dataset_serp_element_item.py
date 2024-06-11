# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.dataset_serp_element_item import DatasetSerpElementItem

class TestDatasetSerpElementItem(unittest.TestCase):
    """DatasetSerpElementItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetSerpElementItem:
        """Test DatasetSerpElementItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetSerpElementItem`
        """
        model = DatasetSerpElementItem()
        if include_optional:
            return DatasetSerpElementItem(
                rank_group = 56,
                rank_absolute = 56,
                position = '',
                xpath = '',
                dataset_id = '',
                title = '',
                image_url = '',
                scholarly_citations_count = 56,
                scholarly_articles_url = '',
                unique_identifier = '',
                related_article = '',
                links = [
                    dataforseo_client.models.link_element.LinkElement(
                        type = '', 
                        title = '', 
                        snippet = '', 
                        description = '', 
                        url = '', 
                        domain = '', 
                        xpath = '', )
                    ],
                dataset_providers = [
                    dataforseo_client.models.licenses_element.LicensesElement(
                        type = '', 
                        title = '', 
                        url = '', 
                        domain = '', )
                    ],
                formats = [
                    dataforseo_client.models.formats_element.FormatsElement(
                        type = '', 
                        format = '', 
                        size = '', )
                    ],
                authors = [
                    dataforseo_client.models.authors_element.AuthorsElement(
                        type = '', 
                        name = '', 
                        url = '', 
                        domain = '', )
                    ],
                licenses = [
                    dataforseo_client.models.licenses_element.LicensesElement(
                        type = '', 
                        title = '', 
                        url = '', 
                        domain = '', )
                    ],
                updated_date = '',
                area_covered = [
                    ''
                    ],
                period_covered = dataforseo_client.models.period_covered.PeriodCovered(
                    start_date = '', 
                    end_date = '', 
                    displayed_date = '', ),
                dataset_description = dataforseo_client.models.dataset_description.DatasetDescription(
                    text = '', 
                    links = [
                        dataforseo_client.models.link_element.LinkElement(
                            type = '', 
                            title = '', 
                            snippet = '', 
                            description = '', 
                            url = '', 
                            domain = '', 
                            xpath = '', )
                        ], )
            )
        else:
            return DatasetSerpElementItem(
        )
        """

    def testDatasetSerpElementItem(self):
        """Test DatasetSerpElementItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()