# coding: utf-8

# flake8: noqa
"""
    Royal Mail API Shipping V2 (REST)

    This API specification details the requirements for integrating with Royal Mail API Shipping V2 (REST). It specifically covers how the Royal Mail API Shipping V2 (REST) can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.  Royal Mail API Shipping V2 (REST) exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail. Built on industry standards, Royal Mail API Shipping V2 (REST) provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels.  There are no costs to customers for using the Royal Mail API Shipping V2 (REST) services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.  This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating cancelling a shipment and manifesting click here&#58; www.royalmail.com/pro-shipping-help  # noqa: E501

    OpenAPI spec version: 1.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from rmail_api.models.address import Address
from rmail_api.models.cancel_or_update_shipment_response import CancelOrUpdateShipmentResponse
from rmail_api.models.completed_shipments import CompletedShipments
from rmail_api.models.contact import Contact
from rmail_api.models.content_detail import ContentDetail
from rmail_api.models.created_shipment_response import CreatedShipmentResponse
from rmail_api.models.documents_request import DocumentsRequest
from rmail_api.models.error import Error
from rmail_api.models.error_response import ErrorResponse
from rmail_api.models.errors import Errors
from rmail_api.models.label_images import LabelImages
from rmail_api.models.label_response import LabelResponse
from rmail_api.models.manifest_request import ManifestRequest
from rmail_api.models.manifest_response import ManifestResponse
from rmail_api.models.manifest_shipment import ManifestShipment
from rmail_api.models.manifest_shipments import ManifestShipments
from rmail_api.models.measurement import Measurement
from rmail_api.models.offline_shipment import OfflineShipment
from rmail_api.models.parcel import Parcel
from rmail_api.models.print_manifest_response import PrintManifestResponse
from rmail_api.models.recipient_address import RecipientAddress
from rmail_api.models.recipient_contact import RecipientContact
from rmail_api.models.service import Service
from rmail_api.models.service_enhancements import ServiceEnhancements
from rmail_api.models.shipment import Shipment
from rmail_api.models.shipment_barcode_item import ShipmentBarcodeItem
from rmail_api.models.shipment_barcode_items import ShipmentBarcodeItems
from rmail_api.models.shipment_request_item import ShipmentRequestItem
from rmail_api.models.shipment_request_item_international import ShipmentRequestItemInternational
from rmail_api.models.shipment_with_barcode_and_weight import ShipmentWithBarcodeAndWeight
from rmail_api.models.shipments_request import ShipmentsRequest
from rmail_api.models.token import Token
