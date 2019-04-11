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


class LabelImages(object):
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
        'image1_d_barcode': 'str',
        'image2_d_matrix': 'str'
    }

    attribute_map = {
        'image1_d_barcode': 'image1DBarcode',
        'image2_d_matrix': 'image2DMatrix'
    }

    def __init__(self, image1_d_barcode=None, image2_d_matrix=None):  # noqa: E501
        """LabelImages - a model defined in Swagger"""  # noqa: E501
        self._image1_d_barcode = None
        self._image2_d_matrix = None
        self.discriminator = None
        if image1_d_barcode is not None:
            self.image1_d_barcode = image1_d_barcode
        if image2_d_matrix is not None:
            self.image2_d_matrix = image2_d_matrix

    @property
    def image1_d_barcode(self):
        """Gets the image1_d_barcode of this LabelImages.  # noqa: E501


        :return: The image1_d_barcode of this LabelImages.  # noqa: E501
        :rtype: str
        """
        return self._image1_d_barcode

    @image1_d_barcode.setter
    def image1_d_barcode(self, image1_d_barcode):
        """Sets the image1_d_barcode of this LabelImages.


        :param image1_d_barcode: The image1_d_barcode of this LabelImages.  # noqa: E501
        :type: str
        """

        self._image1_d_barcode = image1_d_barcode

    @property
    def image2_d_matrix(self):
        """Gets the image2_d_matrix of this LabelImages.  # noqa: E501


        :return: The image2_d_matrix of this LabelImages.  # noqa: E501
        :rtype: str
        """
        return self._image2_d_matrix

    @image2_d_matrix.setter
    def image2_d_matrix(self, image2_d_matrix):
        """Sets the image2_d_matrix of this LabelImages.


        :param image2_d_matrix: The image2_d_matrix of this LabelImages.  # noqa: E501
        :type: str
        """

        self._image2_d_matrix = image2_d_matrix

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
        if issubclass(LabelImages, dict):
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
        if not isinstance(other, LabelImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
