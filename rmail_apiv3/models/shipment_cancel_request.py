# coding: utf-8

"""
    Royal Mail API Shipping V3 (REST)

    This API specification details the requirements for integrating with **Royal Mail API Shipping V3**.<br><br>It specifically covers how the Royal Mail API Shipping V3 can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.<br><br>Royal Mail API Shipping V3 exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail.<br><br>Built on industry standards, Royal Mail API Shipping V3 provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels. There are no costs to customers for using the Royal Mail API Shipping V3 services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.<br><br>This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating/ cancelling a shipment and Manifesting please refer to http://www.royalmail.com/pro-shipping-help.  # noqa: E501

    OpenAPI spec version: 3.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ShipmentCancelRequest(object):
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
        'shipment_id': 'str',
        'reason_for_cancellation': 'str'
    }

    attribute_map = {
        'shipment_id': 'ShipmentId',
        'reason_for_cancellation': 'ReasonForCancellation'
    }

    def __init__(self, shipment_id=None, reason_for_cancellation=None):  # noqa: E501
        """ShipmentCancelRequest - a model defined in Swagger"""  # noqa: E501
        self._shipment_id = None
        self._reason_for_cancellation = None
        self.discriminator = None
        self.shipment_id = shipment_id
        self.reason_for_cancellation = reason_for_cancellation

    @property
    def shipment_id(self):
        """Gets the shipment_id of this ShipmentCancelRequest.  # noqa: E501

        Shipment Id<br />The tracking number or Unique Id of the shipment to cancel.  # noqa: E501

        :return: The shipment_id of this ShipmentCancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this ShipmentCancelRequest.

        Shipment Id<br />The tracking number or Unique Id of the shipment to cancel.  # noqa: E501

        :param shipment_id: The shipment_id of this ShipmentCancelRequest.  # noqa: E501
        :type: str
        """
        if shipment_id is None:
            raise ValueError("Invalid value for `shipment_id`, must not be `None`")  # noqa: E501

        self._shipment_id = shipment_id

    @property
    def reason_for_cancellation(self):
        """Gets the reason_for_cancellation of this ShipmentCancelRequest.  # noqa: E501

        Reason for Cancellation  # noqa: E501

        :return: The reason_for_cancellation of this ShipmentCancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason_for_cancellation

    @reason_for_cancellation.setter
    def reason_for_cancellation(self, reason_for_cancellation):
        """Sets the reason_for_cancellation of this ShipmentCancelRequest.

        Reason for Cancellation  # noqa: E501

        :param reason_for_cancellation: The reason_for_cancellation of this ShipmentCancelRequest.  # noqa: E501
        :type: str
        """
        if reason_for_cancellation is None:
            raise ValueError("Invalid value for `reason_for_cancellation`, must not be `None`")  # noqa: E501
        allowed_values = ["OrderCancelled", "Repacked", "UploadedInError", "WrongService"]  # noqa: E501
        if reason_for_cancellation not in allowed_values:
            raise ValueError(
                "Invalid value for `reason_for_cancellation` ({0}), must be one of {1}"  # noqa: E501
                .format(reason_for_cancellation, allowed_values)
            )

        self._reason_for_cancellation = reason_for_cancellation

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
        if issubclass(ShipmentCancelRequest, dict):
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
        if not isinstance(other, ShipmentCancelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other