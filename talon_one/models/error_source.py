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


class ErrorSource(object):
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
        'pointer': 'str',
        'parameter': 'str',
        'line': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'pointer': 'pointer',
        'parameter': 'parameter',
        'line': 'line',
        'resource': 'resource'
    }

    def __init__(self, pointer=None, parameter=None, line=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """ErrorSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pointer = None
        self._parameter = None
        self._line = None
        self._resource = None
        self.discriminator = None

        if pointer is not None:
            self.pointer = pointer
        if parameter is not None:
            self.parameter = parameter
        if line is not None:
            self.line = line
        if resource is not None:
            self.resource = resource

    @property
    def pointer(self):
        """Gets the pointer of this ErrorSource.  # noqa: E501

        Pointer to the path in the payload that caused this error.  # noqa: E501

        :return: The pointer of this ErrorSource.  # noqa: E501
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this ErrorSource.

        Pointer to the path in the payload that caused this error.  # noqa: E501

        :param pointer: The pointer of this ErrorSource.  # noqa: E501
        :type: str
        """

        self._pointer = pointer

    @property
    def parameter(self):
        """Gets the parameter of this ErrorSource.  # noqa: E501

        Query parameter that caused this error.  # noqa: E501

        :return: The parameter of this ErrorSource.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ErrorSource.

        Query parameter that caused this error.  # noqa: E501

        :param parameter: The parameter of this ErrorSource.  # noqa: E501
        :type: str
        """

        self._parameter = parameter

    @property
    def line(self):
        """Gets the line of this ErrorSource.  # noqa: E501

        Line number in uploaded multipart file that caused this error. 'N/A' if unknown.  # noqa: E501

        :return: The line of this ErrorSource.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this ErrorSource.

        Line number in uploaded multipart file that caused this error. 'N/A' if unknown.  # noqa: E501

        :param line: The line of this ErrorSource.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def resource(self):
        """Gets the resource of this ErrorSource.  # noqa: E501

        Pointer to the resource that caused this error.  # noqa: E501

        :return: The resource of this ErrorSource.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ErrorSource.

        Pointer to the resource that caused this error.  # noqa: E501

        :param resource: The resource of this ErrorSource.  # noqa: E501
        :type: str
        """

        self._resource = resource

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
        if not isinstance(other, ErrorSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorSource):
            return True

        return self.to_dict() != other.to_dict()
