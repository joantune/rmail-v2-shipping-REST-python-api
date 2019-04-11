# coding: utf-8

"""
    Royal Mail API Shipping V2 (REST)

    This API specification details the requirements for integrating with Royal Mail API Shipping V2 (REST). It specifically covers how the Royal Mail API Shipping V2 (REST) can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.  Royal Mail API Shipping V2 (REST) exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail. Built on industry standards, Royal Mail API Shipping V2 (REST) provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels.  There are no costs to customers for using the Royal Mail API Shipping V2 (REST) services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.  This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating cancelling a shipment and manifesting click here&#58; www.royalmail.com/pro-shipping-help  # noqa: E501

    OpenAPI spec version: 1.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import rmail_api
from models.print_manifest_response import PrintManifestResponse  # noqa: E501
from rmail_api.rest import ApiException


class TestPrintManifestResponse(unittest.TestCase):
    """PrintManifestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrintManifestResponse(self):
        """Test PrintManifestResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = rmail_api.models.print_manifest_response.PrintManifestResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
