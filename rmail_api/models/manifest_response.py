# coding: utf-8

"""
    Royal Mail API Shipping V2 (REST)

    This API specification details the requirements for integrating with Royal Mail API Shipping V2 (REST). It specifically covers how the Royal Mail API Shipping V2 (REST) can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.  Royal Mail API Shipping V2 (REST) exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail. Built on industry standards, Royal Mail API Shipping V2 (REST) provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels.  There are no costs to customers for using the Royal Mail API Shipping V2 (REST) services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.  This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating cancelling a shipment and manifesting click here&#58; www.royalmail.com/pro-shipping-help  # noqa: E501

    OpenAPI spec version: 1.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from rmail_api.models.manifest_shipments import ManifestShipments  # noqa: F401,E501


class ManifestResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'batch_number': 'int',
        'count': 'int',
        'manifest': 'str',
        'shipments': 'ManifestShipments'
    }

    attribute_map = {
        'batch_number': 'batchNumber',
        'count': 'count',
        'manifest': 'manifest',
        'shipments': 'shipments'
    }

    def __init__(self, batch_number=None, count=None, manifest=None, shipments=None):  # noqa: E501
        """ManifestResponse - a model defined in Swagger"""  # noqa: E501
        self._batch_number = None
        self._count = None
        self._manifest = None
        self._shipments = None
        self.discriminator = None
        if batch_number is not None:
            self.batch_number = batch_number
        if count is not None:
            self.count = count
        if manifest is not None:
            self.manifest = manifest
        if shipments is not None:
            self.shipments = shipments

    @property
    def batch_number(self):
        """Gets the batch_number of this ManifestResponse.  # noqa: E501

        The batch number of the manifest. It is a sequentially allocated number. Used in subsequent call to the create manifest label operation.  # noqa: E501

        :return: The batch_number of this ManifestResponse.  # noqa: E501
        :rtype: int
        """
        return self._batch_number

    @batch_number.setter
    def batch_number(self, batch_number):
        """Sets the batch_number of this ManifestResponse.

        The batch number of the manifest. It is a sequentially allocated number. Used in subsequent call to the create manifest label operation.  # noqa: E501

        :param batch_number: The batch_number of this ManifestResponse.  # noqa: E501
        :type: int
        """

        self._batch_number = batch_number

    @property
    def count(self):
        """Gets the count of this ManifestResponse.  # noqa: E501

        Total number of shipments on this manifest  # noqa: E501

        :return: The count of this ManifestResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ManifestResponse.

        Total number of shipments on this manifest  # noqa: E501

        :param count: The count of this ManifestResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def manifest(self):
        """Gets the manifest of this ManifestResponse.  # noqa: E501

        Customer Collection Receipt in PDF format - Base64 encoded for transfer. Returned here when 'Include the Manifest Image in 'createManifest' response' is enabled in Pro Shipping GUI.  # noqa: E501

        :return: The manifest of this ManifestResponse.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this ManifestResponse.

        Customer Collection Receipt in PDF format - Base64 encoded for transfer. Returned here when 'Include the Manifest Image in 'createManifest' response' is enabled in Pro Shipping GUI.  # noqa: E501

        :param manifest: The manifest of this ManifestResponse.  # noqa: E501
        :type: str
        """

        self._manifest = manifest

    @property
    def shipments(self):
        """Gets the shipments of this ManifestResponse.  # noqa: E501


        :return: The shipments of this ManifestResponse.  # noqa: E501
        :rtype: ManifestShipments
        """
        return self._shipments

    @shipments.setter
    def shipments(self, shipments):
        """Sets the shipments of this ManifestResponse.


        :param shipments: The shipments of this ManifestResponse.  # noqa: E501
        :type: ManifestShipments
        """

        self._shipments = shipments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ManifestResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ManifestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
