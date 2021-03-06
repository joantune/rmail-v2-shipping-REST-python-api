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


class ShipmentCreateResponse(object):
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
        'consignment_number': 'str',
        'consignment_tracking_url': 'str',
        'packages': 'list[PackageResponse]',
        'routing': 'RoutingResponse',
        'label_image_format': 'str',
        'label_images': 'str',
        'customs_documents': 'str',
        'return_label_image_format': 'str',
        'return_label_images': 'str',
        'http_status_code': 'int',
        'http_status_description': 'str',
        'message': 'str',
        'errors': 'list[ErrorDetail]'
    }

    attribute_map = {
        'consignment_number': 'ConsignmentNumber',
        'consignment_tracking_url': 'ConsignmentTrackingUrl',
        'packages': 'Packages',
        'routing': 'Routing',
        'label_image_format': 'LabelImageFormat',
        'label_images': 'LabelImages',
        'customs_documents': 'CustomsDocuments',
        'return_label_image_format': 'ReturnLabelImageFormat',
        'return_label_images': 'ReturnLabelImages',
        'http_status_code': 'HttpStatusCode',
        'http_status_description': 'HttpStatusDescription',
        'message': 'Message',
        'errors': 'Errors'
    }

    def __init__(self, consignment_number=None, consignment_tracking_url=None, packages=None, routing=None, label_image_format=None, label_images=None, customs_documents=None, return_label_image_format=None, return_label_images=None, http_status_code=None, http_status_description=None, message=None, errors=None):  # noqa: E501
        """ShipmentCreateResponse - a model defined in Swagger"""  # noqa: E501
        self._consignment_number = None
        self._consignment_tracking_url = None
        self._packages = None
        self._routing = None
        self._label_image_format = None
        self._label_images = None
        self._customs_documents = None
        self._return_label_image_format = None
        self._return_label_images = None
        self._http_status_code = None
        self._http_status_description = None
        self._message = None
        self._errors = None
        self.discriminator = None
        if consignment_number is not None:
            self.consignment_number = consignment_number
        if consignment_tracking_url is not None:
            self.consignment_tracking_url = consignment_tracking_url
        if packages is not None:
            self.packages = packages
        if routing is not None:
            self.routing = routing
        if label_image_format is not None:
            self.label_image_format = label_image_format
        if label_images is not None:
            self.label_images = label_images
        if customs_documents is not None:
            self.customs_documents = customs_documents
        if return_label_image_format is not None:
            self.return_label_image_format = return_label_image_format
        if return_label_images is not None:
            self.return_label_images = return_label_images
        self.http_status_code = http_status_code
        self.http_status_description = http_status_description
        if message is not None:
            self.message = message
        if errors is not None:
            self.errors = errors

    @property
    def consignment_number(self):
        """Gets the consignment_number of this ShipmentCreateResponse.  # noqa: E501

        Consignment Number<br />Only populated for services that support Multi-Packages  # noqa: E501

        :return: The consignment_number of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._consignment_number

    @consignment_number.setter
    def consignment_number(self, consignment_number):
        """Sets the consignment_number of this ShipmentCreateResponse.

        Consignment Number<br />Only populated for services that support Multi-Packages  # noqa: E501

        :param consignment_number: The consignment_number of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """

        self._consignment_number = consignment_number

    @property
    def consignment_tracking_url(self):
        """Gets the consignment_tracking_url of this ShipmentCreateResponse.  # noqa: E501

        Consignment Tracking URL<br />Only populated for services that support Multi-Packages  # noqa: E501

        :return: The consignment_tracking_url of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._consignment_tracking_url

    @consignment_tracking_url.setter
    def consignment_tracking_url(self, consignment_tracking_url):
        """Sets the consignment_tracking_url of this ShipmentCreateResponse.

        Consignment Tracking URL<br />Only populated for services that support Multi-Packages  # noqa: E501

        :param consignment_tracking_url: The consignment_tracking_url of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """

        self._consignment_tracking_url = consignment_tracking_url

    @property
    def packages(self):
        """Gets the packages of this ShipmentCreateResponse.  # noqa: E501

        Packages<br />Details each package tracking information and Unique Id.  # noqa: E501

        :return: The packages of this ShipmentCreateResponse.  # noqa: E501
        :rtype: list[PackageResponse]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this ShipmentCreateResponse.

        Packages<br />Details each package tracking information and Unique Id.  # noqa: E501

        :param packages: The packages of this ShipmentCreateResponse.  # noqa: E501
        :type: list[PackageResponse]
        """

        self._packages = packages

    @property
    def routing(self):
        """Gets the routing of this ShipmentCreateResponse.  # noqa: E501


        :return: The routing of this ShipmentCreateResponse.  # noqa: E501
        :rtype: RoutingResponse
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """Sets the routing of this ShipmentCreateResponse.


        :param routing: The routing of this ShipmentCreateResponse.  # noqa: E501
        :type: RoutingResponse
        """

        self._routing = routing

    @property
    def label_image_format(self):
        """Gets the label_image_format of this ShipmentCreateResponse.  # noqa: E501

        Label Image Format  # noqa: E501

        :return: The label_image_format of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._label_image_format

    @label_image_format.setter
    def label_image_format(self, label_image_format):
        """Sets the label_image_format of this ShipmentCreateResponse.

        Label Image Format  # noqa: E501

        :param label_image_format: The label_image_format of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PDF", "PNG", "DATASTREAM", "ZPL203DPI", "ZPL300DPI"]  # noqa: E501
        if label_image_format not in allowed_values:
            raise ValueError(
                "Invalid value for `label_image_format` ({0}), must be one of {1}"  # noqa: E501
                .format(label_image_format, allowed_values)
            )

        self._label_image_format = label_image_format

    @property
    def label_images(self):
        """Gets the label_images of this ShipmentCreateResponse.  # noqa: E501

        Label Images<br />Any labels that have been created as a result of the request.<br />Depends on Label Image Format.<br />            <br />**PDF**<br />Base 64 encoded PDF<br />            <br />**PNG**<br />Base 64 encoded PNG<br />            <br />**ZPL 300 / 203 dpi**<br />Base 64 encoded PRN (text file)<br />            <br />**Data stream**<br />Not Included - see Packages for Data Stream responses  # noqa: E501

        :return: The label_images of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._label_images

    @label_images.setter
    def label_images(self, label_images):
        """Sets the label_images of this ShipmentCreateResponse.

        Label Images<br />Any labels that have been created as a result of the request.<br />Depends on Label Image Format.<br />            <br />**PDF**<br />Base 64 encoded PDF<br />            <br />**PNG**<br />Base 64 encoded PNG<br />            <br />**ZPL 300 / 203 dpi**<br />Base 64 encoded PRN (text file)<br />            <br />**Data stream**<br />Not Included - see Packages for Data Stream responses  # noqa: E501

        :param label_images: The label_images of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """

        self._label_images = label_images

    @property
    def customs_documents(self):
        """Gets the customs_documents of this ShipmentCreateResponse.  # noqa: E501

        Customs Documents<br />Base 64 encoded PDF<br />Any customs documents that have been created as a result of the request.  # noqa: E501

        :return: The customs_documents of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._customs_documents

    @customs_documents.setter
    def customs_documents(self, customs_documents):
        """Sets the customs_documents of this ShipmentCreateResponse.

        Customs Documents<br />Base 64 encoded PDF<br />Any customs documents that have been created as a result of the request.  # noqa: E501

        :param customs_documents: The customs_documents of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """

        self._customs_documents = customs_documents

    @property
    def return_label_image_format(self):
        """Gets the return_label_image_format of this ShipmentCreateResponse.  # noqa: E501

        Return Label Image Format  # noqa: E501

        :return: The return_label_image_format of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_label_image_format

    @return_label_image_format.setter
    def return_label_image_format(self, return_label_image_format):
        """Sets the return_label_image_format of this ShipmentCreateResponse.

        Return Label Image Format  # noqa: E501

        :param return_label_image_format: The return_label_image_format of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PDF", "PNG", "ZPL300DPI", "ZPL203DPI"]  # noqa: E501
        if return_label_image_format not in allowed_values:
            raise ValueError(
                "Invalid value for `return_label_image_format` ({0}), must be one of {1}"  # noqa: E501
                .format(return_label_image_format, allowed_values)
            )

        self._return_label_image_format = return_label_image_format

    @property
    def return_label_images(self):
        """Gets the return_label_images of this ShipmentCreateResponse.  # noqa: E501

        Return Label Images<br />Any return labels that have been created as a result of the request and label option settings.<br />Depends on ReturnLabelImageFormat.<br />            <br />**PDF**<br />Base 64 encoded PDF<br />            <br />**PNG**<br />Base 64 encoded PNG<br />            <br />**ZPL 300 / 203 dpi**<br />Base 64 encoded PRN (text file)  # noqa: E501

        :return: The return_label_images of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_label_images

    @return_label_images.setter
    def return_label_images(self, return_label_images):
        """Sets the return_label_images of this ShipmentCreateResponse.

        Return Label Images<br />Any return labels that have been created as a result of the request and label option settings.<br />Depends on ReturnLabelImageFormat.<br />            <br />**PDF**<br />Base 64 encoded PDF<br />            <br />**PNG**<br />Base 64 encoded PNG<br />            <br />**ZPL 300 / 203 dpi**<br />Base 64 encoded PRN (text file)  # noqa: E501

        :param return_label_images: The return_label_images of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """

        self._return_label_images = return_label_images

    @property
    def http_status_code(self):
        """Gets the http_status_code of this ShipmentCreateResponse.  # noqa: E501

        HTTP Status Code  # noqa: E501

        :return: The http_status_code of this ShipmentCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this ShipmentCreateResponse.

        HTTP Status Code  # noqa: E501

        :param http_status_code: The http_status_code of this ShipmentCreateResponse.  # noqa: E501
        :type: int
        """
        if http_status_code is None:
            raise ValueError("Invalid value for `http_status_code`, must not be `None`")  # noqa: E501

        self._http_status_code = http_status_code

    @property
    def http_status_description(self):
        """Gets the http_status_description of this ShipmentCreateResponse.  # noqa: E501

        HTTP Status Description  # noqa: E501

        :return: The http_status_description of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._http_status_description

    @http_status_description.setter
    def http_status_description(self, http_status_description):
        """Sets the http_status_description of this ShipmentCreateResponse.

        HTTP Status Description  # noqa: E501

        :param http_status_description: The http_status_description of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """
        if http_status_description is None:
            raise ValueError("Invalid value for `http_status_description`, must not be `None`")  # noqa: E501

        self._http_status_description = http_status_description

    @property
    def message(self):
        """Gets the message of this ShipmentCreateResponse.  # noqa: E501

        Message<br />Successful response may include a success message.<br />Failure responses will have general reason as to why. Further details may be contained in the list of errors.  # noqa: E501

        :return: The message of this ShipmentCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShipmentCreateResponse.

        Message<br />Successful response may include a success message.<br />Failure responses will have general reason as to why. Further details may be contained in the list of errors.  # noqa: E501

        :param message: The message of this ShipmentCreateResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this ShipmentCreateResponse.  # noqa: E501

        Errors<br />Details about why a request failed.  # noqa: E501

        :return: The errors of this ShipmentCreateResponse.  # noqa: E501
        :rtype: list[ErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ShipmentCreateResponse.

        Errors<br />Details about why a request failed.  # noqa: E501

        :param errors: The errors of this ShipmentCreateResponse.  # noqa: E501
        :type: list[ErrorDetail]
        """

        self._errors = errors

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
        if issubclass(ShipmentCreateResponse, dict):
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
        if not isinstance(other, ShipmentCreateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
