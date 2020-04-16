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


class LoyaltyProgram(object):
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
        'id': 'int',
        'account_id': 'int',
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'subscribed_applications': 'list[int]',
        'default_validity': 'str',
        'allow_subledger': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountID',
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'subscribed_applications': 'subscribedApplications',
        'default_validity': 'defaultValidity',
        'allow_subledger': 'allowSubledger'
    }

    def __init__(self, id=None, account_id=None, name=None, title=None, description=None, subscribed_applications=None, default_validity=None, allow_subledger=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyProgram - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._account_id = None
        self._name = None
        self._title = None
        self._description = None
        self._subscribed_applications = None
        self._default_validity = None
        self._allow_subledger = None
        self.discriminator = None

        self.id = id
        self.account_id = account_id
        self.name = name
        self.title = title
        self.description = description
        self.subscribed_applications = subscribed_applications
        self.default_validity = default_validity
        self.allow_subledger = allow_subledger

    @property
    def id(self):
        """Gets the id of this LoyaltyProgram.  # noqa: E501

        The ID of loyalty program.  # noqa: E501

        :return: The id of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoyaltyProgram.

        The ID of loyalty program.  # noqa: E501

        :param id: The id of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this LoyaltyProgram.  # noqa: E501

        The ID of the Talon.One account that owns this program.  # noqa: E501

        :return: The account_id of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this LoyaltyProgram.

        The ID of the Talon.One account that owns this program.  # noqa: E501

        :param account_id: The account_id of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this LoyaltyProgram.  # noqa: E501

        The internal name for the Loyalty Program.  # noqa: E501

        :return: The name of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoyaltyProgram.

        The internal name for the Loyalty Program.  # noqa: E501

        :param name: The name of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this LoyaltyProgram.  # noqa: E501

        The display title for the Loyalty Program.  # noqa: E501

        :return: The title of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LoyaltyProgram.

        The display title for the Loyalty Program.  # noqa: E501

        :param title: The title of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this LoyaltyProgram.  # noqa: E501

        Description of our Loyalty Program.  # noqa: E501

        :return: The description of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoyaltyProgram.

        Description of our Loyalty Program.  # noqa: E501

        :param description: The description of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def subscribed_applications(self):
        """Gets the subscribed_applications of this LoyaltyProgram.  # noqa: E501

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :return: The subscribed_applications of this LoyaltyProgram.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications

    @subscribed_applications.setter
    def subscribed_applications(self, subscribed_applications):
        """Sets the subscribed_applications of this LoyaltyProgram.

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :param subscribed_applications: The subscribed_applications of this LoyaltyProgram.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and subscribed_applications is None:  # noqa: E501
            raise ValueError("Invalid value for `subscribed_applications`, must not be `None`")  # noqa: E501

        self._subscribed_applications = subscribed_applications

    @property
    def default_validity(self):
        """Gets the default_validity of this LoyaltyProgram.  # noqa: E501

        Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like '1h' or '40m' or '30d'.  # noqa: E501

        :return: The default_validity of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_validity

    @default_validity.setter
    def default_validity(self, default_validity):
        """Sets the default_validity of this LoyaltyProgram.

        Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like '1h' or '40m' or '30d'.  # noqa: E501

        :param default_validity: The default_validity of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_validity is None:  # noqa: E501
            raise ValueError("Invalid value for `default_validity`, must not be `None`")  # noqa: E501

        self._default_validity = default_validity

    @property
    def allow_subledger(self):
        """Gets the allow_subledger of this LoyaltyProgram.  # noqa: E501

        Indicates if this program supports subledgers inside the program  # noqa: E501

        :return: The allow_subledger of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subledger

    @allow_subledger.setter
    def allow_subledger(self, allow_subledger):
        """Sets the allow_subledger of this LoyaltyProgram.

        Indicates if this program supports subledgers inside the program  # noqa: E501

        :param allow_subledger: The allow_subledger of this LoyaltyProgram.  # noqa: E501
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
        if not isinstance(other, LoyaltyProgram):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyProgram):
            return True

        return self.to_dict() != other.to_dict()
