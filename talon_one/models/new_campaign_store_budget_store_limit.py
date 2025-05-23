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


class NewCampaignStoreBudgetStoreLimit(object):
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
        'store_id': 'int',
        'limit': 'float'
    }

    attribute_map = {
        'store_id': 'storeId',
        'limit': 'limit'
    }

    def __init__(self, store_id=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """NewCampaignStoreBudgetStoreLimit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._store_id = None
        self._limit = None
        self.discriminator = None

        self.store_id = store_id
        self.limit = limit

    @property
    def store_id(self):
        """Gets the store_id of this NewCampaignStoreBudgetStoreLimit.  # noqa: E501

        The ID of the store. You can get this ID with the [List stores](#tag/Stores/operation/listStores) endpoint.   # noqa: E501

        :return: The store_id of this NewCampaignStoreBudgetStoreLimit.  # noqa: E501
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this NewCampaignStoreBudgetStoreLimit.

        The ID of the store. You can get this ID with the [List stores](#tag/Stores/operation/listStores) endpoint.   # noqa: E501

        :param store_id: The store_id of this NewCampaignStoreBudgetStoreLimit.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and store_id is None:  # noqa: E501
            raise ValueError("Invalid value for `store_id`, must not be `None`")  # noqa: E501

        self._store_id = store_id

    @property
    def limit(self):
        """Gets the limit of this NewCampaignStoreBudgetStoreLimit.  # noqa: E501

        The value to set for the limit.  # noqa: E501

        :return: The limit of this NewCampaignStoreBudgetStoreLimit.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NewCampaignStoreBudgetStoreLimit.

        The value to set for the limit.  # noqa: E501

        :param limit: The limit of this NewCampaignStoreBudgetStoreLimit.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

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
        if not isinstance(other, NewCampaignStoreBudgetStoreLimit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewCampaignStoreBudgetStoreLimit):
            return True

        return self.to_dict() != other.to_dict()
