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


class ScimPatchOperation(object):
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
        'op': 'str',
        'path': 'str',
        'value': 'str'
    }

    attribute_map = {
        'op': 'op',
        'path': 'path',
        'value': 'value'
    }

    def __init__(self, op=None, path=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ScimPatchOperation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._op = None
        self._path = None
        self._value = None
        self.discriminator = None

        self.op = op
        if path is not None:
            self.path = path
        if value is not None:
            self.value = value

    @property
    def op(self):
        """Gets the op of this ScimPatchOperation.  # noqa: E501

        The method that should be used in the operation.  # noqa: E501

        :return: The op of this ScimPatchOperation.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this ScimPatchOperation.

        The method that should be used in the operation.  # noqa: E501

        :param op: The op of this ScimPatchOperation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and op is None:  # noqa: E501
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        allowed_values = ["add", "remove", "replace"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and op not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"  # noqa: E501
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def path(self):
        """Gets the path of this ScimPatchOperation.  # noqa: E501

        The path specifying the attribute that should be updated.  # noqa: E501

        :return: The path of this ScimPatchOperation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ScimPatchOperation.

        The path specifying the attribute that should be updated.  # noqa: E501

        :param path: The path of this ScimPatchOperation.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def value(self):
        """Gets the value of this ScimPatchOperation.  # noqa: E501

        The value that should be updated. Required if `op` is `add` or `replace`.  # noqa: E501

        :return: The value of this ScimPatchOperation.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ScimPatchOperation.

        The value that should be updated. Required if `op` is `add` or `replace`.  # noqa: E501

        :param value: The value of this ScimPatchOperation.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, ScimPatchOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScimPatchOperation):
            return True

        return self.to_dict() != other.to_dict()
