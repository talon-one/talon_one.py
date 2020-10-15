# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class UpdateUserLatestFeedTimestamp(object):
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
        'new_latest_feed_timestamp': 'datetime'
    }

    attribute_map = {
        'new_latest_feed_timestamp': 'newLatestFeedTimestamp'
    }

    def __init__(self, new_latest_feed_timestamp=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserLatestFeedTimestamp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._new_latest_feed_timestamp = None
        self.discriminator = None

        self.new_latest_feed_timestamp = new_latest_feed_timestamp

    @property
    def new_latest_feed_timestamp(self):
        """Gets the new_latest_feed_timestamp of this UpdateUserLatestFeedTimestamp.  # noqa: E501

        New timestamp to update for the current user  # noqa: E501

        :return: The new_latest_feed_timestamp of this UpdateUserLatestFeedTimestamp.  # noqa: E501
        :rtype: datetime
        """
        return self._new_latest_feed_timestamp

    @new_latest_feed_timestamp.setter
    def new_latest_feed_timestamp(self, new_latest_feed_timestamp):
        """Sets the new_latest_feed_timestamp of this UpdateUserLatestFeedTimestamp.

        New timestamp to update for the current user  # noqa: E501

        :param new_latest_feed_timestamp: The new_latest_feed_timestamp of this UpdateUserLatestFeedTimestamp.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and new_latest_feed_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `new_latest_feed_timestamp`, must not be `None`")  # noqa: E501

        self._new_latest_feed_timestamp = new_latest_feed_timestamp

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
        if not isinstance(other, UpdateUserLatestFeedTimestamp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserLatestFeedTimestamp):
            return True

        return self.to_dict() != other.to_dict()
