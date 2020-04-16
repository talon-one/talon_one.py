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


class IntegrationState(object):
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
        'session': 'CustomerSession',
        'profile': 'CustomerProfile',
        'event': 'Event',
        'loyalty': 'Loyalty',
        'coupon': 'Coupon'
    }

    attribute_map = {
        'session': 'session',
        'profile': 'profile',
        'event': 'event',
        'loyalty': 'loyalty',
        'coupon': 'coupon'
    }

    def __init__(self, session=None, profile=None, event=None, loyalty=None, coupon=None, local_vars_configuration=None):  # noqa: E501
        """IntegrationState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._session = None
        self._profile = None
        self._event = None
        self._loyalty = None
        self._coupon = None
        self.discriminator = None

        self.session = session
        self.profile = profile
        self.event = event
        if loyalty is not None:
            self.loyalty = loyalty
        if coupon is not None:
            self.coupon = coupon

    @property
    def session(self):
        """Gets the session of this IntegrationState.  # noqa: E501


        :return: The session of this IntegrationState.  # noqa: E501
        :rtype: CustomerSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this IntegrationState.


        :param session: The session of this IntegrationState.  # noqa: E501
        :type: CustomerSession
        """
        if self.local_vars_configuration.client_side_validation and session is None:  # noqa: E501
            raise ValueError("Invalid value for `session`, must not be `None`")  # noqa: E501

        self._session = session

    @property
    def profile(self):
        """Gets the profile of this IntegrationState.  # noqa: E501


        :return: The profile of this IntegrationState.  # noqa: E501
        :rtype: CustomerProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this IntegrationState.


        :param profile: The profile of this IntegrationState.  # noqa: E501
        :type: CustomerProfile
        """
        if self.local_vars_configuration.client_side_validation and profile is None:  # noqa: E501
            raise ValueError("Invalid value for `profile`, must not be `None`")  # noqa: E501

        self._profile = profile

    @property
    def event(self):
        """Gets the event of this IntegrationState.  # noqa: E501


        :return: The event of this IntegrationState.  # noqa: E501
        :rtype: Event
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this IntegrationState.


        :param event: The event of this IntegrationState.  # noqa: E501
        :type: Event
        """
        if self.local_vars_configuration.client_side_validation and event is None:  # noqa: E501
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def loyalty(self):
        """Gets the loyalty of this IntegrationState.  # noqa: E501


        :return: The loyalty of this IntegrationState.  # noqa: E501
        :rtype: Loyalty
        """
        return self._loyalty

    @loyalty.setter
    def loyalty(self, loyalty):
        """Sets the loyalty of this IntegrationState.


        :param loyalty: The loyalty of this IntegrationState.  # noqa: E501
        :type: Loyalty
        """

        self._loyalty = loyalty

    @property
    def coupon(self):
        """Gets the coupon of this IntegrationState.  # noqa: E501


        :return: The coupon of this IntegrationState.  # noqa: E501
        :rtype: Coupon
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this IntegrationState.


        :param coupon: The coupon of this IntegrationState.  # noqa: E501
        :type: Coupon
        """

        self._coupon = coupon

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
        if not isinstance(other, IntegrationState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationState):
            return True

        return self.to_dict() != other.to_dict()
