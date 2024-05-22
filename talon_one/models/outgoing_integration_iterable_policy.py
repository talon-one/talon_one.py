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


class OutgoingIntegrationIterablePolicy(object):
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
        'base_url': 'str',
        'api_key': 'str'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'api_key': 'apiKey'
    }

    def __init__(self, base_url=None, api_key=None, local_vars_configuration=None):  # noqa: E501
        """OutgoingIntegrationIterablePolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_url = None
        self._api_key = None
        self.discriminator = None

        self.base_url = base_url
        self.api_key = api_key

    @property
    def base_url(self):
        """Gets the base_url of this OutgoingIntegrationIterablePolicy.  # noqa: E501

        The base URL that is based on the region key of your Iterable account.  # noqa: E501

        :return: The base_url of this OutgoingIntegrationIterablePolicy.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this OutgoingIntegrationIterablePolicy.

        The base URL that is based on the region key of your Iterable account.  # noqa: E501

        :param base_url: The base_url of this OutgoingIntegrationIterablePolicy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_url is None:  # noqa: E501
            raise ValueError("Invalid value for `base_url`, must not be `None`")  # noqa: E501

        self._base_url = base_url

    @property
    def api_key(self):
        """Gets the api_key of this OutgoingIntegrationIterablePolicy.  # noqa: E501

        The API key generated from your Iterable account. See [Iterable API Key Guide](https://support.iterable.com/hc/en-us/articles/360043464871-API-Keys-)  # noqa: E501

        :return: The api_key of this OutgoingIntegrationIterablePolicy.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this OutgoingIntegrationIterablePolicy.

        The API key generated from your Iterable account. See [Iterable API Key Guide](https://support.iterable.com/hc/en-us/articles/360043464871-API-Keys-)  # noqa: E501

        :param api_key: The api_key of this OutgoingIntegrationIterablePolicy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_key is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

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
        if not isinstance(other, OutgoingIntegrationIterablePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutgoingIntegrationIterablePolicy):
            return True

        return self.to_dict() != other.to_dict()
