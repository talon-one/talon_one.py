# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class NotificationTest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'http_response': 'str',
        'http_status': 'int'
    }

    attribute_map = {
        'http_response': 'httpResponse',
        'http_status': 'httpStatus'
    }

    def __init__(self, http_response=None, http_status=None, local_vars_configuration=None):  # noqa: E501
        """NotificationTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._http_response = None
        self._http_status = None
        self.discriminator = None

        self.http_response = http_response
        self.http_status = http_status

    @property
    def http_response(self):
        """Gets the http_response of this NotificationTest.  # noqa: E501

        The returned http response.  # noqa: E501

        :return: The http_response of this NotificationTest.  # noqa: E501
        :rtype: str
        """
        return self._http_response

    @http_response.setter
    def http_response(self, http_response):
        """Sets the http_response of this NotificationTest.

        The returned http response.  # noqa: E501

        :param http_response: The http_response of this NotificationTest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and http_response is None:  # noqa: E501
            raise ValueError("Invalid value for `http_response`, must not be `None`")  # noqa: E501

        self._http_response = http_response

    @property
    def http_status(self):
        """Gets the http_status of this NotificationTest.  # noqa: E501

        The returned http status code.  # noqa: E501

        :return: The http_status of this NotificationTest.  # noqa: E501
        :rtype: int
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this NotificationTest.

        The returned http status code.  # noqa: E501

        :param http_status: The http_status of this NotificationTest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and http_status is None:  # noqa: E501
            raise ValueError("Invalid value for `http_status`, must not be `None`")  # noqa: E501

        self._http_status = http_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationTest):
            return True

        return self.to_dict() != other.to_dict()
