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


class NewLoyaltyProgram(object):
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
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'subscribed_applications': 'list[int]',
        'default_validity': 'str',
        'default_pending': 'str',
        'allow_subledger': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'subscribed_applications': 'subscribedApplications',
        'default_validity': 'defaultValidity',
        'default_pending': 'defaultPending',
        'allow_subledger': 'allowSubledger'
    }

    def __init__(self, name=None, title=None, description=None, subscribed_applications=None, default_validity=None, default_pending=None, allow_subledger=None, local_vars_configuration=None):  # noqa: E501
        """NewLoyaltyProgram - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._title = None
        self._description = None
        self._subscribed_applications = None
        self._default_validity = None
        self._default_pending = None
        self._allow_subledger = None
        self.discriminator = None

        self.name = name
        self.title = title
        if description is not None:
            self.description = description
        if subscribed_applications is not None:
            self.subscribed_applications = subscribed_applications
        self.default_validity = default_validity
        self.default_pending = default_pending
        self.allow_subledger = allow_subledger

    @property
    def name(self):
        """Gets the name of this NewLoyaltyProgram.  # noqa: E501

        The internal name for the Loyalty Program. This is an immutable value.  # noqa: E501

        :return: The name of this NewLoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewLoyaltyProgram.

        The internal name for the Loyalty Program. This is an immutable value.  # noqa: E501

        :param name: The name of this NewLoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this NewLoyaltyProgram.  # noqa: E501

        The display title for the Loyalty Program.  # noqa: E501

        :return: The title of this NewLoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewLoyaltyProgram.

        The display title for the Loyalty Program.  # noqa: E501

        :param title: The title of this NewLoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this NewLoyaltyProgram.  # noqa: E501

        Description of our Loyalty Program.  # noqa: E501

        :return: The description of this NewLoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewLoyaltyProgram.

        Description of our Loyalty Program.  # noqa: E501

        :param description: The description of this NewLoyaltyProgram.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def subscribed_applications(self):
        """Gets the subscribed_applications of this NewLoyaltyProgram.  # noqa: E501

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :return: The subscribed_applications of this NewLoyaltyProgram.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications

    @subscribed_applications.setter
    def subscribed_applications(self, subscribed_applications):
        """Sets the subscribed_applications of this NewLoyaltyProgram.

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :param subscribed_applications: The subscribed_applications of this NewLoyaltyProgram.  # noqa: E501
        :type: list[int]
        """

        self._subscribed_applications = subscribed_applications

    @property
    def default_validity(self):
        """Gets the default_validity of this NewLoyaltyProgram.  # noqa: E501

        Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like '1h' or '40m'.  # noqa: E501

        :return: The default_validity of this NewLoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_validity

    @default_validity.setter
    def default_validity(self, default_validity):
        """Sets the default_validity of this NewLoyaltyProgram.

        Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like '1h' or '40m'.  # noqa: E501

        :param default_validity: The default_validity of this NewLoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_validity is None:  # noqa: E501
            raise ValueError("Invalid value for `default_validity`, must not be `None`")  # noqa: E501

        self._default_validity = default_validity

    @property
    def default_pending(self):
        """Gets the default_pending of this NewLoyaltyProgram.  # noqa: E501

        Indicates the default duration for the pending time, after which points will be valid. The format is a number followed by a duration unit, like '1h' or '40m'.  # noqa: E501

        :return: The default_pending of this NewLoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_pending

    @default_pending.setter
    def default_pending(self, default_pending):
        """Sets the default_pending of this NewLoyaltyProgram.

        Indicates the default duration for the pending time, after which points will be valid. The format is a number followed by a duration unit, like '1h' or '40m'.  # noqa: E501

        :param default_pending: The default_pending of this NewLoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_pending is None:  # noqa: E501
            raise ValueError("Invalid value for `default_pending`, must not be `None`")  # noqa: E501

        self._default_pending = default_pending

    @property
    def allow_subledger(self):
        """Gets the allow_subledger of this NewLoyaltyProgram.  # noqa: E501

        Indicates if this program supports subledgers inside the program  # noqa: E501

        :return: The allow_subledger of this NewLoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subledger

    @allow_subledger.setter
    def allow_subledger(self, allow_subledger):
        """Sets the allow_subledger of this NewLoyaltyProgram.

        Indicates if this program supports subledgers inside the program  # noqa: E501

        :param allow_subledger: The allow_subledger of this NewLoyaltyProgram.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_subledger is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_subledger`, must not be `None`")  # noqa: E501

        self._allow_subledger = allow_subledger

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
        if not isinstance(other, NewLoyaltyProgram):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewLoyaltyProgram):
            return True

        return self.to_dict() != other.to_dict()
