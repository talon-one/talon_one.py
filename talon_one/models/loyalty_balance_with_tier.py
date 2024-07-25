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


class LoyaltyBalanceWithTier(object):
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
        'active_points': 'float',
        'pending_points': 'float',
        'spent_points': 'float',
        'expired_points': 'float',
        'current_tier': 'Tier',
        'projected_tier': 'ProjectedTier',
        'points_to_next_tier': 'float',
        'next_tier_name': 'str'
    }

    attribute_map = {
        'active_points': 'activePoints',
        'pending_points': 'pendingPoints',
        'spent_points': 'spentPoints',
        'expired_points': 'expiredPoints',
        'current_tier': 'currentTier',
        'projected_tier': 'projectedTier',
        'points_to_next_tier': 'pointsToNextTier',
        'next_tier_name': 'nextTierName'
    }

    def __init__(self, active_points=None, pending_points=None, spent_points=None, expired_points=None, current_tier=None, projected_tier=None, points_to_next_tier=None, next_tier_name=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyBalanceWithTier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_points = None
        self._pending_points = None
        self._spent_points = None
        self._expired_points = None
        self._current_tier = None
        self._projected_tier = None
        self._points_to_next_tier = None
        self._next_tier_name = None
        self.discriminator = None

        if active_points is not None:
            self.active_points = active_points
        if pending_points is not None:
            self.pending_points = pending_points
        if spent_points is not None:
            self.spent_points = spent_points
        if expired_points is not None:
            self.expired_points = expired_points
        if current_tier is not None:
            self.current_tier = current_tier
        if projected_tier is not None:
            self.projected_tier = projected_tier
        if points_to_next_tier is not None:
            self.points_to_next_tier = points_to_next_tier
        if next_tier_name is not None:
            self.next_tier_name = next_tier_name

    @property
    def active_points(self):
        """Gets the active_points of this LoyaltyBalanceWithTier.  # noqa: E501

        Total amount of points awarded to this customer and available to spend.  # noqa: E501

        :return: The active_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: float
        """
        return self._active_points

    @active_points.setter
    def active_points(self, active_points):
        """Sets the active_points of this LoyaltyBalanceWithTier.

        Total amount of points awarded to this customer and available to spend.  # noqa: E501

        :param active_points: The active_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: float
        """

        self._active_points = active_points

    @property
    def pending_points(self):
        """Gets the pending_points of this LoyaltyBalanceWithTier.  # noqa: E501

        Total amount of points awarded to this customer but not available until their start date.  # noqa: E501

        :return: The pending_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: float
        """
        return self._pending_points

    @pending_points.setter
    def pending_points(self, pending_points):
        """Sets the pending_points of this LoyaltyBalanceWithTier.

        Total amount of points awarded to this customer but not available until their start date.  # noqa: E501

        :param pending_points: The pending_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: float
        """

        self._pending_points = pending_points

    @property
    def spent_points(self):
        """Gets the spent_points of this LoyaltyBalanceWithTier.  # noqa: E501

        Total amount of points already spent by this customer.  # noqa: E501

        :return: The spent_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: float
        """
        return self._spent_points

    @spent_points.setter
    def spent_points(self, spent_points):
        """Sets the spent_points of this LoyaltyBalanceWithTier.

        Total amount of points already spent by this customer.  # noqa: E501

        :param spent_points: The spent_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: float
        """

        self._spent_points = spent_points

    @property
    def expired_points(self):
        """Gets the expired_points of this LoyaltyBalanceWithTier.  # noqa: E501

        Total amount of points awarded but never redeemed. They cannot be used anymore.  # noqa: E501

        :return: The expired_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: float
        """
        return self._expired_points

    @expired_points.setter
    def expired_points(self, expired_points):
        """Sets the expired_points of this LoyaltyBalanceWithTier.

        Total amount of points awarded but never redeemed. They cannot be used anymore.  # noqa: E501

        :param expired_points: The expired_points of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: float
        """

        self._expired_points = expired_points

    @property
    def current_tier(self):
        """Gets the current_tier of this LoyaltyBalanceWithTier.  # noqa: E501


        :return: The current_tier of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: Tier
        """
        return self._current_tier

    @current_tier.setter
    def current_tier(self, current_tier):
        """Sets the current_tier of this LoyaltyBalanceWithTier.


        :param current_tier: The current_tier of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: Tier
        """

        self._current_tier = current_tier

    @property
    def projected_tier(self):
        """Gets the projected_tier of this LoyaltyBalanceWithTier.  # noqa: E501


        :return: The projected_tier of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: ProjectedTier
        """
        return self._projected_tier

    @projected_tier.setter
    def projected_tier(self, projected_tier):
        """Sets the projected_tier of this LoyaltyBalanceWithTier.


        :param projected_tier: The projected_tier of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: ProjectedTier
        """

        self._projected_tier = projected_tier

    @property
    def points_to_next_tier(self):
        """Gets the points_to_next_tier of this LoyaltyBalanceWithTier.  # noqa: E501

        The number of points required to move up a tier.  # noqa: E501

        :return: The points_to_next_tier of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: float
        """
        return self._points_to_next_tier

    @points_to_next_tier.setter
    def points_to_next_tier(self, points_to_next_tier):
        """Sets the points_to_next_tier of this LoyaltyBalanceWithTier.

        The number of points required to move up a tier.  # noqa: E501

        :param points_to_next_tier: The points_to_next_tier of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: float
        """

        self._points_to_next_tier = points_to_next_tier

    @property
    def next_tier_name(self):
        """Gets the next_tier_name of this LoyaltyBalanceWithTier.  # noqa: E501

        The name of the tier consecutive to the current tier.  # noqa: E501

        :return: The next_tier_name of this LoyaltyBalanceWithTier.  # noqa: E501
        :rtype: str
        """
        return self._next_tier_name

    @next_tier_name.setter
    def next_tier_name(self, next_tier_name):
        """Sets the next_tier_name of this LoyaltyBalanceWithTier.

        The name of the tier consecutive to the current tier.  # noqa: E501

        :param next_tier_name: The next_tier_name of this LoyaltyBalanceWithTier.  # noqa: E501
        :type: str
        """

        self._next_tier_name = next_tier_name

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
        if not isinstance(other, LoyaltyBalanceWithTier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyBalanceWithTier):
            return True

        return self.to_dict() != other.to_dict()