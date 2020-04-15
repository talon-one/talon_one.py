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


class Rule(object):
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
        'title': 'str',
        'description': 'str',
        'bindings': 'list[Binding]',
        'condition': 'list[object]',
        'effects': 'list[object]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'bindings': 'bindings',
        'condition': 'condition',
        'effects': 'effects'
    }

    def __init__(self, title=None, description=None, bindings=None, condition=None, effects=None, local_vars_configuration=None):  # noqa: E501
        """Rule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._description = None
        self._bindings = None
        self._condition = None
        self._effects = None
        self.discriminator = None

        self.title = title
        if description is not None:
            self.description = description
        if bindings is not None:
            self.bindings = bindings
        self.condition = condition
        self.effects = effects

    @property
    def title(self):
        """Gets the title of this Rule.  # noqa: E501

        A short description of the rule.  # noqa: E501

        :return: The title of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Rule.

        A short description of the rule.  # noqa: E501

        :param title: The title of this Rule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Rule.  # noqa: E501

        A longer, more detailed description of the rule.  # noqa: E501

        :return: The description of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.

        A longer, more detailed description of the rule.  # noqa: E501

        :param description: The description of this Rule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def bindings(self):
        """Gets the bindings of this Rule.  # noqa: E501

        An array that provides objects with variable names (name) and talang expressions to whose result they are bound (expression) during rule evaluation. The order of the evaluation is decided by the position in the array.  # noqa: E501

        :return: The bindings of this Rule.  # noqa: E501
        :rtype: list[Binding]
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        """Sets the bindings of this Rule.

        An array that provides objects with variable names (name) and talang expressions to whose result they are bound (expression) during rule evaluation. The order of the evaluation is decided by the position in the array.  # noqa: E501

        :param bindings: The bindings of this Rule.  # noqa: E501
        :type: list[Binding]
        """

        self._bindings = bindings

    @property
    def condition(self):
        """Gets the condition of this Rule.  # noqa: E501

        A Talang expression that will be evaluated in the context of the given event.  # noqa: E501

        :return: The condition of this Rule.  # noqa: E501
        :rtype: list[object]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Rule.

        A Talang expression that will be evaluated in the context of the given event.  # noqa: E501

        :param condition: The condition of this Rule.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and condition is None:  # noqa: E501
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition

    @property
    def effects(self):
        """Gets the effects of this Rule.  # noqa: E501

        An array of effectful Talang expressions in arrays that will be evaluated when a rule matches.  # noqa: E501

        :return: The effects of this Rule.  # noqa: E501
        :rtype: list[object]
        """
        return self._effects

    @effects.setter
    def effects(self, effects):
        """Sets the effects of this Rule.

        An array of effectful Talang expressions in arrays that will be evaluated when a rule matches.  # noqa: E501

        :param effects: The effects of this Rule.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and effects is None:  # noqa: E501
            raise ValueError("Invalid value for `effects`, must not be `None`")  # noqa: E501

        self._effects = effects

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
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
